import pytest
from starlette.testclient import TestClient

from app import main
from app.config import carregar_config, Config


def get_settings_override():
    return Config(testing=1)


@pytest.fixture(scope="module")
def test_app():
    main.app.dependency_overrides[carregar_config] = get_settings_override
    with TestClient(main.app) as test_client:
        yield test_client
