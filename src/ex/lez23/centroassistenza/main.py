from abc import ABC, abstractmethod
from flask import Flask, jsonify, request, abort, url_for

class Device(ABC):
    def __init__(self, id: str, model: str, customer_name: str, purchase_year: int, status: str):
        self.id = id
        self.model = model
        self.customer_name = customer_name
        self.purchase_year = purchase_year
        self.status = status

    @abstractmethod
    def device_type(self) -> str:
        pass

    @abstractmethod
    def base_diagnosis_time(self) -> int:
        pass

    @abstractmethod
    def repair_complexity(self) -> int:
        pass

    def info(self) -> dict:
        return self.__dict__.copy()

    def estimated_total_time(self, factor: float = 1.0) -> int:
        return int(self.base_diagnosis_time() * factor + self.repair_complexity())


class Smartphone(Device):
    def __init__(self, id: str, model: str, customer_name: str, purchase_year: int, status: str, has_protective_case: bool, storage_gb: int):
        super().__init__(id, model, customer_name, purchase_year, status)
        self.has_protective_case = has_protective_case
        self.storage_gb = storage_gb

    def device_type(self) -> str:
        return "smartphone"

    def base_diagnosis_time(self) -> int:
        return 20

    def repair_complexity(self) -> int:
        return 3


class Laptop(Device):
    def __init__(self, id: str, model: str, customer_name: str, purchase_year: int, status: str, has_dedicated_gpu: bool, screen_size_inch: float):
        super().__init__(id, model, customer_name, purchase_year, status)
        self.has_dedicated_gpu = has_dedicated_gpu
        self.screen_size_inch = screen_size_inch

    def device_type(self) -> str:
        return "laptop"

    def base_diagnosis_time(self) -> int:
        return 40

    def repair_complexity(self) -> int:
        return 5


class ServiceCenter:
    def __init__(self, devices: dict[str, Device] | None = None):
        self.devices = devices or {}

    def add_device(self, device: Device):
        if device.id in self.devices:
            raise ValueError(f"Device with ID {device.id} already exists.")
        self.devices[device.id] = device

    def get_device(self, id: str) -> Device | None:
        return self.devices.get(id)

    def update(self, id: str, new_device: Device):
        if id not in self.devices:
            raise ValueError(f"Device with ID {id} does not exist.")
        if new_device.id != id:
            raise ValueError("New device ID must match the existing one.")
        self.devices[id] = new_device

    def patch_status(self, id: str, new_status: str):
        device = self.get_device(id)
        if not device:
            raise ValueError(f"Device with ID {id} does not exist.")
        device.status = new_status

    def list_all(self) -> list[dict]:
        return [device.info() for device in self.devices.values()]


service_center = ServiceCenter()
# Adding some initial devices for demonstration
service_center.add_device(Smartphone("s1", "iPhone 12", "Alice", 2020, "in repair", True, 128))
service_center.add_device(Laptop("l1", "Dell XPS 15", "Bob", 2019, "waiting for parts", False, 15.6))

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Welcome to the Service Center API",
        "links": {
            "devices": url_for('list_devices'),
            "device_example": url_for('get_device', id='s1'),
            "device_example_estimate": url_for('device_estimate', id='s1', factor=1.5)
        }
    })

@app.get('/devices')
def list_devices():
    return jsonify(service_center.list_all())

@app.get('/devices/<id>')
def get_device(id):
    device = service_center.get_device(id)
    
    if not device:
        abort(404, description="Device not found")
    return jsonify(device.info())

@app.get('/devices/<id>/estimate/<float:factor>')
def device_estimate(id, factor):
    device = service_center.get_device(id)

    if not device:
        abort(404, description="Device not found")
    estimated_time = device.estimated_total_time(factor)
    return jsonify({
        "device_id": id,
        "estimated_total_time": estimated_time
    })

@app.post('/devices')
def add_device():
    data = request.get_json()

    # 1. Added "type" to required fields
    required = ["id", "model", "customer_name", "purchase_year", "status", "type"]
    if not all(k in data for k in required):
        return jsonify({"Error": "Missing Fields"}), 400
    
    # 2. Corrected method name to get_device
    if service_center.get_device(data["id"]):
        return jsonify({"Error": "Device already present"}), 400

    if data["type"] == "smartphone":
        new_device = Smartphone(
            id=data["id"],
            model=data["model"],
            customer_name=data["customer_name"],
            purchase_year=data["purchase_year"],
            status=data["status"],
            has_protective_case=data.get("has_protective_case", False),
            storage_gb=data.get("storage_gb", 0)
        )
    elif data["type"] == "laptop":
        new_device = Laptop(
            id=data["id"],
            model=data["model"],
            customer_name=data["customer_name"],
            purchase_year=data["purchase_year"],
            status=data["status"],
            has_dedicated_gpu=data.get("has_dedicated_gpu", False),
            screen_size_inch=data.get("screen_size_inch", 0.0)
        )
    else:
        return jsonify({"Error": "Invalid device type"}), 400
    
    service_center.add_device(new_device)
    return jsonify(new_device.info()), 201

@app.put('/devices/<id>')
def update_device(id):
    data = request.get_json()

    required = ["id","model","customer_name","purchase_year","status"]
    if not all(k in data for k in required):
        return jsonify({"Error" : "Missing Fields"}), 400
    
    if not service_center.get(id):
        return jsonify({"Error": "Device not found"}), 404

    if data["type"] == "smartphone":
        updated_device = Smartphone(
            id=data["id"],
            model=data["model"],
            customer_name=data["customer_name"],
            purchase_year=data["purchase_year"],
            status=data["status"],
            has_protective_case=data.get("has_protective_case"),
            storage_gb=data.get("storage_gb")
            )
    elif data["type"] == "laptop":
        updated_device = Laptop(
            id=data["id"],
            model=data["model"],
            customer_name=data["customer_name"],
            purchase_year=data["purchase_year"],
            status=data["status"],
            has_dedicated_gpu=data.get("has_dedicated_gpu"),
            screen_size_inch=data.get("screen_size_inch")
        )
    else:
        return jsonify({"Error": "Invalid device type"}), 400

    try:
        service_center.update(id, updated_device)
    except ValueError as e:
        return jsonify({"Error": str(e)}), 400

    return jsonify(updated_device.info()), 200

@app.patch('/devices/<id>/status')
def patch_device_status(id):
    data = request.get_json()
    if "status" not in data:
        return jsonify({"Error": "Missing status field"}), 400

    try:
        service_center.patch_status(id, data["status"])
    except ValueError as e:
        return jsonify({"Error": str(e)}), 404

    device = service_center.get_device(id)
    return jsonify(device.info()), 200

@app.delete('/devices/<id>')
def delete_device(id):
    device = service_center.get_device(id)
    if not device:
        return jsonify({"Error": "Device not found"}), 404
    
    del service_center.devices[id]
    return jsonify({"message": "Device deleted successfully"}), 200


if __name__ == '__main__':
    app.run(debug=True)