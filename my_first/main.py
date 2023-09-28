#?# import math
#?# import random
#?# ceil = input("rondom number ceil !")
#?# floor = input("rondom number floor !")
#?# rounds = input("rondom number rounds !")
#?# ------------------------------------------------------------------------------------------------------
#?# print(math.ceil(float(ceil)),  end=" в большую сторону " )
#?# print(math.floor(float(floor)), end=" в меньшую сторону ") 
#?# print(round(float(rounds)), end=" в ровную сторону ") 
#?# ------------------------------------------------------------------------------------------------------
#?# print(random.randrange(1,10))
#?# print(random.randint(1,10))
#?# print(round(random.random() * 10))
#?# ------------------------------------------------------------------------------------------------------

# # input("rondom two numbers")
# # one_number = int(input("one number"))
# # two_numbre = int(input("two number"))

# # numbers = random.randrange(one_number,two_numbre)
# # if numbers == 9: 
# #     print("first won" , numbers , end="!!!" , sep="_" )
# # elif numbers == 5:
# #     print("second won" , numbers , end="!!!" , sep="_" )
# # else :
# #     print("you not won")

# # print(numbers = random.randrange(one_number,two_numbre))

# # lorem = input("lorem")

# # # print(len(lorem))
# # sardor = ["sardor",'help']
# # match sardor:
# #     case ["sardor",("sardor" | "help" | "rodras")]:
# #         print("""lorem is lorem """)
# #     case _:
# #?         print("""lorem is not lorem """)

# ! lorem = int(input())
# ! match lorem:
# !    case lorem if lorem == 10:
# !        print("lorem is lorem ")
# ?    case lorem if lorem == 1:
# ?       print(1+2)
# ?    case _:
# ?        print("error lorem" )

# lower()          Converts a string into lower case
#               RU: преобразует строку в нижний регистр
# print("HELLO WORLD".lower())  # hello world
# ===================================
# casefold()      Converts string into lower case
#               RU: преобразует строку в нижний регистр
# print('Hello WORLD'.casefold())  # hello world
# The main difference is casefold() is stronger than lower() method,
# it converts more characters into lower case
# RU: Основное отличие в том, что метод casefold() сильнее, чем метод lower(),
# он преобразует больше символов в нижний регистр
# ===================================
# isupper()          Returns True if all characters in the string are upper case
#               RU: Возвращает True, если все символы в строке в верхнем регистре
# print("HELLO WORLD".isupper())  # True
# ===================================
# islower()          Returns True if all characters in the string are lower case
#               RU: Возвращает True, если все символы в строке в нижнем регистре
# print("HELLO WORLD".islower())  # False
# ===================================
# center()          Returns a centered string
#               RU: Возвращает центрированную строку
# print("Testing center".center(30, "*"))  # False
# ********Testing center********
# ===================================
# count()          Returns the number of times a specified value occurs in a string
#               RU: Возвращает количество раз, когда в строке встречается указанное значение
# print("Test text for checking the count() method".count("t"))  # 6


