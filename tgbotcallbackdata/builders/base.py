from abc import ABC, abstractmethod
from typing import Union

from tgbotcallbackdata.types import Key, Value
from tgbotcallbackdata import errors


DATA_SIZE_LIMIT = 64  # https://core.telegram.org/bots/api#inlinekeyboardbutton


class AbstractBuilder(ABC):

    def build_data(self, key: Key, value: Value = None) -> str:
        data = self.serialize_data([key, value] if value is not None else key)
        data_length = len(data.encode())
        if data_length > DATA_SIZE_LIMIT:
            raise errors.CallbackDataIsTooLargeError(
                "the callback data size exceeds the limit ({length}/{length_limit} bytes, {data!r})!",
                data=data, length=data_length, length_limit=DATA_SIZE_LIMIT
            )

        return data

    @abstractmethod
    def serialize_data(self, data: Union[str, int, list]) -> str:
        pass
