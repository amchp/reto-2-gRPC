from abc import ABC, abstractmethod

from GRPC.user_pb2 import User



class UserDatabase(ABC):

    @abstractmethod
    def createUser(self, user) -> User:
        pass

    @abstractmethod
    def getUser(self, id) -> User:
        pass

    @abstractmethod
    def getUserList(self):
        pass

    @abstractmethod
    def updateUser(self, user) -> User:
        pass

    @abstractmethod
    def deleteUser(self, id) -> User:
        pass
