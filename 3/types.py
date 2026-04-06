# from typing import Iterable
from typing import Callable, Any, TypedDict, Literal
from enum import Enum
# from itertools import chain

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


def apply(func: Callable[[int, int], float], a: int, b: int) -> float:
    return func(a, b)


def divide(a: int, b: int) -> float:
    return a / b


# print(apply(divide, 5, 2))
print(apply(lambda a, b: a / b, 10, 5))

## Any


def log(value: Any) -> None:
    print(value)


## Typed Dictionary TypedDict


class UserData(TypedDict):
    name: str
    age: int
    email: str


def process(data: UserData):
    print(data["name"])


data: UserData = {"name": "caleb", "age": 980, "email": "caleb@calebcurry.com"}

process(data)

## Enums


class SortOrder(Enum):
    ASC = "asc"
    DESC = "desc"


def sort(items, order: SortOrder = SortOrder.ASC):
    return sorted(items, reverse=(order == "desc"))


numbers = [34, 65, 23, 87, 34, 234, 76]

print(sort(numbers, SortOrder.DESC))
