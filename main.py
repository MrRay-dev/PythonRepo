from fastapi import FastAPI
from pydantic import BaseModel

# Initialize FastAPI
app = FastAPI()

# Hardcoded GET API
@app.get("/info")
def get_info():
    return {"message": "Welcome to FastAPI Sample Project!"}

# Define a request model for POST API
class DataModel(BaseModel):
    name: str
    age: int

# Hardcoded POST API
@app.post("/data")
def post_data(data: DataModel):
    return {"response": f"Hello {data.name}, you are {data.age} years old!"}
