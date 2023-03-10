# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: remote_tracking.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15remote_tracking.proto\"J\n\x11\x45xceptionResponse\x12\x13\n\x0bmodule_name\x18\x01 \x01(\t\x12\x12\n\nclass_name\x18\x02 \x01(\t\x12\x0c\n\x04\x61rgs\x18\x03 \x01(\t\"2\n\x1c\x43lientResourceCleanupRequest\x12\x12\n\nclient_uri\x18\x01 \x01(\t\"\x9a\x01\n\x1d\x43lientResourceCleanupResponse\x12\x35\n\x06status\x18\x01 \x01(\x0e\x32%.ClientResourceCleanupResponse.Status\x12%\n\texception\x18\x02 \x01(\x0b\x32\x12.ExceptionResponse\"\x1b\n\x06Status\x12\x06\n\x02OK\x10\x00\x12\t\n\x05\x45RROR\x10\x01\"[\n\x0fResourceRequest\x12\x15\n\rresource_type\x18\x01 \x01(\t\x12\x0f\n\x07handler\x18\x02 \x01(\t\x12\x12\n\nclient_uri\x18\x03 \x01(\t\x12\x0c\n\x04\x61rgs\x18\x04 \x01(\x0c\"\x91\x01\n\x10ResourceResponse\x12\x0f\n\x07handler\x18\x01 \x01(\t\x12(\n\x06status\x18\x02 \x01(\x0e\x32\x18.ResourceResponse.Status\x12%\n\texception\x18\x03 \x01(\x0b\x32\x12.ExceptionResponse\"\x1b\n\x06Status\x12\x06\n\x02OK\x10\x00\x12\t\n\x05\x45RROR\x10\x01\"=\n\x16ReleaseResourceRequest\x12\x0f\n\x07handler\x18\x01 \x01(\t\x12\x12\n\nclient_uri\x18\x02 \x01(\t\"\x8e\x01\n\x17ReleaseResourceResponse\x12/\n\x06status\x18\x02 \x01(\x0e\x32\x1f.ReleaseResourceResponse.Status\x12%\n\texception\x18\x03 \x01(\x0b\x32\x12.ExceptionResponse\"\x1b\n\x06Status\x12\x06\n\x02OK\x10\x00\x12\t\n\x05\x45RROR\x10\x01\"Z\n\rRequestHeader\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x0f\n\x07handler\x18\x02 \x01(\t\x12\x12\n\nclient_uri\x18\x03 \x01(\t\x12\x13\n\x0bmethod_name\x18\x04 \x01(\t\"X\n\x12InstructionRequest\x12 \n\x06header\x18\x01 \x01(\x0b\x32\x0e.RequestHeaderH\x00\x12\x11\n\x07message\x18\x02 \x01(\x0cH\x00\x42\r\n\x0binstruction\"\x8d\x01\n\x0eResponseHeader\x12\x0f\n\x07version\x18\x01 \x01(\t\x12&\n\x06status\x18\x02 \x01(\x0e\x32\x16.ResponseHeader.Status\x12%\n\texception\x18\x03 \x01(\x0b\x32\x12.ExceptionResponse\"\x1b\n\x06Status\x12\x06\n\x02OK\x10\x00\x12\t\n\x05\x45RROR\x10\x01\"Z\n\x13InstructionResponse\x12!\n\x06header\x18\x01 \x01(\x0b\x32\x0f.ResponseHeaderH\x00\x12\x11\n\x07message\x18\x02 \x01(\x0cH\x00\x42\r\n\x0binstruction\"P\n\x18WriteInstructionsRequest\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x12\n\nclient_uri\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\x0c\"\xa3\x01\n\x19WriteInstructionsResponse\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x31\n\x06status\x18\x02 \x01(\x0e\x32!.WriteInstructionsResponse.Status\x12%\n\texception\x18\x03 \x01(\x0b\x32\x12.ExceptionResponse\"\x1b\n\x06Status\x12\x06\n\x02OK\x10\x00\x12\t\n\x05\x45RROR\x10\x01\x32\x8d\x03\n\x15RemoteTrackingService\x12[\n\x18\x63leanup_client_resources\x12\x1d.ClientResourceCleanupRequest\x1a\x1e.ClientResourceCleanupResponse\"\x00\x12\x35\n\x0cget_resource\x12\x10.ResourceRequest\x1a\x11.ResourceResponse\"\x00\x12G\n\x10release_resource\x12\x17.ReleaseResourceRequest\x1a\x18.ReleaseResourceResponse\"\x00\x12\x42\n\x0frun_instruction\x12\x13.InstructionRequest\x1a\x14.InstructionResponse\"\x00(\x01\x30\x01\x12S\n\x16run_write_instructions\x12\x19.WriteInstructionsRequest\x1a\x1a.WriteInstructionsResponse\"\x00(\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'remote_tracking_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EXCEPTIONRESPONSE._serialized_start=25
  _EXCEPTIONRESPONSE._serialized_end=99
  _CLIENTRESOURCECLEANUPREQUEST._serialized_start=101
  _CLIENTRESOURCECLEANUPREQUEST._serialized_end=151
  _CLIENTRESOURCECLEANUPRESPONSE._serialized_start=154
  _CLIENTRESOURCECLEANUPRESPONSE._serialized_end=308
  _CLIENTRESOURCECLEANUPRESPONSE_STATUS._serialized_start=281
  _CLIENTRESOURCECLEANUPRESPONSE_STATUS._serialized_end=308
  _RESOURCEREQUEST._serialized_start=310
  _RESOURCEREQUEST._serialized_end=401
  _RESOURCERESPONSE._serialized_start=404
  _RESOURCERESPONSE._serialized_end=549
  _RESOURCERESPONSE_STATUS._serialized_start=281
  _RESOURCERESPONSE_STATUS._serialized_end=308
  _RELEASERESOURCEREQUEST._serialized_start=551
  _RELEASERESOURCEREQUEST._serialized_end=612
  _RELEASERESOURCERESPONSE._serialized_start=615
  _RELEASERESOURCERESPONSE._serialized_end=757
  _RELEASERESOURCERESPONSE_STATUS._serialized_start=281
  _RELEASERESOURCERESPONSE_STATUS._serialized_end=308
  _REQUESTHEADER._serialized_start=759
  _REQUESTHEADER._serialized_end=849
  _INSTRUCTIONREQUEST._serialized_start=851
  _INSTRUCTIONREQUEST._serialized_end=939
  _RESPONSEHEADER._serialized_start=942
  _RESPONSEHEADER._serialized_end=1083
  _RESPONSEHEADER_STATUS._serialized_start=281
  _RESPONSEHEADER_STATUS._serialized_end=308
  _INSTRUCTIONRESPONSE._serialized_start=1085
  _INSTRUCTIONRESPONSE._serialized_end=1175
  _WRITEINSTRUCTIONSREQUEST._serialized_start=1177
  _WRITEINSTRUCTIONSREQUEST._serialized_end=1257
  _WRITEINSTRUCTIONSRESPONSE._serialized_start=1260
  _WRITEINSTRUCTIONSRESPONSE._serialized_end=1423
  _WRITEINSTRUCTIONSRESPONSE_STATUS._serialized_start=281
  _WRITEINSTRUCTIONSRESPONSE_STATUS._serialized_end=308
  _REMOTETRACKINGSERVICE._serialized_start=1426
  _REMOTETRACKINGSERVICE._serialized_end=1823
# @@protoc_insertion_point(module_scope)
