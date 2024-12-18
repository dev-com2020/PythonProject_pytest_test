class Passenger:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class BookingService:
    def __init__(self):
        self.available_flights = ["Warszawa - Londyn", "Warszawa - Paryż"]


    def book_flight(self, passenger, flight):
        if passenger.age < 18:
            raise ValueError("Pasażer jest niepełnoletni")
        if flight not in self.available_flights:
            raise ValueError("Lot niedostępny")
        return "Rezerwacja potwierdzona"
