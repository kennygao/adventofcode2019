def compose(f, *functions):
    if not functions:
        return f
    else:
        return lambda x: compose(*functions)(f(x))


def test_compose():
    a = lambda x: x + 3
    b = lambda x: x * 3
    c = lambda x: x * x
    print(f'{c(b(a(1)))=}')
    print(f'{compose(a, b, c)(1)=}')


if __name__ == '__main__':
    test_compose()
