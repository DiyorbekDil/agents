import asyncio

async def function_1():
    print("function 1 started")

    await asyncio.sleep(1)

    print("function 1 finished")


async def function_2():
    print("function 2 started")

    await asyncio.sleep(1)

    print("function 2 finished")


# results = await asyncio.gather(
#     function_1(),
#     function_2(),
# )
# 
# print(results)

# await function_1()
# await function_2()


async def main():
    await asyncio.gather(function_1(), function_2())

asyncio.run(main())