from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ID(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class NoMessage(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class User(_message.Message):
    __slots__ = ["age", "email", "id", "name", "password"]
    AGE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    age: int
    email: str
    id: str
    name: str
    password: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., age: _Optional[int] = ..., password: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...
