from api.models.users import CreateUser , UpdateUser
from api.database.config import users
from api.utils.responses import ResponseSuccess , ResponseFailure
from bson import ObjectId

async def createUser(data: CreateUser): 
   user = {
    "name": data.name,
    "age": data.age,
    "phone": data.phone,
    "email": data.email 
   }
   result = users.insert_one(user)
   return ResponseSuccess(201 , "User Created" , result)

async def updateUser(id : str , data: UpdateBook):
   userOne = users.find_one({
    "_id" : ObjectId(id)
   }) 
   if not userOne:
     return ResponseFailure(404 , "User not found")
   user = {
    "name": data.name or userOne.name,
    "age": data.age or userOne.age,
    "phone": data.phone or userOne.phone,
    "email": data.email or userOne.email 
   }
   result = users.update_one({
    "_id" : ObjectId(id)
   } , {
    "$set" : user
   })
   return ResponseSuccess(201 , "User Updated" , result)

async def getAll():
    users = users.find({})
    return ResponseSuccess(200 , "Get All Users" , books)

async def getOne(id : str):
    user = users.find_one({
        "_id" : ObjectId(id)
    })   
    if not user:
        return ResponseFailure(404 , "Not Found")
    return ResponseSuccess(200 , "Get User" , book)

async def deleteUser(id: str):
    user = users.find_one({
        "_id" : ObjectId(id)
    })
    if not user:
        return ResponseFailure(404 , "User not found")
    users.delete_one({
        "_id" : ObjectId(id)
    })     
    return ResponseSuccess(200 , "User Deleted" , book)
