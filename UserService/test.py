from GRPC.user_pb2 import User
from Database.UserDatabase import UserDatabase

user = User(name='Alejandro', age=20, password='password', email='email')
userDatabase = UserDatabase()
userDatabase.createUser(user)