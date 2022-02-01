import kalk


def test_sum():
    a, b = 1, 2
    expected = 3
    result = kalk.sum(a, b)
    assert result == expected, f'Expected {result!r} to be {expected!r}'

    test_data = (
        ((1, 2, 3, 4), 10),
        ((1, 2, 3, 4, -5), 5),
        ((1j, 2, 3, 4, -5), 1j + 4),
        ((1j, 2, 3j, 4, -5), 4j + 1),
    )
    for arguments, expected in test_data:
        result = kalk.sum(*arguments)
        assert result == expected, f'Expected {result!r} to be {expected!r}'


def test_sub():
    a, b = 1, 2
    expected = -1
    result = kalk.sub(a, b)
    assert result == expected, f'Expected {result!r} to be {expected!r}'



def test_mul():
    a, b = 1, -2
    expected = -2
    result = kalk.mul(a, b)
    assert result == expected, f'Expected {result!r} to be {expected!r}'

