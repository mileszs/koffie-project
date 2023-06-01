import pandas as pd
from models import Vehicle as VehicleModel

def save_to_parquet(db, model=VehicleModel):
    path = "/tmp/vehicles.parquet"
    vehicles_query = db.query(VehicleModel).all()
    df = pd.read_sql("SELECT * FROM vehicles", db.bind)
    df.to_parquet(path)

    return path