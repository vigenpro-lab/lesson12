from typing import Union

from src.decorators import log


@log()
def add(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    return x + y


@log(filename="test.log")
def divide(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    return x / y


def test_add() -> None:
    result = add(2, 3)
    assert result == 5


def test_divide() -> None:
    result = divide(6, 2)
    assert result == 3


if __name__ == "__main__":
    test_add()
    test_divide()
