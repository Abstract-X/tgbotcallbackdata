from typing import Union
import json

from tgbotcallbackdata.builders.base import AbstractBuilder


class JSONBuilder(AbstractBuilder):

    def serialize_data(self, data: Union[str, int, list]) -> str:
        return json.dumps(data, separators=(",", ":"))
