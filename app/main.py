from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.routers import tables, reservations


app = FastAPI()

app.include_router(tables.router)
app.include_router(reservations.router)

@app.get("/")
async def root():
    link = "<a href='http://127.0.0.1:8000/docs#/' style='font-size: 50'>API endpoints</a>"
    return HTMLResponse(content=link)
