# from typing import Iterable
# from typing import Callable, Any, TypedDict, Literal
# from enum import Enum
# from itertools import chain

from abc import ABC, abstractmethod
from typing import NamedTuple
from dataclasses import dataclass

# data = [1, 5, 9]  # iterable

# it = iter(data)  # iterator

# print(next(it))  # lazy retrieval
# print(next(it))  # lazy retrieval
# print(next(it))  # lazy retrieval


# def firstn(n):
#     num = 0
#     while num < n:
#         yield num
#         num += 1


# data = firstn(100)
# print(data)

# print(next(data))
# print(next(data))
# print(next(data))
# print(next(data))
# print(list(data))  # starts at 4

# for i in firstn(10):  # we have to use a new generator object
#     print(i)

# print(sum((x**2 for x in firstn(10))))


# def print_all(data: Iterable[int | str]) -> None:
#     for d in data:
#         print(d, end="")
#     print()


# print_all(firstn(4))
# print_all("Caleb")

# first = "Caleb"
# last = "Curry"

# name = chain(first, " ", last)
# print_all(name)


# def apply(func: Callable[[int, int], float], a: int, b: int) -> float:
#     return func(a, b)


# def divide(a: int, b: int) -> float:
#     return a / b


# # print(apply(divide, 5, 2))
# print(apply(lambda a, b: a / b, 10, 5))

# ## Any


# def log(value: Any) -> None:
#     print(value)


# ## Typed Dictionary TypedDict


# class UserData(TypedDict):
#     name: str
#     age: int
#     email: str


# def process(data: UserData):
#     print(data["name"])


# data: UserData = {"name": "caleb", "age": 980, "email": "caleb@calebcurry.com"}

# process(data)

# ## Enums


# class SortOrder(Enum):
#     ASC = "asc"
#     DESC = "desc"


# def sort(items, order: SortOrder = SortOrder.ASC):
#     return sorted(items, reverse=(order == "desc"))


# numbers = [34, 65, 23, 87, 34, 234, 76]

# print(sort(numbers, SortOrder.DESC))

# order = SortOrder.DESC
# print(type(order))

# if isinstance(order, SortOrder):
#     print("this is a valid sort order")


class Person(ABC):
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @abstractmethod
    def role(self) -> str: ...

    def introduce(self) -> str:
        return f"I'm {self.name}, a {self.role()}"


class Teacher(Person):
    def __init__(self, name: str, age: int, department: str) -> None:
        super().__init__(name, age)
        self.department = department

    def role(self) -> str:
        return "teacher"


class Student(Person):
    def __init__(self, name: str, age: int, gpa: float) -> None:
        super().__init__(name, age)
        self.gpa = gpa

    def role(self) -> str:
        return "student"


class StudentTuple(NamedTuple):
    name: str
    age: int


def process(person: Person | dict | StudentTuple) -> None:
    if isinstance(person, Person):
        items = person.__dict__
    elif isinstance(person, dict):
        items = person
    elif isinstance(person, StudentTuple):
        items = person._asdict()
    else:
        raise TypeError("expected person")

    for key, value in items.items():
        print(key, value)


process(Teacher("Caleb", 50, "compsci"))
process(Student("John", 54, 3.5))
process({"name": "Caleb"})


process(StudentTuple("Caleb Tuple", 85))

## Data class


@dataclass
class Course:
    name: str
    instructor: str
    credits: int


print(Course("math", "Caleb", 4))

print(Course("math", "Caleb", 4) == Course("math", "Caleb", 4))

print(type(Course("math", "Caleb", 4)))
