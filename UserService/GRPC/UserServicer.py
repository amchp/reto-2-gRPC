from Database.UserDatabase import UserDatabase
from GRPC.user_pb2 import User, UserList
from .user_pb2_grpc import UserServiceServicer


class UserServicer(UserServiceServicer):
    def __init__(self) -> None:
        self.database = UserDatabase()
        super().__init__()

    def CreateUser(self, request, context) -> User:
        user = self.database.createUser(User(
            id=0,
            name=request.name,
            age=request.age,
            password=request.password,
            email=request.email
        ))
        return user
    
    def GetUser(self, request, context) -> User:
        user = self.database.getUser(request.id)
        return user
    
    def GetUserList(self, request, context) -> UserList:
        users = self.database.getUserList()
        return users
    
    def UpdateUser(self, request, context) -> User:
        user = self.database.updateUser(User(
            id=request.id,
            name=request.name,
            age=request.age,
            password=request.password,
            email=request.email
        ))
        return user
    
    def DeleteUser(self, request, context) -> User:
        user = self.database.deleteUser(request.id)
        return user