import multiprocessing
import time
import random

# Создаем массив из 1000000 случайных чисел
arr = [random.randint(1, 100) for _ in range(1000000)]


# Функция для суммирования элементов массива
def sum_array(start, end):
    return sum(arr[start:end])


# Засекаем время начала вычислений
start_time = time.time()

# Создаем два процесса
p1 = multiprocessing.Process(target=sum_array, args=(0, 500000))
p2 = multiprocessing.Process(target=sum_array, args=(500000, 1000000))

# Запускаем процессы
p1.start()
p2.start()

# Ждем завершения процессов
p1.join()
p2.join()

# Выводим время выполнения вычислений
print("--- %s сек. ---" % (time.time() - start_time))

# Выводим сумму элементов массива
print("Сумма: ", sum_array(0, 1000000))
