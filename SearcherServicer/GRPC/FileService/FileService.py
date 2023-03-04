

import grpc

from GRPC.FileService.file_pb2_grpc import FileServiceStub
from GRPC.FileService.file_pb2 import NoFileMessage




class FileGRPC:
    def __init__(self) -> None:
        channel = grpc.insecure_channel('localhost:50052')
        self.stub = FileServiceStub(channel)

    def getFileList(self):
        return self.stub.GetFileList(NoFileMessage())