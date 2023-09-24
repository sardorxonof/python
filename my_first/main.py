# input("2 numbers one oper")
# create1 = int(input("first")) 
# create2 = int(input("second"))
# create3 = str(input("operator")
# resalt = 0
# if create3 == " +" :
#     resalt = create1 + create2
# elif create3 == " -":
#     resalt = create1 - create2
# elif create3 == " *":
#     resalt = create1 * create2
# elif create3 == " /":
#     resalt = create1 / create2
# else : 
#     print("error")
# print("this is answer"  , resalt ) 
# print(float(create1)) => показиваеть дроб 
# global => работает как var делаеть глобално можно будить использовать 


# --------------------------------------------------------------------------------------------------------------------------------------------------
import math
import random

# math.ceil    => 3.01 => 4
# math.floor() => 3.99 => 3
# round()      => 3.5  => 4   => is used to round the number by
#                               deleting the decimal part if it is
#                               less than 5
#                       2nd param => number of digits after the decimal point
#                       RU: используется для округления числа путем
#                           удаления десятичной части, если она меньше 5
#                       2-й параметр => количество цифр после десятичной точки
# ----------------------------------------------------------------------
# import random
# ----------------------------------------------------------------------
# random.randrange(.., ..?) # gives random number between start and end numbers
#            RU: дает случайное число между начальным и конечным числами
# ex:  random.randrange(0, 10, step=2)  # 0, 2, 4, 6, 8
# ----------------------------------------------------------------------
# random.randint(.., ..)   # gives random number between start and end numbers
#            RU: дает случайное число между начальным и конечным числами
# ex: random.randint(0, 10)  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# ----------------------------------------------------------------------
# random.random()    # gives random float number between 0 and 1
#            RU: дает случайное число с плавающей запятой между 0 и 1
# ex: round(random.random() * 100, 2)
# ----------------------------------------------------------------------

# int       => 1, 2, 3
# float     => 1.0, 2.0, 3.0
# complex() => 1j


# ----------------------------------------------------------------------

# FIND PERCENTAGE

# (60 / 100) * 17  # 10.2
# 60 * 0.17        # 10.2


# ----------------------------------------------------------------------


# +      Addition      x + y
# -      Subtraction      x - y
# *      Multiplication  x * y
# /      Division      x / y
# %      Modulus          x % y     =>    10 % 3  =>  1
# **  Exponentiation  x ** y     =>    2 * 2 * 2 * 2   =   2**4   => 16
#! //  Floor division  x // y     =>    x // 2   => 3.5 => 3
# 5 // 2  # =>  2.5  =>  2
# 15 // 2  # => 7.5  =>  7
#! -------------------------------------------------

x = 2
x += 2

# =       x = 5       x = 5
# +=   x += 3       x = x + 3
# -=   x -= 3       x = x - 3
# *=   x *= 3       x = x * 3
# /=   x /= 3       x = x / 3
# %=   x %= 3       x = x % 3
# **=   x **= 3   x = x ** 3
#! //=   x //= 3   x = x // 3

# ----------------------------------------------------------------------
# x = {}
# y = {}
# print(x is y)

# ==  Equal          x == y    =>  Равно
# !=  Not equal      x != y    =>  Не равно
# >      Greater than  x > y    =>  Больше
# <      Less than      x < y    =>  Меньше
# >=  Greater than or equal to  x >= y    =>  Больше или равно
# <=  Less than or equal to      x <= y    =>  Меньше или равно

# ----------------------------------------------------------------------

# and   Returns True if both statements are true      x < 5 and  x < 10
#     RU: Возвращает True, если оба выражения истинны
# or  Returns True if one of the statements is true  x < 5 or x < 4
#     RU: Возвращает True, если одно из выражений истинно
# not  Reverse the result, returns False if the result is true  not(x < 5 and x < 10
#     RU: Инвертирует результат, возвращает False, если результат истинен

# ----------------------------------------------------------------------
# x = {"x": 1}
# print(x is {"x": 1})
# --------------------
# is       Returns True if both variables are the same object
#       RU: Возвращает True, если обе переменные являются одним и тем же объектом
# ex:   x is y

# is not  Returns True if both variables are not the same object
# ex:   x is not y
#       RU: Возвращает True, если обе переменные не являются одним и тем же объектом

# ----------------------------------------------------------------------



# 'Hello world'.includes("Bemiyya")  # False
# "Bemiyya" in 'Hello world'  # False
# "Hello" in 'Hello world'    # True
# "o" in 'Hello world'        # True
# "y" not in 'Hello world'    # True

# in       Returns True if a sequence with the specified value is
#           present in the object
#       RU: Возвращает True, если последовательность с указанным значением
#           присутствует в объекте
# ex:    x in y

# not in  Returns True if a sequence with the specified value is
#           not present in the object
#       RU: Возвращает True, если последовательность с указанным значением
#           отсутствует в объекте
# ex:    x not in y


# ----------------------------------------------------------------------
#!     *args  => is used receive an arbitrary number of arguments
#  RU: используется для получения произвольного количества аргументов

def sum(*args) -> int:
    """
    This function returns sum of two or more numbers
    RU: Эта функция возвращает сумму двух или более чисел
    """
    result = 0
    # for (let item of []) {...}   =>  in JS
    for num in args:  # arguments
        result += num
    return result


print(sum(1, 2, 3, 4, 5))
# ----------------------------------------------------------------------
# In Java Script
# -------------
# function test(...rest) {
#     let result = 0
#     for (let num of rest) {
#         result += num
#     }
#     return result
# }
# test(1, 2, 3, 4, 5, ...)