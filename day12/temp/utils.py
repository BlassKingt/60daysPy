
def say_hello(name):
    return f"Hello, {name}!"


def test_func():
    print(say_hello("Alex"))

# 练习 3
if __name__ == "__main__":
    test_func()
    print("utils.py 正在被直接运行")
