import grpc
import kvs_pb2_grpc
import kvs_pb2
import logging

def get_value(stub, key):
    value = stub.Getrequest(key)
    print(value.value)

def set_value(stub, setRequestMessage):
    print(stub.Setrequest(setRequestMessage))
    

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    server = str(input("choose a server you want to access (50051 or 50053): "))
    server_name = str("localhost:" + server)
    print(server)
    print(server_name)
    with grpc.insecure_channel(server_name) as channel:
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
                propagated = False
                set_value(stub, kvs_pb2.SetRequestMessage(key=key, value=value, propagated=propagated))
            elif mode == "q":
                break


if __name__ == "__main__":
    logging.basicConfig()
    run()