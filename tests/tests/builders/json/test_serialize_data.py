import pytest

from tgbotcallbackdata import JSONBuilder
from tests.data import DATA_SERIALIZATION_TEST_DATA


@pytest.mark.parametrize(
    ("data", "expected_result"),
    DATA_SERIALIZATION_TEST_DATA
)
def test_behavior(data, expected_result):
    builder = JSONBuilder()
    serialized_data = builder.serialize_data(data)

    assert serialized_data == expected_result
