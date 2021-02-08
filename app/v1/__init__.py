from flask import Blueprint, jsonify
from flask_cors import CORS

from app import request_handler, redis,queue
from app.models.letter import Letter
from app.request.request import Request
from app.task import process_letters_task
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
    job = queue.enqueue(process_letters_task,letters)
    return f"{job.id}", HTTP_OK

@v1.route('/letter/<string:tracking_number>', methods=['POST'])
def get_letter_info(tracking_number):
    if Letter.tracking_number_is_valid(tracking_number):
        response = request_handler.get_letter_details(tracking_number)
        latest_event_code = request_handler.get_latest_event_code(response)
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
