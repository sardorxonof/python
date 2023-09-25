import math
import random
# ceil = input("rondom number ceil !")
# floor = input("rondom number floor !")
# rounds = input("rondom number rounds !")
# ------------------------------------------------------------------------------------------------------
# print(math.ceil(float(ceil)),  end=" в большую сторону " )
# print(math.floor(float(floor)), end=" в меньшую сторону ") 
# print(round(float(rounds)), end=" в ровную сторону ") 
# ------------------------------------------------------------------------------------------------------
# print(random.randrange(1,10))
# print(random.randint(1,10))
# print(round(random.random() * 10))
# ------------------------------------------------------------------------------------------------------

input("rondom two numbers")
one_number = int(input("one number"))
two_numbre = int(input("two number"))

numbers = random.randrange(one_number,two_numbre)
# if numbers == 9: 
#     print("first won" , numbers , end="!!!" , sep="_" )
# elif numbers == 5:
#     print("second won" , numbers , end="!!!" , sep="_" )
# else :
#     print("you not won")

print(numbers = random.randrange(one_number,two_numbre))