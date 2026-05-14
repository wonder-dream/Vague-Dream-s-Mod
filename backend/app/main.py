from fastapi import FastAPI

fastapi = FastAPI()

@fastapi.get("/")
async def root():
    return {"message": "Hello World"}