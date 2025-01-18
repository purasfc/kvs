import kvs_pb2
import kvs_pb2_grpc
import logging
from dictionary_data_2 import d
import grpc
from concurrent import futures

# 自分以外のサーバーの名前
server_names = ["localhost:50051"]

class KeyValueStoreServicer (kvs_pb2_grpc.KeyValueStoreServicer):
    
    def Getrequest(self, key, context):
        for k in d:
            print(k)
            print(key.key)
            if k == key.key:
                print(key)
                return kvs_pb2.Value(value=d[k])

        return kvs_pb2.Value()

    
    def Setrequest(self, setRequestMessage, context):
        if not setRequestMessage.propagated:
            with grpc.insecure_channel("localhost:50051") as channel:
                stub = kvs_pb2_grpc.KeyValueStoreStub(channel)
                print("hi there")
                setRequestMessage.propagated = True
                stub.Setrequest(setRequestMessage)
            
        d[setRequestMessage.key] = setRequestMessage.value
        print(d)
        return kvs_pb2.Empty(empty="you added new word!")
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    kvs_pb2_grpc.add_KeyValueStoreServicer_to_server(
        KeyValueStoreServicer(), server
    )
    server.add_insecure_port("[::]:50053")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()