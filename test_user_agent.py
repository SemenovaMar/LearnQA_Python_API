from contextlib import contextmanager
import requests
import pytest

@contextmanager
def does_not_raise():
    yield

@pytest.mark.parametrize(
    "example_input,expectation"
[(3, does_not_raise()),
        (2, does_not_raise()),
        (1, does_not_raise()),
        (0, pytest.raises(ZeroDivisionError))
    ]

class TestUserAgent:
    def setup(self):


testev = [

    ()




]

response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check")
print(response.headers)













