from GRPC.file_pb2 import File, Name
from Database.FileDatabase import FileDatabase

file = File(name='test.txt', user_id='1', file_format='txt', file=b'text')
fileDatabase = FileDatabase()
fileDatabase.getFileList()
