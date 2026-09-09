from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/add")
async def add(a: float, b: float):
    return {"operation": "add", "a": a, "b": b, "result": a + b}

@app.get("/subtract")
async def subtract(a: float, b: float):
    return {"operation": "subtract", "a": a, "b": b, "result": a - b}

@app.get("/multiply")
async def multiply(a: float, b: float):
    return {"operation": "multiply", "a": a, "b": b, "result": a * b}

@app.get("/divide")
async def divide(a: float, b: float):
    if b == 0:
        return {"error": "Division by zero is not allowed"}
    return {"operation": "divide", "a": a, "b": b, "result": a / b}

if __name__ == "__main__":
    uvicorn.run("calculatorwithapi:app", host="127.0.0.1", port=8001, reload=True)
