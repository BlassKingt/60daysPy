
def test_01():
    assert 3 * 3 == 9
    assert 2 + 2 == 5

def test_02():
    assert "test" in "automation testing"

def test_03():
    age = 18
    assert 10 < age < 20

def test_04():
    assert set([1,2,2,3]) == {1,2,3}

def test_05():
    flag = True
    assert flag
