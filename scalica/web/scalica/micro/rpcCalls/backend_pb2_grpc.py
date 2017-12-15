# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import backend_pb2 as backend__pb2


class GenerateFollowersStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.gen_rec = channel.unary_unary(
        '/GenerateFollowers/gen_rec',
        request_serializer=backend__pb2.RecRequest.SerializeToString,
        response_deserializer=backend__pb2.Void.FromString,
        )


class GenerateFollowersServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def gen_rec(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_GenerateFollowersServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'gen_rec': grpc.unary_unary_rpc_method_handler(
          servicer.gen_rec,
          request_deserializer=backend__pb2.RecRequest.FromString,
          response_serializer=backend__pb2.Void.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'GenerateFollowers', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))