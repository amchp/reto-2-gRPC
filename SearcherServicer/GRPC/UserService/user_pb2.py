# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nuser.proto\"\x0f\n\rNoUserMessage\"\x10\n\x02ID\x12\n\n\x02id\x18\x01 \x01(\x05\"]\n\x04User\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03\x61ge\x18\x03 \x01(\x05\x12\x10\n\x08password\x18\x04 \x01(\t\x12\x12\n\x05\x65mail\x18\x05 \x01(\tH\x00\x88\x01\x01\x42\x08\n\x06_email\" \n\x08UserList\x12\x14\n\x05users\x18\x01 \x03(\x0b\x32\x05.User2\xa0\x01\n\x0bUserService\x12\x1a\n\nCreateUser\x12\x05.User\x1a\x05.User\x12\x15\n\x07GetUser\x12\x03.ID\x1a\x05.User\x12(\n\x0bGetUserList\x12\x0e.NoUserMessage\x1a\t.UserList\x12\x1a\n\nUpdateUser\x12\x05.User\x1a\x05.User\x12\x18\n\nDeleteUser\x12\x03.ID\x1a\x05.Userb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _NOUSERMESSAGE._serialized_start=14
  _NOUSERMESSAGE._serialized_end=29
  _ID._serialized_start=31
  _ID._serialized_end=47
  _USER._serialized_start=49
  _USER._serialized_end=142
  _USERLIST._serialized_start=144
  _USERLIST._serialized_end=176
  _USERSERVICE._serialized_start=179
  _USERSERVICE._serialized_end=339
# @@protoc_insertion_point(module_scope)
