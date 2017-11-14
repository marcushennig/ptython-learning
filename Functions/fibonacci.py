
def fibonacci(m: int, remainder='test'):
    """Computes the nth Fibonacci number
    n is an integer."""
    result = []
    a, b = 0, 1
    print(remainder)
    while a < m:
        result.append(a)
        a, b = b, a + b
    return result


def square(t: tuple):
    _y = ()
    for i in range(0, len(t)):
        _y += (t[i] * t[i],)
    return _y
