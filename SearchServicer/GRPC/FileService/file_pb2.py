# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: file.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nfile.proto\"\x0f\n\rNoFileMessage\"\x14\n\x04Name\x12\x0c\n\x04name\x18\x01 \x01(\t\" \n\x08\x46ileList\x12\x14\n\x05\x66iles\x18\x01 \x03(\x0b\x32\x05.File\"H\n\x04\x46ile\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x66ile_format\x18\x03 \x01(\t\x12\x0c\n\x04\x66ile\x18\x04 \x01(\x0c\x32\xa4\x01\n\x0b\x46ileService\x12\x1a\n\nCreateFile\x12\x05.File\x1a\x05.File\x12\x17\n\x07GetFile\x12\x05.Name\x1a\x05.File\x12(\n\x0bGetFileList\x12\x0e.NoFileMessage\x1a\t.FileList\x12\x1a\n\nUpdateFile\x12\x05.File\x1a\x05.File\x12\x1a\n\nDeleteFile\x12\x05.Name\x1a\x05.Fileb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'file_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _NOFILEMESSAGE._serialized_start=14
  _NOFILEMESSAGE._serialized_end=29
  _NAME._serialized_start=31
  _NAME._serialized_end=51
  _FILELIST._serialized_start=53
  _FILELIST._serialized_end=85
  _FILE._serialized_start=87
  _FILE._serialized_end=159
  _FILESERVICE._serialized_start=162
  _FILESERVICE._serialized_end=326
# @@protoc_insertion_point(module_scope)
