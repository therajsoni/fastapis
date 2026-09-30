from api.routes.books import router as books_routes 
from api.routes.users import router as users_routes 
from fastapi import FastAPI 

app = FastAPI()
app.include_routes(users_routes)
app.include_router(books_routes)


