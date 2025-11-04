class AppointmentScheduler:
    def __init__ (self, appointments: dict[str, dict]) -> None:
        self.appointments = appointments

    def schedule_appointment(self, app_id: str, date: str) -> dict | str:
        if app_id not in self.appointments:
            self.appointments[app_id] = {"date": date, "programmato": True}
            return {app_id: self.appointments[app_id]}
        return "Errore: l'appuntamento esiste già"
    
    def reschedule_appointment(self, app_id: str, new_date: str) -> dict | str:
        if app_id not in self.appointments:
            return "Errore: l'appuntamento non esiste."
        self.appointments[app_id]["date"] = new_date
        return {app_id: self.appointments[app_id]}
    
    def cancel_appointment(self, app_id: str) -> dict | str:
        if app_id not in self.appointments:
            return "Errore: l'appuntamento non esiste."
        self.appointments[app_id]["programmato"] = False
        return {app_id: self.appointments[app_id]}
    
    def remove_appointment(self, app_id: str) -> dict | str:
        if app_id not in self.appointments:
            return "Errore: l'appuntamento non esiste."
        removed_appointment = self.appointments.pop(app_id)
        return {app_id: removed_appointment}
    
    def list_appointments(self) -> list[str]:
        return list(self.appointments.keys())
    
    def get_appointment(self, app_id: str) -> dict | str:
        if app_id not in self.appointments:
            return "Errore: l'appuntamento non esiste."
        return {app_id: self.appointments[app_id]}


if __name__ == "__main__":
    scheduler = AppointmentScheduler({})

    print(scheduler.schedule_appointment("app1", "2024-07-01"))
    print(scheduler.schedule_appointment("app2", "2024-07-02"))
    print(scheduler.list_appointments())
    print(scheduler.get_appointment("app1"))
    print(scheduler.reschedule_appointment("app1", "2024-07-03"))
    print(scheduler.cancel_appointment("app2"))
    print(scheduler.remove_appointment("app1"))
    print(scheduler.list_appointments())