import pytest


@pytest.mark.parametrize('test_input,expected', [
    (5, 5),
    (4, 4),
    ('avocado', 'avocado')
])
def test_nestedcv(test_input, expected):
    assert test_input == expected


@pytest.mark.skip(reason='This test will be skipped')
def test_skipped():
    assert 5 == 2


@pytest.mark.xfail
def test_failed():
    # Don't use for testing if an error should be raised (see next test)
    assert 2 == 5


def test_raised_error():
    # Use when the code should raise an error
    with pytest.raises(ValueError):
        raise ValueError()


def test_fixture(iris):
    # Here "iris" is a fixture (conftest.py) and is the same for all test
    # The function "iris" inside conftest.py will be called
    assert iris


# use capture_stdout fixture
def test_print(capture_stdout):
    print('hello')
    assert capture_stdout['stdout'] == 'hello\n'


if __name__ == '__main__':
    pass
