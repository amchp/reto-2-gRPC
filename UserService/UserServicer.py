from UserService.user_pb2_grpc import UserServiceServicer


class UserServicer(UserServiceServicer):
    def CreateUser(self, request, context):
        return super().CreateUser(request, context)
    
    def GetUser(self, request, context):
        return super().GetUser(request, context)
    
    def GetUserList(self, request, context):
        return super().GetUserList(request, context)
    
    def UpdateUser(self, request, context):
        return super().UpdateUser(request, context)
    
    def DeleteUser(self, request, context):
        return super().DeleteUser(request, context)