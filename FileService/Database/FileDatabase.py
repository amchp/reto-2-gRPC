
from GRPC.file_pb2 import File, FileList
from Database.DatabaseInterface import FileDatabaseInterface
import os
import json

class FileDatabase(FileDatabaseInterface):
    def __init__(self):
        self.user_id = {}
        self.read_user_ids()

    def read_user_ids(self):
        with open('./Database/user_ids.txt') as f:
            self.user_id  = json.loads(f.read())

    def write_user_ids(self):
        with open('./Database/user_ids.txt', 'w') as convert_file:
            convert_file.write(json.dumps(self.user_id))

    def update_user_id(self, name, user_id):
        self.user_id[name] = user_id
        self.write_user_ids()

    def createFile(self, file) -> File:
        if os.path.exists(f'./Database/files/{file.name}'):
            return File()
        with open(f'./Database/files/{file.name}', 'xb') as binary_file:
            binary_file.write(file.file)
        binary_file = open(f'./Database/files/{file.name}', 'rb')
        file_extension = binary_file.name.split('.')[1]
        self.update_user_id(file.name, file.user_id)
        
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
        self.update_user_id(file.name, file.user_id)
        
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
        user_id = self.user_id[name]
        del self.user_id[name]
        self.write_user_ids()
        os.remove(f'./Database/files/{name}')
        
        return File(
            user_id=user_id,
            name=name,
            file_format=file_extension,
            file=file
        ) 