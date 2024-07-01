# Event Creation and Management:

# Store information about events, including event ID, name, date, time, location, and participant limit.
# Implement a function to add new events.
# Implement a function to remove events.
# Implement a function to search for events by name, date, or location using searching algorithms.

# Participant Management:

# Maintain a dictionary of participants for each event, with participant ID as the key and participant details (name, contact information) as the value.
# Implement a function to register participants for an event, ensuring the participant limit is not exceeded.
# Implement a function to remove participants from an event.
# Implement a function to display participant details for a given event.

# Scheduling:

# Implement a function to display a schedule of all events.
# Implement a waitlist system using a queue for events that reach participant capacity.
# When a participant leaves the event, allow the first person in the queue to join the event

# Data Structures and Algorithms:

# Use a dictionary to store event information, with event ID as the key.
# Use a dictionary to maintain the participants for each event.
# Implement binary search for efficient searching within the event list.
# Implement sorting algorithms to display events in chronological order.

# Additional Features (Optional):

# Implement a feature to suggest events to participants based on their registration history and interests.
# Implement a feature to generate a report of all events and participants.

from manager import Manager

m = Manager()

m.add_event("Inaugeration", "2024-7-7", "City Hall", 200)
m.add_event("Birthday", "2024-7-7", "Community Center", 2)
m.add_event("Bar Mitzvah", "2024-7-7", "Community Center", 20)

alice = m.add_user("Alice", "5555555", "alice@example.com")
bob = m.add_user("Bob", "5555555", "bob@example.com")
cassidy = m.add_user("Cassidy", "5555555", "cassidy@example.com")
david = m.add_user("David", "5555555", "david@example.com")

for event in m.find_event_by_location("Community Center","Community Center"):
    print(event)
birthday = m.find_event_by_name("Birthday")
birthday.details()
m.register(bob, birthday)
m.register(alice, birthday)
m.register(cassidy, birthday)
m.register(david, birthday)
birthday.details()
m.remove_user(bob)
birthday.details()

for user in m.find_user_by_phone("5555555","5555555"):
    print(user)