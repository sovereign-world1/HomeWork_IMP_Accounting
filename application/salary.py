import numpy as np

def calculate_salary():
    # Запрос у пользователя ввода данных
    user_input = input("Введите зарплаты через пробел: ")
    
    # Преобразование введенных данных в список чисел
    try:
        arr = np.array(list(map(float, user_input.split())))
    except ValueError:
        print("Ошибка: Введите только числа, разделенные пробелами.")
        return
    
    # Проверка, что массив не пустой
    if len(arr) == 0:
        print("Ошибка: Вы не ввели никаких данных.")
        return
    
    # Вычисление среднего значения
    mean_value = np.mean(arr)
    print('Вычисление среднего значения ЗП:')
    print(mean_value)

calculate_salary()

    