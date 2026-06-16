import httpx
import asyncio


async def fetch(client, sem):
    async with sem:
        response = await client.get("http://localhost:8000", timeout=30)
        return response


async def main():
    sem = asyncio.Semaphore(5)
    async with httpx.AsyncClient() as client:
        tasks = [fetch(client, sem) for _ in range(300)]

        for response in asyncio.as_completed(tasks):
            print((await response).json())


print("Continue executing")
asyncio.run(main())
