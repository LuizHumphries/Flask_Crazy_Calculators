from src.errors.http_bad_request import HttpBadRequestError
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from typing import Dict

def handle_errors(error: Exception) -> Dict:
    if isinstance(error, (HttpUnprocessableEntityError, HttpBadRequestError)):
        return {
            "status_code": error.status_code,
            "body": {
                "errors": [{
                    "name": error.name,
                    "message": error.message
                }]
            }
        }
    return {
        "status_code": 500,
        "body": {
            "errors": [{
                "title": "Server Generic Error",
                "detail": str(error)
            }]
        }
    }