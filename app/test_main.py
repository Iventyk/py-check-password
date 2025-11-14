import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param("1@Qwerty", True, id="8 characters"),
        pytest.param("01234567", False, id="numbers"),
        pytest.param("q$@#&!-_", False, id="special character"),
        pytest.param("1@Qrtyuiqwertyui", True, id="16 characters"),
        pytest.param("1@Qrtyuiqwertyuiq", False, id="17 characters"),
        pytest.param("1@Qwert", False, id="7 characters"),
        pytest.param("", False, id="empty string"),
        pytest.param("1@Q", False, id="only requested"),
        pytest.param("Привіт1@Q", False, id="cyrillic"),
    ]
)
def test_check_password(password, expected):
    assert check_password(password) is expected
