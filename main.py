from typing import Union
from fastapi import FastAPI, Response, status

app = FastAPI()

@app.get("/lookup")
async def lookup(response: Response, vin: Union[str, None] = None):
    if not vin:
        response.status_code = status.HTTP_400_BAD_REQUEST

    return {"message": "Hello World"}

@app.delete("/remove")
async def remove():
    return {"vin": "Hello World", "success": True }

@app.get("/export")
async def export():
    return {"message": "Hello World"}