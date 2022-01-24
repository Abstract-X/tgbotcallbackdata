import pytest

from tgbotcallbackdata import JSONParser
from tests.data import DATA_DESERIALIZING_TEST_DATA


@pytest.mark.parametrize(
    ("data", "expected_result"),
    DATA_DESERIALIZING_TEST_DATA
)
def test_behavior(data, expected_result):
    parser = JSONParser()
    deserialized_data = parser.deserialize_data(data)

    assert deserialized_data == expected_result
