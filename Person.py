# Class

class Person:
    def __init__(self, name, email, ID=0) -> None:
        self.name = name
        self.email = email
        self.ID = ID

    def __repr__(self) -> str:
        return f"Person('{self.name}', {self.email}, {self.ID})"
