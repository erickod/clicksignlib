import pytest
from unittest.mock import Mock, MagicMock, patch as upatch


@pytest.fixture
def mock():
    return Mock()

@pytest.fixture
def magic_mock():
    return MagicMock()

@pytest.fixture
def patch(*args, **kwargs):
    return upatch
