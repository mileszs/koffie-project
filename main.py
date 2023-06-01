from typing import Union
from fastapi import FastAPI, Response, status, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from sqlalchemy import select
import pandas as pd


from database import SessionLocal, engine
from models import Vehicle as VehicleModel, Base as BaseModel
from schemas import Vehicle as VehicleSchema
from to_parquet import save_to_parquet

BaseModel.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/lookup", response_model=VehicleSchema)
async def lookup(response: Response, vin: Union[str, None] = None, db: Session = Depends(get_db)):
    vehicle = VehicleModel.find(db, vin)
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")

    return vehicle

@app.delete("/remove")
async def remove(response: Response, vin: Union[str, None] = None, db: Session = Depends(get_db)):
    success = False
    vehicle = db.query(VehicleModel).filter(VehicleModel.vin == vin).first()
    if vehicle:
        db.delete(vehicle)
        db.commit()
        success = True

    return { "vin": vehicle.vin, "success": success }

@app.get("/export")
async def export(response: Response, db: Session = Depends(get_db)):
    path = save_to_parquet(db, VehicleModel)
    
    return FileResponse(path, filename="vehicles.parquet") 