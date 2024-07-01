from itertools import count as stream
from collections import deque
from quicksort import quicksort

class Doppelganger(Exception):
    pass

class Event:
    gen_id = stream()

    def __init__(self, name, datetime, location, capacity):
        self.name = name
        self.datetime = datetime
        self.location = location
        self.cap = capacity
        self.id = next(self.gen_id)
        self.guests = {}
        self.waiting = deque()
    
    def __str__(self):
        return f"{self.name}\n - Datetime: {self.datetime}\n - Location: {self.location}"

    def add_guest(self, guest):
        if guest.id in self.guests:
            raise Doppelganger("The authorities have been notified")
        elif len(self.guests) < self.cap:
            self.guests[guest.id] = guest
            return 'added'
        else:
            self.waiting.append(guest)
            return 'waited'
    
    def remove_guest(self, guest_id):
        if guest_id in self.guests:
            del self.guests[guest_id]
            if self.waiting:
                backup = self.waiting.popleft()
                self.guests[backup.id] = backup

    def details(self):
        guest_list = [guest.name for guest in self.guests.values()]
        quicksort(guest_list)
        print(self)
        print(f" - Capacity: {self.cap}")
        print("Guest List")
        for name in guest_list:
            print(f" - {name}")
        print("Wait List")
        for n, user in enumerate(self.waiting, start=1):
            print(f" {n} {user.name}")
