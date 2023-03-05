from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserId(_message.Message):
    __slots__ = ["user"]
    USER_FIELD_NUMBER: _ClassVar[int]
    user: str
    def __init__(self, user: _Optional[str] = ...) -> None: ...

class UserName(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class searchFile(_message.Message):
    __slots__ = ["file", "file_format", "name", "user_id"]
    FILE_FIELD_NUMBER: _ClassVar[int]
    FILE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    file: bytes
    file_format: str
    name: str
    user_id: str
    def __init__(self, user_id: _Optional[str] = ..., name: _Optional[str] = ..., file_format: _Optional[str] = ..., file: _Optional[bytes] = ...) -> None: ...

class searchFileList(_message.Message):
    __slots__ = ["files"]
    FILES_FIELD_NUMBER: _ClassVar[int]
    files: _containers.RepeatedCompositeFieldContainer[searchFile]
    def __init__(self, files: _Optional[_Iterable[_Union[searchFile, _Mapping]]] = ...) -> None: ...

class searchUser(_message.Message):
    __slots__ = ["age", "email", "id", "name", "password"]
    AGE_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    age: int
    email: str
    id: int
    name: str
    password: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., age: _Optional[int] = ..., password: _Optional[str] = ..., email: _Optional[str] = ...) -> None: ...

class searchUserList(_message.Message):
    __slots__ = ["users"]
    USERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[searchUser]
    def __init__(self, users: _Optional[_Iterable[_Union[searchUser, _Mapping]]] = ...) -> None: ...
