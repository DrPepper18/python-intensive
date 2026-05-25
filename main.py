from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/hello")
def hello():
    return {"text": "HELLOOOOOOO"}

uvicorn.run(app)