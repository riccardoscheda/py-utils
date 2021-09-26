import sys
import pytest

from sklearn.datasets import load_iris


# scope='session' means that the same value of "iris" will be shared between test (1 download)
@pytest.fixture(scope='session')
def iris():

    data = load_iris()

    yield data


# This fixture capture the std output
@pytest.fixture
def capture_stdout(monkeypatch):

    buffer = {'stdout': '', 'write_calls': 0}

    def fake_write(s):
        buffer['stdout'] += s
        buffer['write_calls'] += 1

    monkeypatch.setattr(sys.stdout, 'write', fake_write)
    return buffer
