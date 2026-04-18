from dataclasses import dataclass

@dataclass(frozen=True)
class User:
    name: str


u = User("Alice")
hash(u)

u.name = "Bob"