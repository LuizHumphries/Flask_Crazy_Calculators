from typing import Dict, List
from src.drivers.numpy_handler import NumpyHandler
from src.calculators.calculator_4 import Calculator4

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandler:
    def avarage(self, numbers: List) -> float:
        return 10

def test_calculate_integration():
    mock_request = MockRequest(body={ "numbers": [2.12, 4.62, 1.32] })
    driver = NumpyHandler()
    calculate_4 = Calculator4(driver)
    formated_reponse = calculate_4.calculate(mock_request)

    assert isinstance(formated_reponse, dict)
    assert formated_reponse == {'data': {'Calculator': 4, 'result': 2.686666666666667}}

def test_calculate():
    mock_request = MockRequest(body={ "numbers": [2.12, 4.62, 1.32] })
    driver = MockDriverHandler()
    calculate_4 = Calculator4(driver)
    formated_reponse = calculate_4.calculate(mock_request)

    assert isinstance(formated_reponse, dict)
    assert formated_reponse == {'data': {'Calculator': 4, 'result': 10}}