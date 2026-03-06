from typing import Any, ItemsView, Protocol
# from _collections_abc import dict_items


class Address:
    def __init__(self, street: str, city: str, state: str) -> None:
        self.street = street
        self.city = city
        self.state = state


class Student:
    def __init__(self, name: str, age: int, address: Address | None) -> None:
        self.name = name
        self.age = age
        self.address = address

    def items(self):
        return self.__dict__.items()


def get_city(student: Student) -> str | None:
    if student.address:
        return student.address.city
    return None


class HasAge(Protocol):
    age: int


def get_oldest[T: HasAge](data: list[T]) -> T | None:
    if not data:
        return None
    return max(data, key=lambda d: d.age)


class SupportsItems(Protocol):
    # def items(self) -> dict_items[str, Any]: ...
    def items(self) -> ItemsView[str, Any]: ...


def print_data[T: SupportsItems](data: T) -> T:
    for key, value in data.items():
        print(key, value)
    return data


students: list[Student] = []
students.append(Student("Caleb Curry", 95, Address("hello", "this", "is a test")))
students.append(Student("Kale", 97, Address("hello", "this", "is a test")))

student = {"name": "Paul", "age": 30, "Address": None}
print_data(student)
print_data(students[0])

# Call function then check return
student = get_oldest(students)
if student:
    print(student.name)

# Conditional Expression (Ternary)
# Value or some default
name = student.name if student else "Unknown"
print(name)

# Walrus Operator
# Assignment Expression
if student := get_oldest(students):
    print(student.name)

# Try Except
# Bascically optional chaining equivalent
student = None
try:
    student = get_oldest(students)
    print(student.address.city)  # type: ignore
except AttributeError:
    # Keep print commented out to fail silently and just go with None
    pass
    # print("Error accessing data")

print(student)
