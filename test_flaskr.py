# Third party modules
import pytest
import pytest_mock

# First party modules
from app import create_app, db
from app.models.letter import Letter

# Unit tests for Letter
def test_current_status_outdated_postive():
    letter = Letter(id=1, tracking_number="ABCD123", status="DR1")
    new_code = 'ET2'
    if letter.current_status_outdated(new_code):
        letter.update_status(new_code)
    assert letter.status == new_code

def test_current_status_outdated_same():
    letter = Letter(id=1, tracking_number="ABCD1234", status="ET2")
    new_code = 'ET2'
    if letter.current_status_outdated(new_code):
        letter.update_status(new_code)
    assert letter.status == 'ET2'

def test_current_status_outdated_failure_less_than():
    letter = Letter(id=1, tracking_number="ABCD1234", status="ET2")
    new_code = 'DR1'
    if letter.current_status_outdated(new_code):
        letter.update_status(new_code)
    assert letter.status == 'ET2'


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"

    with app.app_context():
        db.create_all()
    with app.test_client() as client:
        yield client


def test_empty_database(client):
    response = client.post("/v1/letter")
    assert response.status_code == 404

''' def test_home_page_post_with_fixture(client,mocker):
    def mock_send_request(self):
        return 200
    mocker.patch(
        'app.request.request.Request.get_letter_details',mock_send_request
    )
    response = client.post('/letter/6P01007508742')
    assert response == 200
    assert b"Welcome to the Flask User Management Example!" not in response.data '''