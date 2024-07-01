from itertools import count as stream

class User:
    gen_id = stream()

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
        self.id = next(self.gen_id)

    def __str__(self):
        return f"{self.name}\n - Phone: {self.phone}\n - Email: {self.email}"