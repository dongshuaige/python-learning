"""
自定义模块
"""
# __all__ = ["test_a"]


def test_a(a, b):
    return a + b


def test_b(a, b):
    return a - b


if __name__ == '__main__':
    test_a(1, 2)
