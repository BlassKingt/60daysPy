from utils import add,is_even,greet

def test_add():
    assert add(1, 2) == 3
    assert add(10, 15) == 25

def test_is_even():
    assert is_even(4) is True
    assert is_even(5) is False

def test_greet():
    assert "Hello" in greet("Alice")

