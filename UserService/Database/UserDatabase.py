
from GRPC.user_pb2 import User, UserList
from Database.DatabaseInterface import UserDatabase
import json
from google.protobuf.json_format import MessageToDict

class UserDatabase(UserDatabase):
    def __init__(self):
        self.readFile()

    def readFile(self):
        with open('./Database/users.txt') as f:
            self.database  = json.loads(f.read())
        lastId = 1
        for i in self.database.keys():
            user = self.database[i]
            lastId = user["id"]
            self.database[i] = User(
                id=user["id"], 
                name=user["name"], 
                age=user["age"], 
                password=user["password"], 
                email=user["email"]
            )
        self.id_count = lastId + 1

    def writeFile(self):
        with open('./Database/users.txt', 'wb') as convert_file:
            convert_file.write(bytes(json.dumps(self.database, default=MessageToDict), 'utf-8'))

    def createUser(self, user) -> User:
        
        user.id = self.id_count
        id = str(user.id)
        self.database[id] =  user
        self.writeFile()
        self.id_count += 1
        return self.database[id]

    def getUser(self, id) -> User:
        id = str(id)
        if not id in self.database:
            return User()
        return self.database[id]

    def getUserList(self) -> UserList:
        return UserList(users=self.database.values())

    def updateUser(self, user) -> User:
        id = str(user.id)
        if not id in self.database:
            return User()
        self.database[id] = user
        self.writeFile()
        return self.database[id]


    def deleteUser(self, id) -> User:
        id = str(id)
        if not id in self.database:
            return User()
        user = self.database[id]
        del self.database[id]
        self.writeFile()
        return user