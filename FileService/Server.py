import grpc
import json
from concurrent import futures
from GRPC.FileServicer import FileServicer
from GRPC.file_pb2_grpc import add_FileServiceServicer_to_server


def serve(): 
    with open("./config.json") as file:
        config = json.load(file)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_FileServiceServicer_to_server(
        FileServicer(), server)
    
    server.add_insecure_port(f'{config["IP"]}:{config["PORT"]}')
    print("Starting Server", config["IP"], config["PORT"])
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
