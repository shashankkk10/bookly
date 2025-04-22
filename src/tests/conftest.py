from src.db.main import get_session
from src.auth.dependencies import AccessTokenBearer, RoleChecker, RefreshTokenBearer
from src import app
from unittest.mock import Mock
from fastapi.testclient import TestClient
import pytest

mock_session = Mock()
mock_user_service = Mock()
mock_book_service = Mock()

access_token_bearer = AccessTokenBearer()
refresh_token_bearer = RefreshTokenBearer()
role_checker = RoleChecker(["admin"])

def get_mock_session():
    yield mock_session

app.dependency_overrides[get_session] = get_mock_session
app.dependency_overrides[role_checker] = Mock()
app.dependency_overrides[refresh_token_bearer] = Mock()
 

@pytest.fixture
def fake_session():
    return mock_session

@pytest.fixture
def fake_user_service():
    return mock_user_service

@pytest.fixture
def fake_book_service():
    return mock_book_service

@pytest.fixture
def test_client():
    return TestClient(app)

