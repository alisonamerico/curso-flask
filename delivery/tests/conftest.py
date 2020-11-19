# conftest

import pytest
from delivery.app import create_app


@pytest.fixture(scope="module")
def app():
    """Instance of Mian flask app"""
    return create_app()