# print("Test text for checking the count() method".count("text"))  # 1
# ===================================
# endswith()      Returns true if the string ends with the specified value
#               RU: Возвращает true, если строка заканчивается указанным значением
# print("Test text".endswith("text"))  # True
# print("Test text".endswith("www"))   # False
# ===================================
# startswith()      Returns true if the string starts with the specified value
#               RU: Возвращает true, если строка начинается с указанного значения
# print("Test text".startswith("Test"))  # True
# print("Test text".startswith("www"))   # False
# ===================================
# expandtabs()      Sets the tab size of the string  (EX:  "H\te\tl\tl\to" ==>  "H    e    l    l    o")
#               RU: Устанавливает размер табуляции строки
# test_text = "H\tello w\torl\td"
# print(test_text.expandtabs(1))  # H ello w orl d
# print(test_text.expandtabs(5))  # H    ello w     orl  d
# ===================================
# find()          Searches the string for a specified value and returns the position of where it was found (==> .indexOf())
#               RU: Ищет строку для указанного значения и возвращает позицию, где оно было найдено
# test_text = "This is test text for checking the find() method"
# print(test_text.find("test"))  # 8
# print(test_text.find("www"))   # -1
# ===================================
# rfind()          Searches the string for a specified value and returns the last position of where it was found  (==> .lastIndexOf()
#               RU: Ищет строку для указанного значения и возвращает последнюю позицию, где оно было найдено
# test_text = "This is test text for checking test the find() method"
# print(test_text.rfind("test"))  # 31
# print(test_text.rfind("www"))  # -1
# ===================================
# index()          Searches the string for a specified value and returns the position of where it was found (==> .indexOf())
#               RU: Ищет строку для указанного значения и возвращает позицию, где оно было найдено
# test_text = "This is test text for checking test the find() method"
# print(test_text.index("www"))  # raises ValueError
# ===================================
# rindex()          Searches the string for a specified value and returns the
#                   last position of where it was found (==> lastIndexOf in JS)
#               RU: Ищет строку для указанного значения и возвращает последнюю позицию, где оно было найдено
# ===================================
# swapcase()      Swaps cases, lower case becomes upper case and vice versa
#               RU: Меняет регистр, нижний регистр становится верхним и наоборот
# test_text = "HeLLo world"
# print(test_text.swapcase())  # hEllO WORLD
# ===================================
# format()          Formats specified values in a string
#               RU: Форматирует указанные значения в строке
# x = "Updated"
# z1 = "Test text for {var} checking .format()".format(var=x)
# z2 = f"Test text for {x} checking .format()"
# print(z1)
# print(z2)
# ===================================
# isalnum()          Returns True if all characters in the string are alphanumeric
#               RU: Возвращает True, если все символы в строке являются буквенно-цифровыми
# x = "Hello777"
# print(x.isalnum())  # True
# ===================================
# isalpha()       Returns True if all characters in the string are in the alphabet
#               RU: Возвращает True, если все символы в строке находятся в алфавите
# x = "Hello"
# print(x.isalpha()) # True
# x = 777
# print(x.isalpha()) # False
# ===================================
# isdecimal()      Returns True if all characters in the string are decimals
# ==             RU: Возвращает True, если все символы в строке являются десятичными
# isdigit()       Returns True if all characters in the string are digits
# ==             RU: Возвращает True, если все символы в строке являются цифрами
# isnumeric()      Returns True if all characters in the string are numeric


#               RU: Возвращает True, если все символы в строке являются числовыми
# x = "123"
# print(x.isnumeric())  # True
# print(x.isdigit())    # True
# print(x.isdecimal())  # True
# ===================================
# isspace()          Returns True if all characters in the string are whitespaces
#               RU: Возвращает True, если все символы в строке являются пробелами
# x = "   "
# print(x.isspace())  # True
# ===================================
# join()          Joins the elements of an iterable to the end of the string
#               RU: Объединяет элементы итерируемого объекта в конец строки
# x = ["Text 1", "Text 2", "Text 3"]
# print("|".join(x))  # Text 1|Text 2|Text 3
# print("".join(x))   # Text 1Text 2Text 3
# print(" ".join(x))   # Text 1 Text 2 Text 3
# ===================================
# ljust()          Returns a left justified version of the string  (==> padStart in JS)
#               RU: Возвращает левую версию строки
# rjust()          Returns a right justified version of the string (==> padEnd in JS)
#               RU: Возвращает правую версию строки
# test_txt = "Hello"
# print(test_txt.ljust(20, "*"))
# print(test_txt.rjust(20, "*"))
# ===================================
# strip()          Returns a trimmed version of the string         (==> trim in JS)
#              RU: Возвращает усеченную версию строки
# x = "   Hello world   "
# print(x.strip())  # "Hello world"
# ===================================
# replace()          Returns a string where a specified value is replaced with a specified value
#              RU: Возвращает строку, в которой указанное значение заменяется на указанное значение
# ===================================
# split()          Splits the string at the specified separator, and returns a list
#              RU: Разделяет строку по указанному разделителю и возвращает список
# x = "Text 1, Text 2, Text 3"
# print(x.split(","))  # ['Text 1', ' Text 2', ' Text 3']

# If we want to split by letters, we can use list()
# x = list(x)
# print(x)
# ===================================
# rsplit(maxsplit)Splits the string at the specified separator, and returns a list
#              RU: Разделяет строку по указанному разделителю и возвращает список
# x = "Text 1, Text 2, Text 3"
# x = x.rsplit(" ")
# print(x)
# print(x) # ["Text 1, Text 2", " Text 3"]

