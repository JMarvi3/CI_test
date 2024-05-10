import pytest
from app.app import App


def test_init_with_valid_inputs():
    app = App("Hello", 1)
    assert app.a == "Hello"
    assert app.b == 1


def test_init_with_invalid_a_type():
    with pytest.raises(TypeError):
        App(123, 1)


def test_init_with_invalid_b_type():
    with pytest.raises(TypeError):
        App("Hello", "World")


def test_sum():
    app = App("Hello", 1)
    assert app.concat == "Hello1"
