import grpc
from concurrent import futures
from GRPC.SearchService.SerchServicer import SearcherServicer
from GRPC.SearchService.search_pb2_grpc import add_SearcherServiceServicer_to_server


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_SearcherServiceServicer_to_server(
        SearcherServicer(), server)
    server.add_insecure_port('[::]:50053')
    print("Starting Server")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
