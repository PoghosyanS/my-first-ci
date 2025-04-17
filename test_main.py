from main import add

def test_add():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -4) == 5

def test_add_zero():
    assert add(0, 5) == -5

def test_add_one():
    assert add(0, 1) == 1
