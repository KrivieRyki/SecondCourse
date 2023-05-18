import os

import pytest
from starlette.testclient import TestClient

from course_fast_api import main
from course_fast_api.config import get_settings, Settings
from course_fast_api.main import create_application


def get_settings_override():
    return Settings(testing=1, database_url=os.environ.get("DATABASE_TEST_URL"))


@pytest.fixture(scope="module")
def test_app():
    app = create_application()
    app.dependency_overrides[get_settings] = get_settings_override
    with TestClient(main.app) as test_client:

        # testing
        yield test_client

    # tear down