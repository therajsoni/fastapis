from pydantic import Field , BaseModel
class CreateUser(BaseModel):
    name: str 
    age: int 
    phone: str 
    email: str 
class UpdateUser(BaseModel):
    name: str | None
    age: int | None 
    phone: int | None 
    email: str | None 

