
import pytest

class customError(Exception):
    def __init__(self, message = "value not in range"):
        #self.input_ = input_
        self.message = message
        super().__init__(self.message)


def test_generic():
    a = 5 
    with pytest.raises(customError):
        if a not in range(10,20):
            raise customError

