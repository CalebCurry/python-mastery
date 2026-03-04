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


def get_city(student: Student) -> str | None:
    if student.address:
        return student.address.city
    return None


def get_oldest(students: list[Student]) -> Student | None:
    if not students:
        return None
    return max(students, key=lambda student: student.age)


students = []
# students.append(Student("Caleb Curry", 95, Address("hello", "this", "is a test")))
# students.append(Student("Kale", 97, Address("hello", "this", "is a test")))

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
