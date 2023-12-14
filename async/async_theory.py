import asyncio

import time


async def foo():
    print('One')
    # time.sleep(1)
    await asyncio.sleep(1)
    print('Twwo')


async def foo2():
    print('One222222')
    await asyncio.sleep(1)
    print('Twwo22222')


async def main():
    await asyncio.gather(foo(), foo2(), foo())


start = time.monotonic()
print(start)
asyncio.run(main())

asyncio.run(foo())
end = time.monotonic()
print(end)
print(__file__, end - start)
