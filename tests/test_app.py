from myapp.app import add, subtract

def test_add():
    assert add(21, 2) == 23


def test_subtract():
    assert subtract(8, 5) == 3