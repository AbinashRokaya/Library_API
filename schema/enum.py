from enum import Enum

class Status(str,Enum):
    available = "available"
    borrowed = "not-available"


class Gender(str,Enum):
    M = "M"
    F = "F"
    O = "O"

class UserRole(str,Enum):
    admin = "admin"
    librarian = "librarian"
    assistant = "assistant"

class ActionType(str, Enum):
    borrow = "borrow"
    return_ = "return"