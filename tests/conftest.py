import pytest
from unittest.mock import Mock, MagicMock


@pytest.fixture
def mock():
    return Mock()


@pytest.fixture
def magic_mock():
    return MagicMock()
