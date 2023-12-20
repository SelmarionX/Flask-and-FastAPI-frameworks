import threading
import time
import random

# Создаем массив из 1000000 случайных чисел
arr = [random.randint(1, 100) for _ in range(1000000)]


# Функция для суммирования элементов массива
def sum_array(start, end, result1):
    result1[0] += sum(arr[start:end])


# Засекаем время начала вычислений
start_time = time.time()

# Создаем список для хранения результата
result = [0]

# Создаем два потока
t1 = threading.Thread(target=sum_array, args=(0, 500000, result))
t2 = threading.Thread(target=sum_array, args=(500000, 1000000, result))

# Запускаем потоки
t1.start()
t2.start()

# Ждем завершения потоков
t1.join()
t2.join()

# Выводим время выполнения вычислений
print("--- %s сек. ---" % (time.time() - start_time))

# Выводим сумму элементов массива
print("Сумма: ", result[0])
