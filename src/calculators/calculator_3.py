from typing import List, Dict
from flask import Request as FlaskRequest
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from src.errors.http_bad_request import HttpBadRequestError

class Calculator3:

    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)

        variance = self.__calculate_variance(input_data)
        mulitplication = self.__calculate_multiplication_all(input_data) 
        self.__verify_results(variance, mulitplication) 

        formated_response = self.__format_response(variance)
        return formated_response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("Body wrongly formated")
        input_data = body["numbers"]
        return input_data
    
    def __calculate_variance(self, numbers: List[float]) -> float:
        return self.__driver_handler.variance(numbers)
    
    def __calculate_multiplication_all(self, numbers: List[float]) -> float:
        return self.__driver_handler.multiply_all(numbers)
    
    def __verify_results(self, variance: float, multiplication: float) -> None:
        if variance < multiplication:
            raise HttpBadRequestError("Process fail: Variance < Multiplication")
    
    def __format_response(self, variance: float) -> Dict:
        return {
            "data": {
                "Calculator": 3,
                "result": variance,
                "Success": True
            }
        }
