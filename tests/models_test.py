from models import Base, Vehicle
from database import engine, SessionLocal

class TestVehicle:
    def setup_class(self):
        Base.metadata.create_all(engine)
        self.session = SessionLocal()
        self.valid_vehicle = Vehicle(
            make="Nissan",
            model="Frontier",
            year="2017",
            body_class="pickup_truck"
        )

    def teardown_class(self):
        self.session.rollback()
        self.session.close()

    def test_vehicle_valid(self):   
        self.session.add(self.valid_vehicle)
        self.session.commit()
        frontier = self.session.query(Vehicle).filter_by(model="Frontier").first()
        assert frontier.make == "Nissan"
        assert frontier.model != "Titan"
        assert frontier.year == "2017"
        assert frontier.body_class == "pickup_truck"