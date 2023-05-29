from fastapi import FastAPI

app = FastAPI()

@app.get("/lookup")
async def lookup():
    return {"message": "Hello World"}

@app.delete("/remove")
async def remove():
    return {"message": "Hello World"}

@app.get("/export")
async def export():
    return {"message": "Hello World"}