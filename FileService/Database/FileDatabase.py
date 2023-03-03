
from GRPC.file_pb2 import File, FileList
from Database.DatabaseInterface import FileDatabaseInterface
import os

class FileDatabase(FileDatabaseInterface):
    def __init__(self):
        self.user_id = {}
        self.inverse_user_id = {}

    def createFile(self, file) -> File:
        try:
            with open(f'./Database/files/{file.name}', 'xb') as binary_file:
                binary_file.write(file.file)
        except:
            return File()
        binary_file = open(f'./Database/files/{file.name}', 'rb')
        file_extension = binary_file.name.split('.')[1]
        self.user_id[file.name] = file.user_id
        if file.name in self.inverse_user_id:
            self.inverse_user_id[file.name].append(file.name)
        else:
            self.inverse_user_id[file.name] = [file.name]
        
        return File(
            user_id=file.user_id,
            name=file.name,
            file_format=file_extension,
            file=b''.join(binary_file.readlines())
        ) 

    def getFile(self, name) -> File:
        if not os.path.exists(f'./Database/files/{name}'):
            return File()
        binary_file = open(f'./Database/files/{name}', 'rb')
        file_extension = binary_file.name.split('.')[1]
        
        return File(
            user_id=self.user_id[name],
            name=name,
            file_format=file_extension,
            file=b''.join(binary_file.readlines())
        )    

    def getFileList(self) -> FileList:
        files = []
        file_names = os.listdir('./Database/files')
        for file in file_names:
            binary_file = open(f'./Database/files/{file}', 'rb')
            file_name = file
            file_extension = file_name.split('.')[1]
            files.append(File(
                user_id=self.user_id[file_name],
                name=file_name,
                file_format=file_extension,
                file=b''.join(binary_file.readlines())
            ))
        return FileList(files=files)

    def updateFile(self, file) -> File:
        if not os.path.exists(f'./Database/files/{file.name}'):
            return File()

        with open(f'./Database/files/{file.name}', 'wb') as binary_file:
            binary_file.write(file.file)
        binary_file = open(f'./Database/files/{file.name}', 'rb')
        file_extension = binary_file.name.split('.')[1]
        
        return File(
            user_id=self.user_id[file.name],
            name=file.name,
            file_format=file_extension,
            file=b''.join(binary_file.readlines())
        ) 


    def deleteFile(self, name) -> File:
        if not os.path.exists(f'./Database/files/{name}'):
            return File()

        binary_file = open(f'./Database/files/{name}', 'rb')
        file_extension = binary_file.name.split('.')[1]
        file = b''.join(binary_file.readlines())
        os.remove(f'./Database/files/{name}')
        
        return File(
            user_id=self.user_id[name],
            name=name,
            file_format=file_extension,
            file=file
        ) 