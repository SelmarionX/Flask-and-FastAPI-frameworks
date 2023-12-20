import asyncio
import time
import random

# Создаем массив из 1000000 случайных чисел
arr = [random.randint(1, 100) for _ in range(1000000)]


# Функция для суммирования элементов массива
async def sum_array(start, end):
    return sum(arr[start:end])


# Засекаем время начала вычислений
start_time = time.time()

# Создаем цикл событий
loop = asyncio.get_event_loop()

# Запускаем функции в цикле событий
tasks = [sum_array(0, 500000), sum_array(500000, 1000000)]
results = loop.run_until_complete(asyncio.gather(*tasks))

# Выводим время выполнения вычислений
print("--- %s сек ---" % (time.time() - start_time))

# Выводим сумму элементов массива
print("Сумма: ", sum(results))
