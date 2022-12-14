# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: format.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='format.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('Z\002/.'),
  serialized_pb=_b('\n\x0c\x66ormat.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"9\n\x0bMapTCPstate\x12\x1b\n\x04type\x18\x01 \x01(\x0e\x32\r.TCPstateType\x12\r\n\x05\x63ount\x18\x02 \x01(\r\"\x89\x02\n\x0fHistogramFamily\x12\x12\n\nmashine_id\x18\x01 \x01(\r\x12\x0f\n\x07pck_len\x18\x02 \x03(\r\x12\x0e\n\x06L3_DST\x18\x03 \x03(\r\x12\x0e\n\x06L4_DST\x18\x04 \x03(\r\x12\x0e\n\x06L3_SRC\x18\x05 \x03(\r\x12\x0e\n\x06L4_SRC\x18\x06 \x03(\r\x12\x14\n\x0cL3_PROTOCOLS\x18\x07 \x03(\r\x12 \n\nTCP_STATES\x18\t \x03(\x0b\x32\x0c.MapTCPstate\x12.\n\nprobe_time\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x02v4\x18\x0b \x01(\x07H\x00\x12\x0c\n\x02v6\x18\x0c \x01(\x0cH\x00\x42\r\n\x0b\x64st_ip_addr*\xb1\x01\n\x0cTCPstateType\x12\n\n\x06\x43LOSED\x10\x00\x12\n\n\x06LISTEN\x10\x01\x12\x0c\n\x08SYN_SENT\x10\x02\x12\x10\n\x0cSYN_RECEIVED\x10\x03\x12\x0f\n\x0b\x45STABLISHED\x10\x04\x12\x0e\n\nFIN_WAIT_1\x10\x05\x12\x0e\n\nCLOSE_WAIT\x10\x06\x12\x0e\n\nFIN_WAIT_2\x10\x07\x12\x0c\n\x08LAST_ACK\x10\x08\x12\r\n\tTIME_WAIT\x10\t\x12\x0b\n\x07\x43LOSING\x10\nB\x04Z\x02/.b\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])

_TCPSTATETYPE = _descriptor.EnumDescriptor(
  name='TCPstateType',
  full_name='TCPstateType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CLOSED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LISTEN', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYN_SENT', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SYN_RECEIVED', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ESTABLISHED', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIN_WAIT_1', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLOSE_WAIT', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FIN_WAIT_2', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LAST_ACK', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIME_WAIT', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLOSING', index=10, number=10,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=377,
  serialized_end=554,
)
_sym_db.RegisterEnumDescriptor(_TCPSTATETYPE)

TCPstateType = enum_type_wrapper.EnumTypeWrapper(_TCPSTATETYPE)
CLOSED = 0
LISTEN = 1
SYN_SENT = 2
SYN_RECEIVED = 3
ESTABLISHED = 4
FIN_WAIT_1 = 5
CLOSE_WAIT = 6
FIN_WAIT_2 = 7
LAST_ACK = 8
TIME_WAIT = 9
CLOSING = 10



_MAPTCPSTATE = _descriptor.Descriptor(
  name='MapTCPstate',
  full_name='MapTCPstate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='MapTCPstate.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='count', full_name='MapTCPstate.count', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=49,
  serialized_end=106,
)


_HISTOGRAMFAMILY = _descriptor.Descriptor(
  name='HistogramFamily',
  full_name='HistogramFamily',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mashine_id', full_name='HistogramFamily.mashine_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pck_len', full_name='HistogramFamily.pck_len', index=1,
      number=2, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='L3_DST', full_name='HistogramFamily.L3_DST', index=2,
      number=3, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='L4_DST', full_name='HistogramFamily.L4_DST', index=3,
      number=4, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='L3_SRC', full_name='HistogramFamily.L3_SRC', index=4,
      number=5, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='L4_SRC', full_name='HistogramFamily.L4_SRC', index=5,
      number=6, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='L3_PROTOCOLS', full_name='HistogramFamily.L3_PROTOCOLS', index=6,
      number=7, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='TCP_STATES', full_name='HistogramFamily.TCP_STATES', index=7,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='probe_time', full_name='HistogramFamily.probe_time', index=8,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='v4', full_name='HistogramFamily.v4', index=9,
      number=11, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='v6', full_name='HistogramFamily.v6', index=10,
      number=12, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='dst_ip_addr', full_name='HistogramFamily.dst_ip_addr',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=109,
  serialized_end=374,
)

_MAPTCPSTATE.fields_by_name['type'].enum_type = _TCPSTATETYPE
_HISTOGRAMFAMILY.fields_by_name['TCP_STATES'].message_type = _MAPTCPSTATE
_HISTOGRAMFAMILY.fields_by_name['probe_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_HISTOGRAMFAMILY.oneofs_by_name['dst_ip_addr'].fields.append(
  _HISTOGRAMFAMILY.fields_by_name['v4'])
_HISTOGRAMFAMILY.fields_by_name['v4'].containing_oneof = _HISTOGRAMFAMILY.oneofs_by_name['dst_ip_addr']
_HISTOGRAMFAMILY.oneofs_by_name['dst_ip_addr'].fields.append(
  _HISTOGRAMFAMILY.fields_by_name['v6'])
_HISTOGRAMFAMILY.fields_by_name['v6'].containing_oneof = _HISTOGRAMFAMILY.oneofs_by_name['dst_ip_addr']
DESCRIPTOR.message_types_by_name['MapTCPstate'] = _MAPTCPSTATE
DESCRIPTOR.message_types_by_name['HistogramFamily'] = _HISTOGRAMFAMILY
DESCRIPTOR.enum_types_by_name['TCPstateType'] = _TCPSTATETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MapTCPstate = _reflection.GeneratedProtocolMessageType('MapTCPstate', (_message.Message,), dict(
  DESCRIPTOR = _MAPTCPSTATE,
  __module__ = 'format_pb2'
  # @@protoc_insertion_point(class_scope:MapTCPstate)
  ))
_sym_db.RegisterMessage(MapTCPstate)

HistogramFamily = _reflection.GeneratedProtocolMessageType('HistogramFamily', (_message.Message,), dict(
  DESCRIPTOR = _HISTOGRAMFAMILY,
  __module__ = 'format_pb2'
  # @@protoc_insertion_point(class_scope:HistogramFamily)
  ))
_sym_db.RegisterMessage(HistogramFamily)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
