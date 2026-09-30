from pydantic import BaseModel , Field
class CreateBook(BaseModel):
    name: str 
    description: str 
    author: str 
    prize: str 
    quantity: int 
class UpdateBook(BaseModel):
    name: str | None
    description: str | None 
    author: str | None
    prize: str | None
    quantity: int | None
