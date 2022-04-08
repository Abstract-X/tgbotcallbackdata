from dataclasses import dataclass

from xcept import Exception_


@dataclass
class CallbackDataIsTooLargeError(Exception_):
    data: str
    length: int
    length_limit: int
