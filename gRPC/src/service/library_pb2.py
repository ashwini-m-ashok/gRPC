# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: library.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rlibrary.proto\"j\n\x04\x42ook\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\x15\n\rpublishedYear\x18\x04 \x01(\x05\x12\x0c\n\x04isbn\x18\x01 \x02(\t\x12\x1e\n\x05genre\x18\x05 \x01(\x0e\x32\x06.Genre:\x07UNKNOWN\"\xa0\x01\n\rInventoryItem\x12\x11\n\tinvNumber\x18\x01 \x02(\x05\x12\x15\n\x04\x62ook\x18\x02 \x01(\x0b\x32\x05.BookH\x00\x12\x30\n\x06status\x18\x03 \x01(\x0e\x32\x15.InventoryItem.Status:\tAVAILABLE\"\"\n\x06Status\x12\r\n\tAVAILABLE\x10\x00\x12\t\n\x05TAKEN\x10\x01\x42\x0f\n\rinventoryType\"\x1e\n\x0eGetBookRequest\x12\x0c\n\x04isbn\x18\x01 \x02(\t\"4\n\x0cGetBookReply\x12\x13\n\x04\x62ook\x18\x01 \x01(\x0b\x32\x05.Book\x12\x0f\n\x07message\x18\x02 \x02(\t\"w\n\x11\x43reateBookRequest\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\x15\n\rpublishedYear\x18\x04 \x01(\x05\x12\x0c\n\x04isbn\x18\x01 \x02(\t\x12\x1e\n\x05genre\x18\x05 \x01(\x0e\x32\x06.Genre:\x07UNKNOWN\"\"\n\x0f\x43reateBookReply\x12\x0f\n\x07message\x18\x01 \x02(\t*N\n\x05Genre\x12\x0b\n\x07MYSTERY\x10\x00\x12\x0b\n\x07ROMANCE\x10\x01\x12\x0b\n\x07\x46ICTION\x10\x02\x12\x11\n\rAUTOBIOGRAPHY\x10\x03\x12\x0b\n\x07UNKNOWN\x10\x04\x32u\n\x10InventoryService\x12+\n\x07GetBook\x12\x0f.GetBookRequest\x1a\r.GetBookReply\"\x00\x12\x34\n\nCreateBook\x12\x12.CreateBookRequest\x1a\x10.CreateBookReply\"\x00')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'library_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GENRE._serialized_start=531
  _GENRE._serialized_end=609
  _BOOK._serialized_start=17
  _BOOK._serialized_end=123
  _INVENTORYITEM._serialized_start=126
  _INVENTORYITEM._serialized_end=286
  _INVENTORYITEM_STATUS._serialized_start=235
  _INVENTORYITEM_STATUS._serialized_end=269
  _GETBOOKREQUEST._serialized_start=288
  _GETBOOKREQUEST._serialized_end=318
  _GETBOOKREPLY._serialized_start=320
  _GETBOOKREPLY._serialized_end=372
  _CREATEBOOKREQUEST._serialized_start=374
  _CREATEBOOKREQUEST._serialized_end=493
  _CREATEBOOKREPLY._serialized_start=495
  _CREATEBOOKREPLY._serialized_end=529
  _INVENTORYSERVICE._serialized_start=611
  _INVENTORYSERVICE._serialized_end=728
# @@protoc_insertion_point(module_scope)
