from GRPC.SearchService.search_pb2 import UserName
from GRPC.FileService.FileService import FileGRPC



userGRPC = FileGRPC()
print(userGRPC.getFileList())

