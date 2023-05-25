

class Error(Exception):
    pass


class NumberSmallError(Error):
    pass


class NumberBigError(Error):
    pass


number = 10

while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise NumberSmallError
        elif i_num > number:
            raise NumberBigError
        break
    except NumberSmallError:
        print("NumberSmallError : This value is too small, try again!")
        print()
    except NumberBigError:
        print("This value is too large, try again!")
        print()
print("Congratulations! You guessed it correctly.")


class my_error(Exception):
    pass
def mul(a,b):
    if a == 0 or b ==0:
        raise my_error()
    else:
        print(a*b)

def main():
    try:

        a = int(input())
        b = int(input())
        mul(a,b)
    except:
        raise my_error("asddfasdfror")


main()

# class my_error(Exception):
#     pass
# def mul(a,b):
#     try:
#         if a == 0 or b ==0:
#             raise my_error()
#         else:
#             print(a*b)
#     except my_error:
#         print("asddfasdfror")
# def main():
#         a = int(input("a:"))
#         b = int(input("b:"))
#         mul(a,b)
# main()