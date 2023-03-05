import grpc
import json
from concurrent import futures
from GRPC.UserServicer import UserServicer
from GRPC.user_pb2_grpc import add_UserServiceServicer_to_server


def serve():
    with open("./config.json") as file:
        config = json.load(file)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_UserServiceServicer_to_server(
        UserServicer(), server)
    
    server.add_insecure_port(f'{config["IP"]}:{config["PORT"]}')
    print("Starting Server", config["IP"], config["PORT"])
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
