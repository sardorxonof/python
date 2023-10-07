def piramid_recursion(n_times:int,number=0,number_2=0, number_3=0):
    """piramid_recursion"""
    if n_times % 2 == 0:
        number += 2
        lens = number * "*"
        number_2 = n_times - number_3
        if n_times == len(lens):
            print(number_2 * " " , lens , number_2 * " " )
        else:
            print(number_2 * " " , lens , number_2 * " " )
            piramid_recursion(n_times,number,number_2,number_3+1)
    else :
        number += 3
        lens = number * "*"
        number_2 = n_times - number_3
        if n_times == len(lens):
            print(number_2 * " " , lens , number_2 * " " )
        else:
            print(number_2 * " " , lens , number_2 * " " )
            piramid_recursion(n_times,number,number_2,number_3+1)

piramid_recursion(20)