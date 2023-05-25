def calculater1(value_1 ,oprater ,value_2):
    if oprater == '1':
        ans = (value_1) + value_2
        return f"{value_1} + {value_2} = {ans}"

    elif oprater == '2':
        ans = value_1 - value_2
        return f"{value_1} - {value_2} = {ans}"

    elif oprater == '3':
        ans = value_1 * value_2
        return f"{value_1} * {value_2} = {ans}"

    elif oprater == '4':
        ans = value_1 / value_2
        return f"{value_1} / {value_2} = {ans}"

    elif oprater == '5':
        ans = value_1 % value_2
        return f"{value_1} % {value_2} = {ans}"


def choise():
    print("=============================CALCULATER=============================")
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Modulus")
    global opr
    opr = input("Enter your choice : ")
    for i in range(2):
        if opr == "1" or opr == "2" or opr == "3" or opr == "4" or opr == "5":
            return opr
            break
        else:
            opr = input("Enter valid choice : ")
    else:
        exit()


def first_vaule():
    global value
    value = input("Enter first Value : ")
    for i in range(2):
        if value.isdigit() == True:
            value = float(value)
            return value
            break
        else:
            value = input('Enter valid first Value : ')
            if value.isdigit() == True:
                value = float(value)
                break
    else:
        exit()

def second_vaule():
    global value2
    value2 = input("Enter second Value : ")
    for i in range(2):
        if value2.isdigit() == True:
            value2 = float(value2)
            return value2
            break
        else:
            value2 = input('Enter valid second Value : ')
            if value2.isdigit() == True:
                value2 = float(value2)
                break
    else:
        exit()


def exit_program():
    exit1 = input("do you want exit ? (y/n) : ")
    if exit1 == "y":
        print("Thank You!")
        exit()