# x.rsplit(" ", 2)  => ['Text 1, Text 2,', 'Text', '3']
# x.rsplit(" ")  => ['Text', '1,', 'Text', '2,', 'Text', '3']
# ===================================
# list()           For splitting string-letters into list
#              RU: Для разделения букв строки на списке
#   EX: list('Hello') ==> ['H', 'e', 'l', 'l', 'o']
# x = "Text 1, Text 2, Text 3"
# print(list(x))
# ===================================
# splitlines()     Splits the string at line breaks and returns a list
#              RU: Разделяет строку по переводам строк и возвращает список
# x = "This is \n test \n text"
# print(x)
# print(x.splitlines())
# ===================================
# zfill()          Fills the string with a specified number of 0 values at the beginning
#              RU: Заполняет строку указанным количеством значений 0 в начале
# x = "Hello"
# print(x.zfill(10))  # 00000Hello
# ===================================
# 'Hello'[::-1]    Reverses a string
#              RU: Переворачивает строку


# # 9. Write a Python program to get a string made of the first 2 and last 2 characters of a given string.
# # If the string length is less than 2, return the empty string instead.
# # RU: Напишите программу на Python, чтобы получить строку,
# # состоящую из первых 2 и последних 2 символов заданной строки.
# # Если длина строки меньше 2, вместо этого верните пустую строку.
# def first_last_two(string):  # первые_2_последние_2
#     return string[:2] + string[-2:]


# # 10. Write a Python program to get a string from a given string where all occurrences of its first char
# # have been changed to '$', except the first char itself.
# # RU: Напишите программу на Python, чтобы получить строку из заданной строки,
# # где все вхождения ее первого символа были заменены на '$',
# # кроме самого первого символа.

#? # INPUT:   =>  "This is test text"
#? # OUTPUT:  =>  "This is $es$ $ex$"
#? # изменить_первый_символ
#? def change_first_char(str, symbol="$"):
#?     first = str[0]
#?     str = str.lower()
#?     str = str.replace(first.lower(), symbol)
#?     return first + str[1:]
#? print(change_first_char("Hello hhhh hello"))



# def swap_first_two(string1, string2):  # поменять_первые_два
# # 12. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string
# # already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
# # RU: Напишите программу на Python, чтобы добавить 'ing' в конец заданной строки (длина должна быть не менее 3).
# # Если заданная строка уже заканчивается на 'ing', вместо этого добавьте 'ly'.
# # Если длина строки заданной строки меньше 3, оставьте ее без изменений.
# def add_ing(string):  # добавить_ing
# # 13. Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string.
# # If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
# # RU: Напишите программу на Python, чтобы найти первое появление подстрок «не» и «плохо» в заданной строке.
# # Если «не» следует за «плохо», замените всю подстроку «не» ... «плохо» на «хорошо». Вернуть полученную строку.
# def replace_not_poor(string):  # заменить_не_плохо
# # 14. Write a Python function to create an HTML string with tags around the word(s)
# # RU: Напишите функцию Python для создания HTML-строки с тегами вокруг слова (слов).
# def add_tags(tag, string):  # добавить_теги
# # 15. Write a Python function to insert a string in the middle of a string.
# # RU: Напишите функцию Python для вставки строки посередине строки.
# # вставить_строку_посередине


# def insert_string_middle(string, string_to_insert):
# # 16. Write a Python function to get a string made of 4 copies of the last two characters of a specified string
# # RU: Напишите функцию Python, чтобы получить строку, состоящую из 4 копий последних двух символов заданной строки
# def last_two(string):  # последние_два
# # 17. Write a Python function to get a string made of the first three characters of a specified string.
# # If the length of the string is less than 3, return the original string.
# # RU: Напишите функцию Python, чтобы получить строку, состоящую из первых трех символов заданной строки.
# # Если длина строки меньше 3, вернуть исходную строку.
# def first_three(string):  # первые_три
# # 18. Write a Python function to get the first half of a specified string of even length.
# # RU: Напишите функцию Python, чтобы получить первую половину заданной строки четной длины.
# def first_half_even(string):  # первая_половина_четная

# # 19. Write a Python program to concatenate two strings and return the result.
# # If the length of the strings are not same then remove the characters from the longer string.
# # RU: Напишите программу на Python для объединения двух строк и верните результат. Если длины строк не одинаковы,
# # то удалите символы из более длинной строки.


# def concat_strings(string1, string2):  # объединить_строки


