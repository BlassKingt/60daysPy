
def test_add():
    assert 2 + 3 == 5

def test_add2():
    assert 2 + 3 == 10

def test_string():
    assert 'Hello' + ' ' + 'World' == 'Hello World'

# 文件名必须叫test_xxx.py
# pytest -v xx.py 即可, -v可看更多细节