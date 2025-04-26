class Room:
    def __init__(self, id:str, floor:int, seats:int):
        self.id = id
        self.floor = floor
        self.seats = seats
        self.area = seats * 2

    def get_id(self):
        return self.id
    
    def get_floor(self):
        return self.floor
    
    def get_seats(self):
        return self.seats
    
    def get_area(self):
        return self.area
    
class Building:
    def __init__(self, name: str, address: str, floors: tuple):
        self.name = name
        self.address = address
        self.floors = floors
        self.rooms = []

    def get_floors(self):
        return self.floors

    def get_rooms(self):
        return self.rooms

    def add_room(self, room):
        exroom = [r.get_id() for r in self.rooms]
        if room.get_id() not in exroom and room.get_floor() in range(self.floors[0], self.floors[1] + 1):
            self.rooms.append(room)

    def area(self):
        return sum(room.get_area() for room in self.rooms)
    
