from abc import ABC, abstractmethod
from typing import Any

from flask import Flask, jsonify, request, url_for

status_codes = { 'online', 'offline', 'error' , 'error' }

class SmartDevice(ABC):
    def __init__ (self, serial_number: str, brand: str, room: str, installation_year: int, status: str) -> None:
        self.serial_number = serial_number
        self.brand = brand
        self.room = room
        self.installation_year = installation_year
        self.status = status

    @abstractmethod
    def device_type(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def energy_consumption(self) -> float | int:
        raise NotImplementedError
    
    @abstractmethod
    def connection_quality(self) -> int:
        raise NotImplementedError
    
    def info(self) -> dict[str, float | int | str]:
        return {
            "serial_number": self.serial_number,
            "brand": self.brand,
            "room": self.room,
            "installation_year": self.installation_year,
            "status": self.status,
            "device": self.device_type()
        }
    
    def diagnostic_time(self, factor: float = 1.0) -> float:
        seconds = float(self.energy_consumption() * factor + self.connection_quality())
        return int(round(seconds))
    
class SmartBulb(SmartDevice):
    def __init__ (self, serial_number: str, brand: str, room: str, installation_year: int, status: str, brightness_lumens: int, color_capability: bool) -> None:
        super().__init__(serial_number, brand, room, installation_year, status)
        self.brightness_lumens = brightness_lumens
        self.color_capability = color_capability

    def device_type(self) -> str:
        return "bulb"

    def energy_consumption(self) -> float | int:
        return 9
    
    def connection_quality(self) -> int:
        return 2
    
    def info(self) -> dict[str, float | int | str]:
        data = super().info()
        data.update(
            {
                "brightness_lumens": self.brightness_lumens,
                "color_capability": self.color_capability,
            }
        )
        return data
    
class SecurityCamera(SmartDevice):
    def __init__(self,serial_number: str, brand: str, room: str, installation_year: int, status: str, resolution: str, night_vision: bool) -> None:
        super().__init__(serial_number, brand, room, installation_year, status)
        self.resolution = resolution
        self.night_vision = night_vision

    def device_type(self) -> str:
        return "camera"

    def energy_consumption(self) -> float | int:
        return 50

    def connection_quality(self) -> int:
        return 9

    def info(self) -> dict[str, float | int | str | bool]:
        data = super().info()
        data.update({"resolution": self.resolution, "night_vision": self.night_vision})
        return data


class IoTHub:
    def __init__(self) -> None:
        self.devices: dict[str, SmartDevice] = {}

    def add(self, device: SmartDevice) -> bool:
        if device.serial_number not in self.devices:
            self.devices[device.serial_number] = device
            return True
        return False

    def get(self, serial_number: str) -> SmartDevice | None:
        return self.devices.get(serial_number)

    def update(self, serial_number: str, new_device: SmartDevice) -> None:
        self.devices[serial_number] = new_device

    def patch_status(self, serial_number: str, new_status: str) -> None:
        d = self.devices.get(serial_number)
        if d is None:
            return
        d.status = new_status

    def delete(self, serial_number: str) -> bool:
        if serial_number not in self.devices:
            return False
        del self.devices[serial_number]
        return True

    def list_all(self) -> list[dict[str, float | int | str | bool]]:
        return [d.info() for d in self.devices.values()]


app = Flask(__name__)

iot_hub = IoTHub()

Smartbulb = SmartBulb("SB123", "Philips", "Living Room", 2020, "online", 800, True)
iot_hub.add(Smartbulb)

Securitycamera = SecurityCamera("SC456", "Nest", "Front Door", 2021, "online", "1080p", True)
iot_hub.add(Securitycamera)

@app.route("/", methods=["GET"])
def index() -> Any:
    links = {
        "devices": url_for("list_devices", _external=True),
        "devices/<serial_number>": url_for("get_device", serial_number="<serial_number>", _external=True),
        "devices/<serial_number>/diagnostic": url_for("device_diagnostic", serial_number="<serial_number>", _external=True),
    }   
    return jsonify({
        "message": "Welcome to the Smart Home IoT Hub API",
        "links": links
        }
    )

@app.route("/devices", methods=["GET"])
def list_devices() -> Any:
    devices = iot_hub.list_all()
    return jsonify(devices), 200

@app.route("/devices/<serial_number>", methods=["GET"])
def get_device(serial_number: str) -> Any:
    device = iot_hub.get(serial_number)
    if device is None:
        return jsonify({"error": "Device not found"}), 404
    return jsonify(device.info()), 200

@app.route("/devices/<serial_number>/diagnostic/<factor>", methods=["GET"])
def device_diagnostic(serial_number: str) -> Any:
    device = iot_hub.get(serial_number)
    if device is None:
        return jsonify({"error": "Device not found"}), 404
    factor = float(factor)
    time_seconds = device.diagnostic_time(factor)

    return jsonify({
        "serial_number": serial_number,
        "diagnostic_time_seconds": time_seconds
    }), 200

@app.route("/devices", methods=["POST"])
def add_device() -> Any:
    data = request.get_json()
    # Validate input data
    if not isinstance(data, dict):
        return jsonify({"error": "Invalid input"}), 400
    
    # Create device based on type
    device_type = data.get("device")

    # Check required fields
    if device_type == "bulb":
        d = SmartBulb(
            serial_number=data["serial_number"],
            brand=data["brand"],
            room=data["room"],
            installation_year=data["installation_year"],
            status=data["status"],
            brightness_lumens=data["brightness_lumens"],
            color_capability=data["color_capability"]
        )
    elif device_type == "camera":
        d = SecurityCamera(
            serial_number=data["serial_number"],
            brand=data["brand"],
            room=data["room"],
            installation_year=data["installation_year"],
            status=data["status"],
            resolution=data["resolution"],
            night_vision=data["night_vision"]
        )
    else:
        return jsonify({"error": "Invalid device type"}), 400
    
    # Add device to IoT Hub
    ok = iot_hub.add(d)
    if not ok:
        return jsonify({"error": "Device already exists"}), 400

    # Return created device info
    return jsonify(d.info()), 201

@app.route("/devices/<serial_number>", methods=["PUT"])
def update_device(serial_number: str) -> Any:
    data = request.get_json()
    # Validate input data
    if not isinstance(data, dict):
        return jsonify({"error": "Invalid input"}), 400

    # Check if device exists
    existing_device = iot_hub.get(serial_number)
    if existing_device is None:
        return jsonify({"error": "Device not found"}), 404

    # Create updated device based on type
    device_type = data.get("device")
    if device_type == "bulb":
        d = SmartBulb(
            serial_number=serial_number,
            brand=data["brand"],
            room=data["room"],
            installation_year=data["installation_year"],
            status=data["status"],
            brightness_lumens=data["brightness_lumens"],
            color_capability=data["color_capability"]
        )
    elif device_type == "camera":
        d = SecurityCamera(
            serial_number=serial_number,
            brand=data["brand"],
            room=data["room"],
            installation_year=data["installation_year"],
            status=data["status"],
            resolution=data["resolution"],
            night_vision=data["night_vision"]
        )
    else:
        return jsonify({"error": "Invalid device type"}), 400

    iot_hub.update(serial_number, d)
    return jsonify(d.info()), 200

@app.route("/devices/<serial_number>/status", methods=["PATCH"])
def patch_device_status(serial_number: str) -> Any:
    data = request.get_json()
    if not isinstance(data, dict) or "status" not in data:
        return jsonify({"error": "Invalid input"}), 400

    new_status = data["status"]
    if new_status not in status_codes:
        return jsonify({"error": "Invalid status value"}), 400

    device = iot_hub.get(serial_number)
    if device is None:
        return jsonify({"error": "Device not found"}), 404

    iot_hub.patch_status(serial_number, new_status)
    return jsonify({"message": "Status updated"}), 200

@app.route("/devices/<serial_number>", methods=["DELETE"])
def delete_device(serial_number: str) -> Any:
    ok = iot_hub.delete(serial_number)
    if not ok:
        return jsonify({"error": "Device not found"}), 404
    return jsonify({"message": "Device deleted"}), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)