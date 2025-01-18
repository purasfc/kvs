import kvs_pb2
import kvs_pb2_grpc
import logging
from dictionary_data import d
import grpc
from concurrent import futures


class KeyValueStoreServicer (kvs_pb2_grpc.KeyValueStoreServicer):
    def Getrequest(self, key, context):
        for k in d:
            print(k)
            print(key.key)
            if k == key.key:
                print(key)
                return kvs_pb2.Value(value=d[k])
            # else:
            #     return kvs_pb2.Empty(empty="nothing")
        return kvs_pb2.Value()

    
    def Setrequest(self, request, context):
        d[request.key] = request.value
        print(d)
        return kvs_pb2.Empty(empty="you added new word!")
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    kvs_pb2_grpc.add_KeyValueStoreServicer_to_server(
        KeyValueStoreServicer(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()