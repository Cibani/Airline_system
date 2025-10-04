from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flight_no = db.Column(db.String(20), nullable=False)
    origin = db.Column(db.String(100), nullable=False)
    destination = db.Column(db.String(100), nullable=False)
    departure = db.Column(db.String(50), nullable=False)
    arrival = db.Column(db.String(50), nullable=False)
    seats_total = db.Column(db.Integer, nullable=False)
    seats_available = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flight_id = db.Column(db.Integer, db.ForeignKey("flight.id"), nullable=False)
    passenger_name = db.Column(db.String(200), nullable=False)
    passenger_email = db.Column(db.String(200), nullable=False)
    seats_booked = db.Column(db.Integer, nullable=False)
    booked_at = db.Column(db.DateTime, default=datetime.utcnow)

    flight = db.relationship("Flight", backref="bookings")

    def as_dict(self):
        data = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        data["flight_no"] = self.flight.flight_no
        return data
