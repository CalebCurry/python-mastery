# import secrets
# import copy
# from pydantic import BaseModel
# import string

# from datetime import datetime, timezone, date, time

# import time as t

# from zoneinfo import ZoneInfo, available_timezones

from urllib.request import urlopen
from bs4 import BeautifulSoup

# import json
# import requests
import httpx

# # random numbers #

# token = secrets.token_hex(32)
# print(token)

# number = secrets.randbelow(1000) + 1
# print(number)

# # copying data #

# original = {"name": "Caleb", "scores": [5, 40, 23]}
# # shallow = copy.copy(original)
# # shallow["scores"][0] = 500

# deep = copy.deepcopy(original)
# deep["scores"][0] = 500

# print(original)
# print(deep)


# class User(BaseModel):
#     name: str
#     scores: list[int]

# user = User(name="Caleb", scores=[1, 2, 3])

# updated = user.model_copy(update={"name": "Someone Else"})
# print(updated)  # name='Someone Else' scores=[1, 2, 3]

# # string operations #

# # go character by character of a larger string input
# print("a" in string.ascii_letters)


## Working with Dates

# dt = datetime.now()

# print(dt)

# print(dt.strftime("%Y-%m-%d %H:%M"))

# date_string = "2026-05-01 11:11:00.100000"

# dt2 = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S.%f")

# print(dt2)

# ## Working with just dates ##

# print(date.today())

# ## Working with just times ##

# print(datetime.now().time())

# ## timestamps ##

# print(t.time())

# ## timezones ##

# dt_zoned = datetime.now(ZoneInfo("America/New_York"))
# print(dt_zoned)

# print(dt_zoned.astimezone(ZoneInfo("America/Los_Angeles")))

# print(dt_zoned.astimezone(ZoneInfo("UTC")))

# ## timing things ##

# # time before
# start = t.time()

# # do something
# total = 0
# for i in range(100000000):
#     total += i
# # time after
# end = t.time()

# # do math
# print(end - start)


# ## perf_counter() ##

# start = t.perf_counter()

# total = 0
# for i in range(100000000):
#     total += i

# end = t.perf_counter()

# print(end - start)

## Web Requests ##

# url = "https://docs.python.org/3/library/datetime.html#format-codes"

# with urlopen(url) as response:
#     soup = BeautifulSoup(response.read(), "html.parser")

# print(soup.head.title.text)  # type: ignore

# # get all links

# for link in soup.body.find_all("a"):  # type: ignore
#     print(link.get("href"))


## JSON ##

url = httpx.URL("https://openlibrary.org/search.json?q=python+programming")
print(url.host, url.path, url.params)

data = httpx.get(url).json()

books = data.get("docs")[:3]

for book in books:
    print(book.get("title"), end="\n\n")
