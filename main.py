"""
 _____         _      __  
|_   _|       | |    /  | 
  | | __ _ ___| | __ `| | 
  | |/ _` / __| |/ /  | | 
  | | (_| \__ \   <  _| |_
  \_/\__,_|___/_|\_\ \___/

Напишите программу, которая выводит в консоль "Hello world"

hint: что такое print?
"""
#
print("Hello world!")
#
"""
 _____         _      _____ 
|_   _|       | |    / __  \
  | | __ _ ___| | __ `' / /'
  | |/ _` / __| |/ /   / /  
  | | (_| \__ \   <  ./ /___
  \_/\__,_|___/_|\_\ \_____/

Напишите программу, которая выводит числа от 1 до введенного пользователем. Для чисел, кратных 3, выводится "Fizz",'
для кратных 5 — "Buzz", а для чисел, кратных 3 и 5 — "FizzBuzz"

hint: цикл, если и "%"
 """
#
n = int(input("Введите число: "))
for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
#

"""
 _____         _      _____ 
|_   _|       | |    |____ |
  | | __ _ ___| | __     / /
  | |/ _` / __| |/ /     \ \
  | | (_| \__ \   <  .___/ /
  \_/\__,_|___/_|\_\ \____/ 

Напишите программу, которая проверяет, является ли введенный пользователем год високосным

hint: https://ru.wikihow.com/%D0%B2%D1%8B%D1%81%D1%87%D0%B8%D1%82%D1%8B%D0%B2%D0%B0%D1%82%D1%8C-%D0%B2%D0%B8%D1%81%D0%BE%D0%BA%D0%BE%D1%81%D0%BD%D1%8B%D0%B5-%D0%B3%D0%BE%D0%B4%D1%8B
"""
#
year = int(input("Введите год: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} является високосным годом.")
else:
    print(f"{year} не является високосным годом.")
#

"""
 _____         _        ___ 
|_   _|       | |      /   |
  | | __ _ ___| | __  / /| |
  | |/ _` / __| |/ / / /_| |
  | | (_| \__ \   <  \___  |
  \_/\__,_|___/_|\_\     |_/

Напишите программау, которая проверяет, является ли введенная пользователем строка или число палиндромом, то есть читается ли оно одинаково с обеих сторон

hint: https://letpy.com/handbook/builtins/reversed/
"""
#
def is_palindrome(s):
    cleaned = ''.join(s.split()).lower()
    return cleaned == cleaned[::-1]
user_input = input("Введите строку или число: ")
if is_palindrome(user_input):
    print(f"{user_input} является палиндромом.")
else:
    print(f"{user_input} не является палиндромом.")
#
"""
 _____         _      _____ 
|_   _|       | |    |  ___|
  | | __ _ ___| | __ |___ \ 
  | |/ _` / __| |/ /     \ \
  | | (_| \__ \   <  /\__/ /
  \_/\__,_|___/_|\_\ \____/ 

Напишите программу, которая запрашивает число у пользователя и вычисляет факториал заданного числа, используя цикл или рекурсию

hint: https://ru.wikipedia.org/wiki/%D0%A4%D0%B0%D0%BA%D1%82%D0%BE%D1%80%D0%B8%D0%B0%D0%BB
"""

#
def factorial_recursive(n):
    if n < 0:
        return None  
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)
user_input = int(input("Введите число для вычисления факториала: "))
factorial_result = factorial_recursive(user_input)
if factorial_result is not None:
   print(f"Факториал числа {user_input} равен {factorial_result}.")
else:
    print("Факториал отрицательного числа не определен.")
#
"""
 _____         _       ____ 
|_   _|       | |     / ___|
  | | __ _ ___| | __ / /___ 
  | |/ _` / __| |/ / | ___ \
  | | (_| \__ \   <  | \_/ |
  \_/\__,_|___/_|\_\ \_____/

Напишите программу, которая проверяет, является ли число простым (делится только на 1 и само на себя). Используйте перебор делителей.

hint: x <= 1 - не простые числа
hint 2: %
"""
#
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:  
            return False  
    return True  
user_input = int(input("Введите число для проверки на простоту: "))
if is_prime(user_input):
    print(f"Число {user_input} является простым.")
else:
    print(f"Число {user_input} не является простым.")
#

"""
 _____         _      ______
|_   _|       | |    |___  /
  | | __ _ ___| | __    / / 
  | |/ _` / __| |/ /   / /  
  | | (_| \__ \   <  ./ /   
  \_/\__,_|___/_|\_\ \_/    

Напишите программу, которая находит сумму всех цифр числа

hint: циклы
"""
#
def sum_of_digits(number):
    total = 0
    number = abs(number)
    while number > 0:
        digit = number % 10  
        total += digit       
        number //= 10       
    return total
user_input = int(input("Введите число: "))
result = sum_of_digits(user_input)
print("Сумма всех цифр числа:", result)
#
"""
 _____         _      _____ 
|_   _|       | |    |  _  |
  | | __ _ ___| | __  \ V / 
  | |/ _` / __| |/ /  / _ \ 
  | | (_| \__ \   <  | |_| |
  \_/\__,_|___/_|\_\ \_____/

Напишите программу, которая генерирует последовательность Фибоначчи до указанного числа или количества элементов

hint: 1, 1, 2, 3 https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%B0_%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8
hint 2: попробуйте решить с помощью рекурсии
"""
#
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        seq = fibonacci(n - 1)
        seq.append(seq[-1] + seq[-2])
        return seq
def fibonacci_until(limit):
    seq = []
    a, b = 0, 1
    while a <= limit:
        seq.append(a)
        a, b = b, a + b
    return seq
choice = input("Хотите ввести (1) лимит или (2) количество элементов? (введите 1 или 2): ")
if choice == '1':
    limit = int(input("Введите лимит: "))
    result = fibonacci_until(limit)
elif choice == '2':
    count = int(input("Введите количество элементов: "))
    result = fibonacci(count)
else:
    print("Некорректный выбор.")
    result = []
print("Последовательность Фибоначчи:", result)
#



