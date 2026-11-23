import asyncio
import time


async def deliver(order, seconds):
    print(f"{order}: გაიგზავნა")
    await asyncio.sleep(seconds)
    print(f"{order}: მიტანილია")


async def exercise_1():
    orders = [
        ("შეკვეთა #1", 1.0),
        ("შეკვეთა #2", 1.5),
        ("შეკვეთა #3", 2.0),
    ]

    start = time.perf_counter()
    for order, seconds in orders:
        await deliver(order, seconds)
    sequential_time = time.perf_counter() - start
    print(f"ზედიზედ: {sequential_time:.1f} წმ")

    start = time.perf_counter()
    await asyncio.gather(*(deliver(order, seconds) for order, seconds in orders))
    concurrent_time = time.perf_counter() - start
    print(f"ერთდროულად: {concurrent_time:.1f} წმ")
    print(f"დაჩქარება: {sequential_time / concurrent_time:.1f}x")

    # ერთდროული ლოდინები ერთმანეთს ემთხვევა, ამიტომ საერთო დრო დაახლოებით ყველაზე ხანგრძლივი შეკვეთის დროს უდრის.


async def square(number):
    await asyncio.sleep(1)
    return number * number


async def exercise_2():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]

    start = time.perf_counter()
    squares = await asyncio.gather(*(square(number) for number in numbers))
    elapsed = time.perf_counter() - start

    for number, result in zip(numbers, squares):
        print(f"{number}² = {result}")
    print(f"ჯამი: {sum(squares)}")
    print(f"დრო: {elapsed:.1f} წმ")

    # რვავე კორუტინა ერთდროულად ელოდება, ამიტომ მათი ერთწამიანი ლოდინები ერთმანეთს ემთხვევა.


async def load_user(user_id):
    await asyncio.sleep(1)  # შეცდომა 1: time.sleep ბლოკავდა event loop-ს; საჭიროა asyncio.sleep.
    return {"id": user_id, "name": f"მომხმარებელი {user_id}"}


async def exercise_3():
    # შეცდომა 2: load_user(...) კორუტინებს await უნდა; gather სამივეს ერთდროულად ასრულებს.
    start = time.perf_counter()
    users = await asyncio.gather(*(load_user(user_id) for user_id in (1, 2, 3)))
    print(users)
    print(f"დრო: {time.perf_counter() - start:.1f} წმ")


async def main():
    await exercise_1()
    print()
    await exercise_2()
    print()
    await exercise_3()


# საწყისი შეცდომიანი კოდი არაფერს ბეჭდავს და აჩვენებს RuntimeWarning-ს:
# "coroutine 'main' was never awaited". main() კორუტინა არ იყო გაშვებული.
if __name__ == "__main__":
    # შეცდომა 3: main() მარტო კორუტინას ქმნის; asyncio.run(main()) event loop-ს უშვებს.
    asyncio.run(main())
