from api.models.books import CreateBook , UpdateBook
from api.database.config import books
from api.utils.response import ResponseSuccess , ResponseFailure
from bson import ObjectId

async def createBook(data: CreateBook):
   book = {
    "name": data.name,
    "description": data.description,
    "author": data.author,
    "prize": data.prize, 
    "quantity": data.quantity 
   }
   result = books.insert_one(book)
   return ResponseSuccess(201 , "Book Created" , result)

async def updateBook(id : str , data: UpdateBook):
   bookOne = books.find_one({
    "_id" : ObjectId(id)
   }) 
   if not bookOne:
     return ResponseFailure(404 , "Book not found")
   book = {
    "name": data.name or bookOne.name,
    "description": data.description or bookOne.description,
    "author": data.author or bookOne.author,
    "prize": data.prize or bookOne.prize, 
    "quantity": data.quantity or bookOne.quantity 
   }
   result = books.update_one({
    "_id" : ObjectId(id)
   } , {
    "$set" : book
   })
   return ResponseSuccess(201 , "Book Updated" , result)

async def getAll():
    books = books.find({})
    return ResponseSuccess(200 , "Get All Books" , books)

async def getOne(id : str):
    book = books.find_one({
        "_id" : ObjectId(id)
    })   
    if not book:
        return ResponseFailure(404 , "Not Found")
    return ResponseSuccess(200 , "Get Book" , book)

async def deleteBook(id: str):
    book = books.find_one({
        "_id" : ObjectId(id)
    })
    if not book:
        return ResponseFailure(404 , "Book not found")
    books.delete_one({
        "_id" : ObjectId(id)
    })     
    return ResponseSuccess(200 , "Book Deleted" , book)
