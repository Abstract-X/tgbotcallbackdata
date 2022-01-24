import pytest

from tgbotcallbackdata import JSONBuilder
from tgbotcallbackdata.builders.base import DATA_SIZE_LIMIT
from tgbotcallbackdata.errors import CallbackDataIsTooLargeError
from tests.data import DATA_BUILDING_TEST_DATA


@pytest.mark.parametrize(
    ("key", "value", "expected_result"),
    DATA_BUILDING_TEST_DATA
)
def test_behavior(key, value, expected_result):
    builder = JSONBuilder()
    callback_data = builder.build_data(key, value)

    assert callback_data == expected_result


def test_callback_data_over_limit():
    builder = JSONBuilder()

    with pytest.raises(CallbackDataIsTooLargeError):
        builder.build_data("a" * (DATA_SIZE_LIMIT + 1))
