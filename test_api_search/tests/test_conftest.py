import pytest

@pytest.fixture(scope="session")
def base_url():
    return "https://gw.alifshop.uz/web/client/search" 