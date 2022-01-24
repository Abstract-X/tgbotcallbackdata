from typing import Union
import json

from tgbotcallbackdata.parsers.base import AbstractParser


class JSONParser(AbstractParser):

    def deserialize_data(self, data: str) -> Union[str, int, list]:
        return json.loads(data)
