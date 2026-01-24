from abc import ABC
from flask import Flask, jsonify, request, url_for

status_options: dict = { 'scheduled', 'checked_in', 'completed', 'canceled', 'no_show'}

class Booking(ABC):
    def __init__(self, booking_id: str, patient_name: str, doctor: str, department: str, date: str, time: str, status: str) -> None:
        self.booking_id = booking_id
        self.patient_name = patient_name
        self.doctor = doctor