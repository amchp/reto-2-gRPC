import grpc
import json
from GRPC.FileService.file_pb2_grpc import FileServiceStub
from GRPC.FileService.file_pb2 import NoFileMessage




class FileGRPC:
    def __init__(self) -> None:
        with open("./config.json") as file:
            config = json.load(file)
        channel = grpc.insecure_channel(f'{config["IP_FILE_SERVICE"]}:{config["PORT_FILE_SERVICE"]}')
        self.stub = FileServiceStub(channel)

    def getFileList(self):
        return self.stub.GetFileList(NoFileMessage())