import asyncio
import time

async def main():
    print("main start")

    sum_task = asyncio.create_task(func())

    print("main working...")
    await asyncio.sleep(1)
    print("main working...")
    await asyncio.sleep(1)
    print("main working...")
    await asyncio.sleep(1)
    print("main working...")
    await asyncio.sleep(1)

    print("sum of func: ", await sum_task)
    # asyncio.

    print("main finish")




async def func():
    sum=0
    for i in range(10):
        sum+=i
        await asyncio.sleep(0.01)
    return sum


if __name__ == "__main__":
     asyncio.run( main() )