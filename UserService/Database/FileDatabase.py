
from GRPC.user_pb2 import User, UserList
from Database.DatabaseInterface import UserDatabase

class UserFileDatabase(UserDatabase):
    def __init__(self):
        self.readFile()

    def readFile(self):
        self.database = {1:User(id=1, name='Alejandro', age=20, password='password', email='email')}
        self.id_count = 2
        pass

    def createUser(self, user) -> User:
        user.id = self.id_count
        self.database[user.id] =  user
        self.id_count += 1
        return self.database[user.id]

    def getUser(self, id) -> User:
        if not id in self.database:
            return User()
        return self.database[id]

    def getUserList(self) -> UserList:
        return UserList(users=self.database.values())

    def updateUser(self, user) -> User:
        id = user.id
        if not id in self.database:
            return User()
        self.database[id] = user
        return self.database[id]


    def deleteUser(self, id) -> User:
        if not id in self.database:
            return User()
        user = self.database[id]
        del self.database[id]
        return user