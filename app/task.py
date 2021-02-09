from app import request_handler
from app.request.request import Request

def process_letters_task(letters):
    if letters:
        for letter in letters:
            process_letter_update(letter)

def process_letter_update(letter):
    response = request_handler.get_letter_details(letter.tracking_number)
    if response:
        latest_event_code = request_handler.get_latest_event_code(response)
        if latest_event_code:
            if letter.current_status_outdated(latest_event_code):
                letter.update_status(latest_event_code)
                letter.update()