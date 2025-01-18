import grpc
import kvs_pb2_grpc
import kvs_pb2
import logging

def get_value(stub, key):
    value = stub.Getrequest(key)
    print(value.value)

def set_value(stub, keyvalue):
    print(stub.Setrequest(keyvalue))
    

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = kvs_pb2_grpc.KeyValueStoreStub(channel)
        while True:
            mode = input("choose mode (get, set, q): ")
            if mode == "get":        
                print("-------------- Get value --------------")        
                key = input("enter the key to get the value: ")
                get_value(stub, kvs_pb2.Key(key=key))
            elif mode == "set":
                print("-------------- Get value --------------")
                key = str(input("type key you want to add: "))
                value = int(input("type value you want to register: "))
                set_value(stub, kvs_pb2.KeyValue(key=key, value=value))
            elif mode == "q":
                break


if __name__ == "__main__":
    logging.basicConfig()
    run()