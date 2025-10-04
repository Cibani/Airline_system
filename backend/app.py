from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Flight, Booking

app = Flask(__name__)
CORS(app)  # allow frontend JS to call backend

# SQLite DB (switch to MySQL/Postgres by changing URI)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///airline.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# -------------------------------
# Create DB + Sample Flights
# -------------------------------
@app.before_first_request
def create_tables():
    db.create_all()
    if Flight.query.count() == 0:
        f1 = Flight(flight_no="AI101", origin="Chennai", destination="Bengaluru",
                    departure="2025-11-01 08:00", arrival="2025-11-01 09:15",
                    seats_total=120, seats_available=120, price=3000.0)
        f2 = Flight(flight_no="AI202", origin="Chennai", destination="Delhi",
                    departure="2025-11-02 06:30", arrival="2025-11-02 09:45",
                    seats_total=150, seats_available=150, price=5500.0)
        db.session.add_all([f1, f2])
        db.session.commit()

# -------------------------------
# Routes
# -------------------------------

@app.route("/api/flights")
def get_flights():
    origin = request.args.get("origin", "")
    destination = request.args.get("destination", "")
    query = Flight.query
    if origin: query = query.filter(Flight.origin.ilike(f"%{origin}%"))
    if destination: query = query.filter(Flight.destination.ilike(f"%{destination}%"))
    flights = [f.as_dict() for f in query.all()]
    return jsonify(flights)

@app.route("/api/book", methods=["POST"])
def book_flight():
    data = request.json
    flight = Flight.query.get(data["flightId"])
    if not flight: 
        return jsonify({"success": False, "message": "Flight not found"}), 404
    if flight.seats_available < data["seats"]:
        return jsonify({"success": False, "message": "Not enough seats"}), 400
    
    booking = Booking(
        flight_id=flight.id,
        passenger_name=data["passengerName"],
        passenger_email=data["passengerEmail"],
        seats_booked=data["seats"]
    )
    flight.seats_available -= data["seats"]
    db.session.add(booking)
    db.session.commit()
    return jsonify({"success": True, "message": "Booking confirmed!"})

@app.route("/api/bookings")
def get_bookings():
    bookings = Booking.query.join(Flight).all()
    return jsonify([b.as_dict() for b in bookings])

if __name__ == "__main__":
    app.run(debug=True)
