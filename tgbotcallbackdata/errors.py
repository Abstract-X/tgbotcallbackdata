from dataclasses import dataclass

from xcept import BaseException_


@dataclass
class CallbackDataIsTooLargeError(BaseException_):

    data: str
    length: int
    length_limit: int
