from abc import ABC, abstractmethod
from flask import Flask, jsonify, request, url_for

status_options: dict = { 'scheduled', 'checked_in', 'completed', 'canceled', 'no_show'}

class Booking(ABC):
    def __init__(self, booking_id: str, patient_name: str, doctor: str, department: str, date: str, time: str, status: str) -> None:
        self.booking_id = booking_id
        self.patient_name = patient_name
        self.doctor = doctor
        self.department = department
        self.date = date
        self.time = time
        self.status = status

    @abstractmethod
    def booking_type(self) -> str:
        raise NotImplementedError
    
    @abstractmethod
    def base_duration(self) -> int:
        raise NotImplementedError
    
    @abstractmethod
    def priority_level(self) -> int:
        raise NotImplementedError
    
    def info(self) -> dict[str, int | str | bool | float]:
        return {
            "id": self.booking_id,
            "patient_name": self.patient_name,
            "doctor": self.doctor,
            "department": self.department,
            "date": self.date,
            "time": self.time,
            "status": self.status,
            "type": self.booking_type()
        }
    
    def estimated_wait(self, factor: float = 1.0) -> int:
        result = self.base_duration() * factor + self.priority_level() * 5
        return int(round(result))
    
class MedicalVisit(Booking):
    def __init__(self, booking_id: str, patient_name: str, doctor: str, department: str, date: str, time: str, status: str, visit_reason: str, first_time: bool) -> None:
        super().__init__(booking_id, patient_name, doctor, department, date, time, status)
        self.visit_reason = visit_reason
        self.first_time = first_time

    def booking_type(self) -> str:
        return 'visit'
    
    def base_duration(self) -> int:
        return 20
    
    def priority_level(self) -> int:
        reason = (self.visit_reason or "").lower()
        keywords = ["urgente", "dolore", "acuto", "svenimento"]
        if reason in keywords:
            return 7
        return 5
    
    def info(self) -> dict[str, int | str | bool | float]:
        data = super().info()
        data.update(
            {
                "visit_reason": self.visit_reason,
                "first_time": self.first_time
            }
        )
        return data
    
class DiagnosticExam(Booking):
    def __init__(self, booking_id: str, patient_name: str, doctor: str, department: str, date: str, time: str, status: str, exam_type: str, requires_fasting: bool) -> None:
        super().__init__(booking_id, patient_name, doctor, department, date, time, status)
        self.exam_type = exam_type
        self.requires_fasting = requires_fasting

    def booking_type(self) -> str:
        return "exam"
    
    def base_duration(self) -> int:
        return 30
    
    def priority_level(self) -> int:
        et = (self.exam_type or "").strip().lower()
        if et in ["rmn","mri","tac","ct"]:
            return 8
        return 7
    
    def info(self) -> dict[str, int | str | bool | float]:
        data = super().info()
        data.update(
            {
                "exam_type": self.exam_type,
                "requires_fasting": self.requires_fasting
            }
        )
        return data
    
class ClinicHub:
    def __init__(self):
        self.bookings : dict[str, Booking] = {}

    def add(self, booking: Booking) -> bool:
        if booking.booking_id in self.bookings:
            return False
        self.bookings[booking.booking_id] = booking
        return True
    
    def get(self, booking_id: str) -> Booking | None:
        return self.bookings.get(booking_id)
    
    def update(self, booking_id: str, new_booking: Booking) -> None:
        self.bookings[booking_id] = new_booking

    def patch_status(self, booking_id: str, new_status: str) -> None:
        b = self.bookings.get(booking_id)
        b.status = new_status

    def delete(self, booking_id: str) -> bool:
        if booking_id not in self.bookings:
            return False
        del self.bookings[booking_id]
        return True
    
    def list_all(self) -> list[dict[str, int | str | bool | float]]:
        return [b.info() for b in self.bookings.values()]
    
app = Flask(__name__)
clinic = ClinicHub()

visit1 = MedicalVisit("b001", "Mario Rossi", "Dr. Bianchi", "Cardiology", "2024-07-01", "10:00", "scheduled", "Dolore toracico acuto", True)
exam1 = DiagnosticExam("b002", "Luigi Verdi", "Dr. Neri", "Radiology", "2024-07-02", "11:30", "scheduled", "RMN", False)

clinic.add(visit1)
clinic.add(exam1)

@app.get("/")
def index():
    return jsonify({
        "message": "Clinic Booking Hub API",
        "links": {
            "bookings_list": url_for("bookings"),
            "booking_sample": url_for("get_booking", booking_id="b001"),
            "estimate_sample": url_for("estimated_wait", booking_id="b001", factor=1.5)
        }
    })

