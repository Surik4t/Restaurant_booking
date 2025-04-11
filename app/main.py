from fastapi import FastAPI
from app.routers import tables


app = FastAPI()

app.include_router(tables.router)

@app.get("/home")
async def root():
    return {"message": "Restaurant booking API"}


print(app.routes)