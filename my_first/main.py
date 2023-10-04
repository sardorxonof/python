def rotate_string_recursively(string ,number=1,number_9=0):
    print(string)
    string_3 = len(string) - int(number)
    string_2 = string[-1:]
    string_4 = string_2 + string[:string_3]
    string_4 = str(string_4)
    string_5 = len(string) - 1
    number_9 = string_5
    match number_9:
        case 0:
            print(string_4)
        case _ :
            rotate_string_recursively(string_4,number,number_9)
rotate_string_recursively("Hello world")

