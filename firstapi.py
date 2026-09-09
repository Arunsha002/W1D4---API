from fastapi import FastAPI   # lowercase 'fastapi', not 'firstapi'
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run("firstapi:app", host="127.0.0.1", port=8000, reload=True)
