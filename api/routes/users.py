from api.services.users import getAll , getOne , createUser , updateuser , deleteUser
from api.models.users import CreateUser , UpdateUser
from fastapi import APIRouter 
router = APIRouter(prefix="/users")

@router.get("/")
def GetAll():
   return getAll()

@router.get("/{id}")
def GetOne(id: str):
    return getOne(id)

@router.patch("/{id}")
def PatchUser(id: str, data: UpdateUser):
    return updateuser(id , data)

@router.delete("/{id}")
def DeleteUser(id: str):
    return deleteUser(id)

@router.post("/create")
def InsertUser(data: CreateUser):
    return createUser(data)

    