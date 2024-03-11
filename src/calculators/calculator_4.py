from typing import List, Dict
from flask import Request as FlaskRequest
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class Calculator4:

    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)

        variance = self.__calculate_avarage(input_data)
        formated_response = self.__format_response(variance)

        return formated_response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("Body wrongly formated")
        input_data = body["numbers"]
        return input_data
    
    def __calculate_avarage(self, numbers: List[float]) -> float:
        return self.__driver_handler.avarage(numbers)
    
    def __format_response(self, variance: float) -> Dict:
        return {
            "data": {
                "Calculator": 4,
                "result": variance,
            }
        }
