import grpc
import json
from GRPC.UserService.user_pb2_grpc import UserServiceStub
from GRPC.UserService.user_pb2 import NoUserMessage


class UserGRPC:
    def __init__(self) -> None:
        with open("./config.json") as file:
            config = json.load(file)
        channel = grpc.insecure_channel(f'{config["IP_USER_SERVICE"]}:{config["PORT_USER_SERVICE"]}')
        self.stub = UserServiceStub(channel)

    def getUserList(self):
        return self.stub.GetUserList(NoUserMessage())