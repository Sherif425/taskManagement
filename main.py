from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello WOrld"}

@app.get("/message")
async def root():
    return {"message":"Fast Api how to mkae APIs"}
