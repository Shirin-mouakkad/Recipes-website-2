from fastapi import FastAPI
from Router import user, chef
from typing import Optional
from DB import Models, Database
from DB.Database import engine, Base


app = FastAPI()
app.include_router(user.router)
app.include_router(chef.router)

@app.get('/hello')
def index():
  return {'message': 'Hello world!'}

Models.Base.metadata.create_all(engine)