# # 20. Write a Python function to convert a given string to all uppercase if it contains
# # at least 2 uppercase characters in the first 4 characters.
# # RU: Напишите функцию Python для преобразования заданной строки в верхний регистр, если она содержит
# # не менее 2 заглавных символов в первых 4 символах.
# def convert_upper(string):  # преобразовать_в_верхний_регистр
#     if sum(1 for char in string[:4] if char.isupper()) >= 2:
# # 21. Write a Python program to remove a newline in Python.
# # RU: Напишите программу на Python, чтобы удалить перевод строки в Python.
# def remove_newline(string):  # удалить_перевод_строки
# # 22. Write a Python program to remove existing indentation from all of the lines in a given text.
# # RU: Напишите программу на Python для удаления существующего отступа из всех строк в заданном тексте.
# def remove_indentation(string):  # удалить_отступ
# # 23. Write a Python program to count and display the vowels of a given text.
# # RU: Напишите программу Python, чтобы подсчитать и отобразить гласные заданного текста.
# def count_vowels(string):  # подсчитать_гласные
# # 24. Swapkeys
# def swap_cases(string):  # поменять_регистр
# # 25. Write a function in Python to check duplicate letters.
# # It must accept a string, i.e., a sentence. The function should return
# # True if the sentence has any word with duplicate letters, else return False.
# # RU: Напишите функцию на Python для проверки повторяющихся букв.
# # Он должен принимать строку, то есть предложение. Функция должна возвращать
# # True, если в предложении есть слово с повторяющимися буквами, иначе возвращать False.
# # проверить_повторяющиеся_буквы
# def check_duplicate_letters(string) -> bool:
# # 26. Write a function that takes a sentence as argument, then takes last word's first letter and
# # repeats 5 times in the beginning of the sentence and at the end.
# # RU: Напишите функцию, которая принимает предложение в качестве аргумента, затем берет первую букву
# # последнего слова и повторяет 5 раз в начале предложения и в конце.


# def repeat_first_l_of_last_word(sentence):
# # 26. Write a code in Python to create a Morse code translator.
# # You can take a string with alphanumeric characters in lower or upper case.
# # The string can also have any special characters as a part of the Morse code.
# # Special characters can include commas, colons, apostrophes, exclamation marks,
# # periods, and question marks. The code should return the Morse code that is equivalent to the string.


# def morse_code(string):
# # 27. Write a function to detect 13th Friday. The function can accept two parameters,
# # and both will be numbers. The first parameter will be the number indicating the month,
# # and the second will be the year in four digits. Your function should parse the parameters,
# # and it must return True when the month contains a Friday with the 13th, else return False.
# def detect_13th_friday(month, year):
# # 28. Write a function to find the domain name from the IP address. The function will accept an
# # IP address, make a DNS request, and return the domain name that maps to that IP address while
# # using records of PTR DNS. You can import the Python socket library.

# def find_domain_name(ip_address):
# # 29. Write a function in Python to convert a decimal to a hex. It must accept a string of ASCII
# # characters as input. The function should return the value of each character as a hexadecimal string.
# # You have to separate each byte by a space and return all alpha hexadecimal characters as lowercase.



# def convert_to_hex(string):
# # 30. Write a function in Python to parse a string such that it accepts a parameter- an encoded string.
# # This encoded string will contain a first name, last name, and an id. You can separate the values
# # in the string by any number of zeros. The id will not contain any zeros. The function should return
# # a Python dictionary with the first name, last name, and id values. For example, if the input would
# # be "John000Doe000123". Then the function should return:
# # { "first_name": "John", "last_name": "Doe", "id": "123" }


# def encoded_string(string):
# # 31. Write a code in Python to find out whether a given string S is a valid regex or not.


# def is_valid_regex(string):
# # 32. Create a function that takes a text and repeats the middle
# # letter three times
# # RU: Создайте функцию, которая принимает текст и повторяет
# # среднюю букву три раза
# # Welcome   =>   Welcccome


# def repeat_middle(sentence):
# # 33. Create a function that repeats first and last half of the text n times
# # RU: Создайте функцию, которая повторяет первую и вторую половину текста n раз
# # "Welcome"  =>  "WelWelWelcomecomecomecome"


# def repeat_half_n_times(sentence, n):

# ? !  ----------------------------------------------------------------------------------------------------------------------

# x = []

# def test(arg: int) -> None:
#     arg =+ 2 
#     x.append(arg)
    
# def test3(arg: int , arg2: int) -> int:
#     return arg + arg2
 
# def stard(arg):
#     print("*" * arg)
#     if arg > 1:
#         return stard(arg - 2)
    
# print(stard(10))
def factarial(arg):
    print(arg)
    if arg == 1:
        return 1 
    else:
        print()
factarial(10)