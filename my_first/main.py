# def string1(string1) :
#     if len(string1) > 3 and str(string1).endswith("ing") :
#         print(string1 + "ly")
#     elif len(string1) > 3:
#         print(string1 + "ing")
#     else:
#         print(string1 + "erore")
# print(string1(str(input("text"))))
# ? -----------------------------------------------------------------------------------------------------------
# def replace_not_poor(string):
#     print(str(string).replace("не плохо","хорошо "))
# print(replace_not_poor(str(input("lorem"))))
# ? -----------------------------------------------------------------------------------------------------------
# def add_tags(tag, string):
#     match tag:
#         case "button":
#             print(f"<{tag}>{string}<{tag}/>")
#         case "input":
#             print(f"<{tag}type'{string}'{tag}/>")
#         case "h1":
#             print(f"<{tag}>{string}<{tag}/>")
#         case "p":
#             print(f"<{tag}>{string}<{tag}/>")
#         case "div":
#             print(f"<{tag}>{string}<{tag}/>")
#         case _:
#             return "error"
# print(add_tags(str(input("tag")),str(input("string"))))
# ? -----------------------------------------------------------------------------------------------------------
# def have(strong,number) :
#     text = str(strong).center(int(number) , " ")
#     print(text)
# print(have(str(input("text")), int(input())))
# ? -----------------------------------------------------------------------------------------------------------
# def insert_string_middle(string_to_insert, lenth): 
#     lenthe = len(string_to_insert) + int(lenth)
#     string_to_insert = str(string_to_insert)
#     lenthss = string_to_insert[-2::]
#     lenthss = string_to_insert.ljust(lenthe,f"{lenthss}")
#     print(lenthss)
# print(insert_string_middle(str(input("lorem")),input(int())))
# ? -----------------------------------------------------------------------------------------------------------
# def first_half_even(string):
#     if(len(string) % 3 == 0):
#        lens =  len(string) / 2 
#        lsnss = string[0:int(lens):]
#        lsnss2 = string[int(lens)::]
#        objects = print(lsnss + lsnss + lsnss + lsnss2)
#        print(objects)
#     else:
#         print("len > 2 string")
# print(first_half_even(str(input("text"))))
# ? -----------------------------------------------------------------------------------------------------------


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