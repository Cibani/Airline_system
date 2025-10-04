const apiBase = "http://127.0.0.1:5000/api";

document.getElementById("searchBtn").addEventListener("click", searchFlights);
document.getElementById("bookingForm").addEventListener("submit", submitBooking);
document.getElementById("cancelBooking").addEventListener("click", () =>
  document.getElementById("bookForm").classList.add("hidden")
);
document.getElementById("refreshBookings").addEventListener("click", fetchBookings);

async function searchFlights() {
  const origin = document.getElementById("origin").value;
  const destination = document.getElementById("destination").value;
  const res = await fetch(`${apiBase}/flights?origin=${origin}&destination=${destination}`);
  const flights = await res.json();
  renderFlights(flights);
}

function renderFlights(flights) {
  const div = document.getElementById("flights");
  div.innerHTML = "";
  if (!flights.length) return (div.innerHTML = "<div>No flights found.</div>");
  flights.forEach((f) => {
    const el = document.createElement("div");
    el.className = "flight";
    el.innerHTML = `<b>${f.flight_no}</b> — ${f.origin} → ${f.destination} 
      <div class="small">Depart: ${f.departure} | Seats: ${f.seats_available} | ₹${f.price}</div>`;
    const btn = document.createElement("button");
    btn.textContent = "Book";
    btn.disabled = f.seats_available <= 0;
    btn.onclick = () => openBooking(f);
    el.appendChild(btn);
    div.appendChild(el);
  });
}

function openBooking(f) {
  document.getElementById("flightId").value = f.id;
  document.getElementById("bookForm").classList.remove("hidden");
}

async function submitBooking(e) {
  e.preventDefault();
  const payload = {
    flightId: parseInt(document.getElementById("flightId").value),
    passengerName: document.getElementById("pname").value,
    passengerEmail: document.getElementById("pemail").value,
    seats: parseInt(document.getElementById("seats").value),
  };
  const res = await fetch(`${apiBase}/book`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  const data = await res.json();
  document.getElementById("bookingMsg").textContent = data.message;
  if (data.success) {
    document.getElementById("bookingForm").reset();
    document.getElementById("bookForm").classList.add("hidden");
    searchFlights();
    fetchBookings();
  }
}

async function fetchBookings() {
  const res = await fetch(`${apiBase}/bookings`);
  const bookings = await res.json();
  const div = document.getElementById("bookingList");
  div.innerHTML = "";
  if (!bookings.length) return (div.innerHTML = "<div>No bookings yet.</div>");
  bookings.forEach((b) => {
    const el = document.createElement("div");
    el.className = "flight";
    el.innerHTML = `<b>${b.passenger_name}</b> — ${b.flight_no} <span class="small">(Seats: ${b.seats_booked})</span><div class="small">Booked at: ${b.booked_at}</div>`;
    div.appendChild(el);
  });
}

fetchBookings();
