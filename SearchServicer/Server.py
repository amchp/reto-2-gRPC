import grpc
import json
from concurrent import futures
from GRPC.SearchService.SerchServicer import SearcherServicer
from GRPC.SearchService.search_pb2_grpc import add_SearcherServiceServicer_to_server


def serve():
    with open("./config.json") as file:
        config = json.load(file)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_SearcherServiceServicer_to_server(
        SearcherServicer(), server)
    
    server.add_insecure_port(f'{config["SEARCH_SERVICE_IP"]}:{config["SEARCH_SERVICE_PORT"]}')
    print("Starting Server", config["SEARCH_SERVICE_IP"], config["SEARCH_SERVICE_PORT"])
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
