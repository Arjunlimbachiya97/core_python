def separate():
    valu = input("Enter value separate by comma :")
    list_1 = valu.split(",")
    list_2 = [float(i) for i in list_1]
    return list_2

def addition(list_2):
    ans = list_2[0]
    for i in list_2[1:]:
        ans += i
    return ans

def subtrection(list_2):
    ans = list_2[0]
    for j in list_2[1:]:
            ans -= j
    return ans

def multiplicatin(list_2):
    ans = list_2[0]
    for i in list_2[1:]:
        ans *= i
    return ans

def division(list_2):
    ans = list_2[0]
    for i in list_2[1:]:
        if i == 0:
            print("Value not divide by zero")
            break
        else:
            ans /= i
    return ans

def modulus(list_2):
    ans = list_2[0]
    for i in list_2[1:]:
        ans %= i
    return ans

# list =  separate()
# print(addition())
# print(subtrection(list))
# multiplicatin()
# division()
