import asyncio
import random
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    wait = random.randint(1, 10)
    print("waiting", wait)
    await asyncio.sleep(wait)
    return {"waited": wait}
