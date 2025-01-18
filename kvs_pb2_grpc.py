# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import kvs_pb2 as kvs__pb2

GRPC_GENERATED_VERSION = '1.69.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in kvs_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class KeyValueStoreStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Getrequest = channel.unary_unary(
                '/KeyValueStore/Getrequest',
                request_serializer=kvs__pb2.Key.SerializeToString,
                response_deserializer=kvs__pb2.Value.FromString,
                _registered_method=True)
        self.Setrequest = channel.unary_unary(
                '/KeyValueStore/Setrequest',
                request_serializer=kvs__pb2.KeyValue.SerializeToString,
                response_deserializer=kvs__pb2.Empty.FromString,
                _registered_method=True)


class KeyValueStoreServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Getrequest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Setrequest(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_KeyValueStoreServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Getrequest': grpc.unary_unary_rpc_method_handler(
                    servicer.Getrequest,
                    request_deserializer=kvs__pb2.Key.FromString,
                    response_serializer=kvs__pb2.Value.SerializeToString,
            ),
            'Setrequest': grpc.unary_unary_rpc_method_handler(
                    servicer.Setrequest,
                    request_deserializer=kvs__pb2.KeyValue.FromString,
                    response_serializer=kvs__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'KeyValueStore', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('KeyValueStore', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class KeyValueStore(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Getrequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/KeyValueStore/Getrequest',
            kvs__pb2.Key.SerializeToString,
            kvs__pb2.Value.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Setrequest(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/KeyValueStore/Setrequest',
            kvs__pb2.KeyValue.SerializeToString,
            kvs__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
