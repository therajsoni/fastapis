from api.services.books import getAll , getOne , createBook , updateBook , deleteBook
from api.models.books import CreateBook , UpdateBook
from fastapi import APIRouter 
router = APIRouter(prefix="/books")

@router.get("/")
def GetAll():
   return getAll()

@router.get("/{id}")
def GetOne(id:str):
    return getOne(id)

@router.patch("/{id}")
def PatchBook(id:str, data: UpdateBook):
    return updateBook(id , data)

@router.delete("/{id}")
def DeleteBook(id:str):
    return deleteBook(id)

@router.post("/create")
def InsertBook(data:CreateBook):
    return createBook(data)

    