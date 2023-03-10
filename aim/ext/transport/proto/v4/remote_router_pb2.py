# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: remote_router.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13remote_router.proto\x1a\x15remote_tracking.proto\"\x10\n\x0eVersionRequest\"\x8f\x01\n\x0fVersionResponse\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\'\n\x06status\x18\x02 \x01(\x0e\x32\x17.VersionResponse.Status\x12%\n\texception\x18\x03 \x01(\x0b\x32\x12.ExceptionResponse\"\x1b\n\x06Status\x12\x06\n\x02OK\x10\x00\x12\t\n\x05\x45RROR\x10\x01\"&\n\x10HeartbeatRequest\x12\x12\n\nclient_uri\x18\x01 \x01(\t\"\x82\x01\n\x11HeartbeatResponse\x12)\n\x06status\x18\x01 \x01(\x0e\x32\x19.HeartbeatResponse.Status\x12%\n\texception\x18\x02 \x01(\x0b\x32\x12.ExceptionResponse\"\x1b\n\x06Status\x12\x06\n\x02OK\x10\x00\x12\t\n\x05\x45RROR\x10\x01\"$\n\x0e\x43onnectRequest\x12\x12\n\nclient_uri\x18\x01 \x01(\t\"\xa2\x01\n\x0f\x43onnectResponse\x12\x0c\n\x04port\x18\x01 \x01(\t\x12\x14\n\x0cworker_index\x18\x02 \x01(\t\x12\'\n\x06status\x18\x03 \x01(\x0e\x32\x17.ConnectResponse.Status\x12%\n\texception\x18\x04 \x01(\x0b\x32\x12.ExceptionResponse\"\x1b\n\x06Status\x12\x06\n\x02OK\x10\x00\x12\t\n\x05\x45RROR\x10\x01\"&\n\x10ReconnectRequest\x12\x12\n\nclient_uri\x18\x01 \x01(\t\"\x90\x01\n\x11ReconnectResponse\x12\x0c\n\x04port\x18\x01 \x01(\t\x12)\n\x06status\x18\x02 \x01(\x0e\x32\x19.ReconnectResponse.Status\x12%\n\texception\x18\x03 \x01(\x0b\x32\x12.ExceptionResponse\"\x1b\n\x06Status\x12\x06\n\x02OK\x10\x00\x12\t\n\x05\x45RROR\x10\x01\"\'\n\x11\x44isconnectRequest\x12\x12\n\nclient_uri\x18\x01 \x01(\t\"\x84\x01\n\x12\x44isconnectResponse\x12*\n\x06status\x18\x01 \x01(\x0e\x32\x1a.DisconnectResponse.Status\x12%\n\texception\x18\x03 \x01(\x0b\x32\x12.ExceptionResponse\"\x1b\n\x06Status\x12\x06\n\x02OK\x10\x00\x12\t\n\x05\x45RROR\x10\x01\x32\xa5\x02\n\x13RemoteRouterService\x12;\n\x10\x63lient_heartbeat\x12\x11.HeartbeatRequest\x1a\x12.HeartbeatResponse\"\x00\x12\x32\n\x0bget_version\x12\x0f.VersionRequest\x1a\x10.VersionResponse\"\x00\x12.\n\x07\x63onnect\x12\x0f.ConnectRequest\x1a\x10.ConnectResponse\"\x00\x12\x34\n\treconnect\x12\x11.ReconnectRequest\x1a\x12.ReconnectResponse\"\x00\x12\x37\n\ndisconnect\x12\x12.DisconnectRequest\x1a\x13.DisconnectResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'remote_router_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _VERSIONREQUEST._serialized_start=46
  _VERSIONREQUEST._serialized_end=62
  _VERSIONRESPONSE._serialized_start=65
  _VERSIONRESPONSE._serialized_end=208
  _VERSIONRESPONSE_STATUS._serialized_start=181
  _VERSIONRESPONSE_STATUS._serialized_end=208
  _HEARTBEATREQUEST._serialized_start=210
  _HEARTBEATREQUEST._serialized_end=248
  _HEARTBEATRESPONSE._serialized_start=251
  _HEARTBEATRESPONSE._serialized_end=381
  _HEARTBEATRESPONSE_STATUS._serialized_start=181
  _HEARTBEATRESPONSE_STATUS._serialized_end=208
  _CONNECTREQUEST._serialized_start=383
  _CONNECTREQUEST._serialized_end=419
  _CONNECTRESPONSE._serialized_start=422
  _CONNECTRESPONSE._serialized_end=584
  _CONNECTRESPONSE_STATUS._serialized_start=181
  _CONNECTRESPONSE_STATUS._serialized_end=208
  _RECONNECTREQUEST._serialized_start=586
  _RECONNECTREQUEST._serialized_end=624
  _RECONNECTRESPONSE._serialized_start=627
  _RECONNECTRESPONSE._serialized_end=771
  _RECONNECTRESPONSE_STATUS._serialized_start=181
  _RECONNECTRESPONSE_STATUS._serialized_end=208
  _DISCONNECTREQUEST._serialized_start=773
  _DISCONNECTREQUEST._serialized_end=812
  _DISCONNECTRESPONSE._serialized_start=815
  _DISCONNECTRESPONSE._serialized_end=947
  _DISCONNECTRESPONSE_STATUS._serialized_start=181
  _DISCONNECTRESPONSE_STATUS._serialized_end=208
  _REMOTEROUTERSERVICE._serialized_start=950
  _REMOTEROUTERSERVICE._serialized_end=1243
# @@protoc_insertion_point(module_scope)
