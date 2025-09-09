from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}



@app.get("/meow")
async def say_meow():
    return {"message": "Meow!"}