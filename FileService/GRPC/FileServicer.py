from Database.FileDatabase import FileDatabase
from .file_pb2 import File
from .file_pb2_grpc import FileServiceServicer

class FileServicer(FileServiceServicer):

    def __init__(self) -> None:
        self.database = FileDatabase()

    def CreateFile(self, request, context):
        file = self.database.createFile(File(
            user_id=request.user_id,
            name=request.name,
            file_format=request.file_format,
            file=request.file,
        ))
        return file

    def GetFileList(self, request, context):
        files = self.database.getFileList()
        return files 
    
    def GetFile(self, request, context):
        file = self.database.getFile(request.name)
        return file

    def UpdateFile(self, request, context):
        file = self.database.updateFile(File(
            user_id=request.user_id,
            name=request.name,
            file_format=request.file_format,
            file=request.file,
        ))
        return file
    
    def DeleteFile(self, request, context):
        file = self.database.deleteFile(request.name)
        return file