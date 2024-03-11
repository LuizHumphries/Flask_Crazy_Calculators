from typing import Dict
from pytest import raises
from src.calculators.calculator_1 import Calculator1

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculate():
    mock_request = MockRequest(body={ "number": 1 })
    calculate_1 = Calculator1()
    response = calculate_1.calculate(mock_request)

    assert isinstance(response, dict)
    assert "data" in response
    assert "Calculator" in response["data"]
    assert "result" in response["data"]

    assert response["data"]["Calculator"] == 1
    assert response["data"]["result"] == 14.25

def test_calculate_with_body_error():
    mock_request_error = MockRequest(body={ "somethingelse": 1 })
    calculator_1 = Calculator1()
    with raises(Exception) as excinfo:
        calculator_1.calculate(mock_request_error)
    
    assert str(excinfo.value) == "Body wrongly formated!"