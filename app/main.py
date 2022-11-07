from fastapi import FastAPI

app = FastAPI

@app.get("/")

def home():
    return {"hola": "Hola Mision TIC 2022"}

