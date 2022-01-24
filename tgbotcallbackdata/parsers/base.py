from abc import ABC, abstractmethod
from typing import Tuple, Union

from tgbotcallbackdata.types import Key, Value


class AbstractParser(ABC):

    def parse_data(self, data: str) -> Tuple[Key, Value]:
        data = self.deserialize_data(data)
        if isinstance(data, list):
            key, value = data
        else:
            key = data
            value = None

        return key, value

    @abstractmethod
    def deserialize_data(self, data: str) -> Union[str, int, list]:
        pass
