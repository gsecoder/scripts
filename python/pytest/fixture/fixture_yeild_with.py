import pytest

@pytest.fixture(scope="module")
def smtp_connection():
    with smtp.SMTP("smtp.gmail.com", 587, timeout=5) as smtp_connection:
        yield smtp_connection  # provide the fixture value