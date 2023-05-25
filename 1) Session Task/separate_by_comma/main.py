from calculater.calculater_functions import *
from separate_by_comma.comma_seprate_functions import *

while True:
    option = choise()
    list =  separate()
    if option == "1":
        print(addition(list))
    elif option == "2":
        print(subtrection(list))
    elif option == "3":
        print(multiplicatin(list))
    elif option == "4":
        print(division(list))
    elif option == "5":
        print(modulus(list))
    exit_program()