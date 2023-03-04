

import grpc

from GRPC.UserService.user_pb2_grpc import UserServiceStub
from GRPC.UserService.user_pb2 import NoUserMessage


class UserGRPC:
    def __init__(self) -> None:
        channel = grpc.insecure_channel('localhost:50051')
        self.stub = UserServiceStub(channel)

    def getUserList(self):
        return self.stub.GetUserList(NoUserMessage())