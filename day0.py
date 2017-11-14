# This is my first python program


def square(t: tuple):
    _y = ()
    for i in range(0, len(t)):
        _y += (t[i] * t[i],)
    return _y


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


'''Build  dictionary '''
lm = [j for j in range(0, 100)]
print(lm)
d = {(i, i): i ** 2 for i in range(0, 3)}
if (2, 2) in d:
    print(d[(2, 2)])
print(d)

for key in d.keys():
    print(f'For {key} found value {d[key]}')

