class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = {}  # {room_number: {"type": "single/double", "price": price, "status": "available/booked"}}
        self.guests = {}  # {guest_id: {"name": name, "room_number": room_number}}

    def add_room(self, room_number, room_type, price):
        if room_number in self.rooms:
            print(f"Room {room_number} already exists.")
        else:
            self.rooms[room_number] = {"type": room_type, "price": price, "status": "available"}
            print(f"Room {room_number} added successfully.")

    def book_room(self, guest_id, guest_name, room_number):
        if room_number not in self.rooms:
            print(f"Room {room_number} does not exist.")
            return

        room = self.rooms[room_number]
        if room["status"] == "booked":
            print(f"Room {room_number} is already booked.")
        else:
            room["status"] = "booked"
            self.guests[guest_id] = {"name": guest_name, "room_number": room_number}
            print(f"Room {room_number} booked successfully for {guest_name}.")

    def check_out(self, guest_id):
        if guest_id not in self.guests:
            print("Guest ID not found.")
            return

        room_number = self.guests[guest_id]["room_number"]
        self.rooms[room_number]["status"] = "available"
        del self.guests[guest_id]
        print(f"Guest ID {guest_id} checked out successfully. Room {room_number} is now available.")

    def view_available_rooms(self):
        print("Available Rooms:")
        for room_number, details in self.rooms.items():
            if details["status"] == "available":
                print(f"Room {room_number}: Type {details['type']}, Price {details['price']}")

    def view_booked_rooms(self):
        print("Booked Rooms:")
        for room_number, details in self.rooms.items():
            if details["status"] == "booked":
                print(f"Room {room_number}: Type {details['type']}, Price {details['price']}")

    def view_guests(self):
        print("Guests:")
        for guest_id, details in self.guests.items():
            print(f"Guest ID {guest_id}: Name {details['name']}, Room {details['room_number']}")

# Example Usage
if __name__ == "__main__":
    hotel = Hotel("Grand View Hotel")

    # Add rooms
    hotel.add_room(101, "single", 100)
    hotel.add_room(102, "double", 150)
    hotel.add_room(103, "single", 100)

    # View available rooms
    hotel.view_available_rooms()

    # Book a room
    hotel.book_room(1, "Alice", 101)
    hotel.book_room(2, "Bob", 102)

    # View booked rooms and guests
    hotel.view_booked_rooms()
    hotel.view_guests()

    # Check out a guest
    hotel.check_out(1)

    # View available rooms again
    hotel.view_available_rooms()
