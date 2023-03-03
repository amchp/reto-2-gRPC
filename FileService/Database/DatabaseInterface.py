from abc import ABC, abstractmethod

from GRPC.file_pb2 import File



class FileDatabaseInterface(ABC):

    @abstractmethod
    def createFile(self, user) -> File:
        pass

    @abstractmethod
    def getFile(self, id) -> File:
        pass

    @abstractmethod
    def getFileList(self):
        pass

    @abstractmethod
    def updateFile(self, user) -> File:
        pass

    @abstractmethod
    def deleteFile(self, id) -> File:
        pass
