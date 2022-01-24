import pytest

from tgbotcallbackdata import JSONParser
from tests.data import DATA_PARSING_TEST_DATA


@pytest.mark.parametrize(
    ("callback_data", "expected_result"),
    DATA_PARSING_TEST_DATA
)
def test_behavior(callback_data, expected_result):
    parser = JSONParser()
    key, value = parser.parse_data(callback_data)

    assert (key, value) == expected_result
