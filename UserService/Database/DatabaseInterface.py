from abc import ABC, abstractmethod

from GRPC.user_pb2 import User



class Database(ABC):

    @abstractmethod
    def createUser(self, request) -> User:
        pass

    @abstractmethod
    def getUser(self, request) -> User:
        pass

    @abstractmethod
    def getUserList(self, request):
        pass

    @abstractmethod
    def updateUser(self, request) -> User:
        pass

    @abstractmethod
    def deleteUser(self, request) -> User:
        pass
