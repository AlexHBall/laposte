from flask import Blueprint, jsonify
from flask_cors import CORS

from app import request_handler
from app.models.letter import Letter
from app.request.request import Request

import json

v1 = Blueprint("v1", __name__)
CORS(v1)

LA_POSTE_ERROR_MSG = "Error Interacting with LaPoste API"
HTTP_OK = 200
HTTP_NOT_FOUND = 404
HTTP_CONFLICT = 409
HTTP_SEVER_ERROR = 502

@v1.route('/letter', methods=['POST'])
def update_all_letters():
    letters = Letter.query.all()
    if letters:
        for letter in letters:
            process_letter_update(letter)
        return "Letters updating", HTTP_OK
    return "No letters in the database", HTTP_NOT_FOUND

@v1.route('/letter/<string:tracking_number>', methods=['POST'])
def get_letter_info(tracking_number):
    if Letter.tracking_number_is_valid(tracking_number):
        response = request_handler.get_letter_details(tracking_number)
        latest_event_code = get_latest_event_code(response)
        if latest_event_code:
            letter = Letter.query.filter_by(
                tracking_number=tracking_number).first()
            if not letter:
                letter = Letter(tracking_number=tracking_number,
                                status=latest_event_code)
                letter.add()
                msg = "Letter added"
            else:
                if letter.current_status_outdated(latest_event_code):
                    letter.update_status(latest_event_code)
                    letter.update()
                    msg = "Letter Status Updated"
                return "Letter Status Already Up To Date", HTTP_CONFLICT
            return msg, HTTP_OK
        return LA_POSTE_ERROR_MSG, HTTP_SEVER_ERROR
    return "Invalid tracking number format", 422


def get_latest_event_code(response):
    if response:
        try:
            if response['returnCode'] == HTTP_OK:
                latest_event_code = response['shipment']['event'][-1]['code']
                return latest_event_code if latest_event_code else None
        except KeyError:
            return None

def process_letter_update(letter):
    print(f'Updating letter [{letter}]')
    response = request_handler.get_letter_details(letter.tracking_number)
    if response:
        latest_event_code = get_latest_event_code(response)
        if latest_event_code:
            if letter.current_status_outdated(latest_event_code):
                letter.update_status(latest_event_code)
                letter.update()