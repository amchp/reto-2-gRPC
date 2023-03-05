from GRPC.FileService.file_pb2 import File, FileList
from GRPC.SearchService.search_pb2_grpc import SearcherService
from GRPC.UserService.UserGRPC import UserGRPC
from GRPC.FileService.FileService import FileGRPC
from GRPC.UserService.user_pb2 import User, UserList
from google.protobuf.json_format import MessageToDict


class SearcherServicer(SearcherService):
    def __init__(self) -> None:
        self.userService = UserGRPC()
        self.fileService = FileGRPC()

    def getFileListByUserId(self, request, context):
        files = MessageToDict(self.fileService.getFileList())
        response = []
        for file in files['files']:
            if file['userId'] == request.user:
                response.append(File(
                    name=file['name'],
                    user_id=file['userId'],
                    file_format=file['fileFormat'],
                    file=bytes(file['file'], 'utf-8')
                ))
        return FileList(files=response)

    def getUsersByName(self, request, context):
        users = MessageToDict(self.userService.getUserList())
        response = []
        for user in users['users']:
            if user['name'] == request.name:
                response.append(User(
                    id=user['id'],
                    name=user['name'],
                    age=user['age'],
                    password=user['password'],
                    email=user['email']
                ))
        return UserList(users=response)