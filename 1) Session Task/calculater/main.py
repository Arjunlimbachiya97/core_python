from calculater.calculater_functions import *

def main():
    while  True:
        opr = choise()
        value = first_vaule()
        value2 = second_vaule()
        print(calculater1(value_1= value ,oprater=opr ,value_2=value2))
        exit_program()

main()