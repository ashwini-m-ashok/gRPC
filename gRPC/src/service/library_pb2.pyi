from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

AUTOBIOGRAPHY: Genre
DESCRIPTOR: _descriptor.FileDescriptor
FICTION: Genre
MYSTERY: Genre
ROMANCE: Genre
UNKNOWN: Genre

class Book(_message.Message):
    __slots__ = ["author", "genre", "isbn", "publishedYear", "title"]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    GENRE_FIELD_NUMBER: _ClassVar[int]
    ISBN_FIELD_NUMBER: _ClassVar[int]
    PUBLISHEDYEAR_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    author: str
    genre: Genre
    isbn: str
    publishedYear: int
    title: str
    def __init__(self, title: _Optional[str] = ..., author: _Optional[str] = ..., publishedYear: _Optional[int] = ..., isbn: _Optional[str] = ..., genre: _Optional[_Union[Genre, str]] = ...) -> None: ...

class CreateBookReply(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class CreateBookRequest(_message.Message):
    __slots__ = ["author", "genre", "isbn", "publishedYear", "title"]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    GENRE_FIELD_NUMBER: _ClassVar[int]
    ISBN_FIELD_NUMBER: _ClassVar[int]
    PUBLISHEDYEAR_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    author: str
    genre: Genre
    isbn: str
    publishedYear: int
    title: str
    def __init__(self, title: _Optional[str] = ..., author: _Optional[str] = ..., publishedYear: _Optional[int] = ..., isbn: _Optional[str] = ..., genre: _Optional[_Union[Genre, str]] = ...) -> None: ...

class GetBookReply(_message.Message):
    __slots__ = ["book", "message"]
    BOOK_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    book: Book
    message: str
    def __init__(self, book: _Optional[_Union[Book, _Mapping]] = ..., message: _Optional[str] = ...) -> None: ...

class GetBookRequest(_message.Message):
    __slots__ = ["isbn"]
    ISBN_FIELD_NUMBER: _ClassVar[int]
    isbn: str
    def __init__(self, isbn: _Optional[str] = ...) -> None: ...

class InventoryItem(_message.Message):
    __slots__ = ["book", "invNumber", "status"]
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AVAILABLE: InventoryItem.Status
    BOOK_FIELD_NUMBER: _ClassVar[int]
    INVNUMBER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TAKEN: InventoryItem.Status
    book: Book
    invNumber: int
    status: InventoryItem.Status
    def __init__(self, invNumber: _Optional[int] = ..., book: _Optional[_Union[Book, _Mapping]] = ..., status: _Optional[_Union[InventoryItem.Status, str]] = ...) -> None: ...

class Genre(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