@app.get("/bookings")
def bookings():
    data = clinic.list_all()
    return jsonify(data)

@app.get("/bookings/<booking_id>")
def get_booking(booking_id):
    # 1. Get the object from the hub
    booking = clinic.get(booking_id)
    
    # 2. Check if it actually exists
    if booking is None:
        return jsonify({"error": "booking not found"}), 404
    
    # 3. Call .info() to get the dictionary representation
    return jsonify(booking.info())

@app.get("/bookings/<booking_id>/wait/<factor>")
def estimated_wait(booking_id: str, factor: float):
    # 1. Get the object from the hub
    booking = clinic.get(booking_id)

    # 2. Check if it actually exists
    if booking is None:
        return jsonify({"error": "booking not found"}), 404
    
    factor = float(factor)
    wait_time = booking.estimated_wait(factor)

    return jsonify({
        "booking_id": booking_id,
        "booking_type": booking.booking_type(),
        "estimated_wait_minutes": wait_time
    })

@app.post("/bookings")
def create_booking():
    # 1. Grab the JSON data
    data = request.get_json()
    
    # 2. Basic Validation: Check for required base fields
    required = ["id", "patient_name", "doctor", "department", "date", "time", "type"]
    if not all(k in data for k in required):
        return jsonify({"error": "Missing required fields"}), 400
    
    # 3. Check if ID already exists in the hub
    if clinic.get(data["id"]):
        return jsonify({"error": "Booking ID already exists"}), 400

    # 4. Logic to create the correct subclass instance (The "Factory" pattern)
    try:
        if data["type"] == "visit":
            new_booking = MedicalVisit(
                booking_id=data["id"],
                patient_name=data["patient_name"],
                doctor=data["doctor"],
                department=data["department"],
                date=data["date"],
                time=data["time"],
                status="scheduled",
                visit_reason=data.get("visit_reason", ""),
                first_time=data.get("first_time", False)
            )
        elif data["type"] == "exam":
            new_booking = DiagnosticExam(
                booking_id=data["id"],
                patient_name=data["patient_name"],
                doctor=data["doctor"],
                department=data["department"],
                date=data["date"],
                time=data["time"],
                status="scheduled",
                exam_type=data.get("exam_type", ""),
                requires_fasting=data.get("requires_fasting", False)
            )
        else:
            return jsonify({"error": "Invalid booking type. Must be 'visit' or 'exam'"}), 400

        # 5. Add to ClinicHub and return success
        clinic.add(new_booking)
        return jsonify(new_booking.info()), 201

    except Exception as e:
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500
    
@app.put("/bookings/<booking_id>")
def update_booking(booking_id):
    data = request.get_json()
    
    # 1. Validation: Does the ID in the URL match the ID in the body?
    if data.get("id") != booking_id:
        return jsonify({"error": "URL ID and Body ID mismatch"}), 400

    # 2. Re-instantiate the correct type (similar logic to POST)
    if data.get("type") == "visit":
        updated_obj = MedicalVisit(booking_id, data['patient_name'], data['doctor'], 
                                   data['department'], data['date'], data['time'], 
                                   data['status'], data['visit_reason'], data['first_time'])
    elif data.get("type") == "exam":
        updated_obj = DiagnosticExam(booking_id, data['patient_name'], data['doctor'], 
                                     data['department'], data['date'], data['time'], 
                                     data['status'], data['exam_type'], data['requires_fasting'])
    else:
        return jsonify({"error": "Invalid type"}), 400

    # 3. Update in Hub
    clinic.update(booking_id, updated_obj)
    return jsonify(updated_obj.info())

@app.patch("/bookings/<booking_id>/status")
def patch_booking(booking_id):
    booking = clinic.get(booking_id)
    if not booking:
        return jsonify({"error": "Booking not found"}), 404
    
    data = request.get_json()
    
    # Update only the fields provided in the JSON
    if "status" in data:
        if data["status"] in status_options:
            booking.status = data["status"]
        else:
            return jsonify({"error": "Invalid status option"}), 400
            
    return jsonify(booking.info())

@app.delete("/bookings/<booking_id>")
def delete_booking(booking_id):
    success = clinic.delete(booking_id)
    
    if not success:
        return jsonify({"error": "Booking not found"}), 404
    
    # 204 means "I did it, but I have nothing to show you back"
    return '', 204


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
