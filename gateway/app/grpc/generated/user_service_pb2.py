# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: user_service.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'user_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12user_service.proto\x12\x0cuser_service\" \n\x12GetUserByIdRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"`\n\x13GetUserByIdResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x17\n\x0fhashed_password\x18\x03 \x01(\t\x12\x15\n\rrefresh_token\x18\x04 \x01(\t\"\x1f\n\x11\x44\x65leteUserRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"%\n\x12\x44\x65leteUserResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"R\n\x11\x43reateUserRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x17\n\x0fhashed_password\x18\x02 \x01(\t\x12\x15\n\rrefresh_token\x18\x03 \x01(\t\"/\n\x12\x43reateUserResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05\x65mail\x18\x02 \x01(\t\"\x7f\n\x11UpdateUserRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x1c\n\x0fhashed_password\x18\x02 \x01(\tH\x00\x88\x01\x01\x12\x1a\n\rrefresh_token\x18\x03 \x01(\tH\x01\x88\x01\x01\x42\x12\n\x10_hashed_passwordB\x10\n\x0e_refresh_token\"/\n\x12UpdateUserResponse\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05\x65mail\x18\x02 \x01(\t2\xdc\x02\n\x0bUserService\x12T\n\x0bGetUserById\x12 .user_service.GetUserByIdRequest\x1a!.user_service.GetUserByIdResponse\"\x00\x12Q\n\nUpdateUser\x12\x1f.user_service.UpdateUserRequest\x1a .user_service.UpdateUserResponse\"\x00\x12Q\n\nCreateUser\x12\x1f.user_service.CreateUserRequest\x1a .user_service.CreateUserResponse\"\x00\x12Q\n\nDeleteUser\x12\x1f.user_service.DeleteUserRequest\x1a .user_service.DeleteUserResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_GETUSERBYIDREQUEST']._serialized_start=36
  _globals['_GETUSERBYIDREQUEST']._serialized_end=68
  _globals['_GETUSERBYIDRESPONSE']._serialized_start=70
  _globals['_GETUSERBYIDRESPONSE']._serialized_end=166
  _globals['_DELETEUSERREQUEST']._serialized_start=168
  _globals['_DELETEUSERREQUEST']._serialized_end=199
  _globals['_DELETEUSERRESPONSE']._serialized_start=201
  _globals['_DELETEUSERRESPONSE']._serialized_end=238
  _globals['_CREATEUSERREQUEST']._serialized_start=240
  _globals['_CREATEUSERREQUEST']._serialized_end=322
  _globals['_CREATEUSERRESPONSE']._serialized_start=324
  _globals['_CREATEUSERRESPONSE']._serialized_end=371
  _globals['_UPDATEUSERREQUEST']._serialized_start=373
  _globals['_UPDATEUSERREQUEST']._serialized_end=500
  _globals['_UPDATEUSERRESPONSE']._serialized_start=502
  _globals['_UPDATEUSERRESPONSE']._serialized_end=549
  _globals['_USERSERVICE']._serialized_start=552
  _globals['_USERSERVICE']._serialized_end=900
# @@protoc_insertion_point(module_scope)
