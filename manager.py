from collections import namedtuple

from avl import AVL
from event import Event
from user import User

SuperIndex = namedtuple("index", ("events", "users"))
UserIndex = namedtuple("users", ("name", "phone", "email"))
EventIndex = namedtuple("events", ("name", "datetime", "location"))

def has_id(id):
    return lambda x: x.id == id

class Manager:
    def __init__(self):
        self.events = {}
        self.users = {}
        self.index = SuperIndex(
            EventIndex(AVL(), AVL(), AVL()),
            UserIndex(AVL(), AVL(), AVL())
        )

    def add_event(self, name, datetime, location, capacity):
        new_event = Event(name, datetime, location, capacity)
        self.events[new_event.id] = new_event
        self.index.events.name.insert(new_event, new_event.name)
        self.index.events.datetime.insert(new_event, new_event.datetime)
        self.index.events.location.insert(new_event, new_event.location)
        return new_event

    def remove_event(self, event_id):
        old_event = self.events[event_id]
        del self.events[event_id]
        self.index.events.name.remove(old_event.name, prop=has_id(event_id))
        self.index.events.datetime.remove(old_event.datetime, prop=has_id(event_id))
        self.index.events.location.remove(old_event.location, prop=has_id(event_id))

    def find_event_by_name(self, start, end=None):
        if end is None:
            return self.index.events.name.find(start)
        else:
            return self.index.events.name.get_range(start, end)

    def find_event_by_datetime(self, start, end=None):
        if end is None:
            return self.index.events.datetime.find(start)
        else:
            return self.index.events.datetime.get_range(start, end)

    def find_event_by_location(self, start, end=None):
        if end is None:
            return self.index.events.location.find(start)
        else:
            return self.index.events.location.get_range(start, end)

    def add_user(self, name, phone, email):
        new_user = User(name, phone, email)
        self.users[new_user.id] = new_user
        self.index.users.name.insert(new_user, new_user.name)
        self.index.users.phone.insert(new_user, new_user.phone)
        self.index.users.email.insert(new_user, new_user.email)
        return new_user

    def remove_user(self, user):
        del self.users[user.id]
        self.index.users.name.remove(user.name, prop=has_id(user.id))
        self.index.users.phone.remove(user.phone, prop=has_id(user.id))
        self.index.users.email.remove(user.email, prop=has_id(user.id))
        for event in self.events.values():
            event.remove_guest(user.id)
    
    def find_user_by_name(self, start, end=None):
        if end is None:
            return self.index.users.name.find(start)
        else:
            return self.index.users.name.get_range(start, end)

    def find_user_by_phone(self, start, end=None):
        if end is None:
            return self.index.users.phone.find(start)
        else:
            return self.index.users.phone.get_range(start, end)

    def find_user_by_email(self, start, end=None):
        if end is None:
            return self.index.users.email.find(start)
        else:
            return self.index.users.email.get_range(start, end)

    def register(self, user, event):
        result = event.add_guest(user)
        if result == 'added':
            print(f"{user.name} has been registered for {event.name}")
        elif result == 'waited':
            print(f"{user.name} has been placed on the waitlist for {event.name}")