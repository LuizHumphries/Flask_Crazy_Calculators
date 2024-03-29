from typing import Dict, List
from src.drivers.numpy_handler import NumpyHandler
from src.calculators.calculator_2 import Calculator2

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandler:
    def standard_deviation(self, numbers: List) -> float:
        return 3

def test_calculate_integration():
    mock_request = MockRequest(body={ "numbers": [2.12, 4.62, 1.32] })
    driver = NumpyHandler()
    calculate_2 = Calculator2(driver)
    formated_reponse = calculate_2.calculate(mock_request)

    assert isinstance(formated_reponse, dict)
    assert formated_reponse == {'data': {'Calculator': 2, 'result': 0.08}}

def test_calculate():
    mock_request = MockRequest(body={ "numbers": [2.12, 4.62, 1.32] })
    driver = MockDriverHandler()
    calculate_2 = Calculator2(driver)
    formated_reponse = calculate_2.calculate(mock_request)

    assert isinstance(formated_reponse, dict)
    assert formated_reponse == {'data': {'Calculator': 2, 'result': 0.33}}