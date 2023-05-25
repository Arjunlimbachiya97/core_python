# # dect = {"Name":"Arjun","Roll no": 19}
# # a = (dect.items())
# # print(a)
# # for i in a:
# #     print(i)
# #
# # b = str(dect)
# # print(type(b))
# # print(b[0])
#
# class PowTwo:
#     """Class to implement an iterator
#     of powers of two"""
#
#     def __init__(self, max=0):
#         self.max = max
#
#     def __iter__(self):
#         self.n = 0
#         return self
#
#     def __next__(self):
#         if self.n <= self.max:
#             result = 2 ** self.n
#             self.n += 1
#             return result
#         else:
#             raise StopIteration
#
#
# # create an object
# numbers = PowTwo(3)
#
# # create an iterable from the object
# i = iter(numbers)
# print(i)
# for j in i:
#     print(j)
# # Using next to get to the next iterator element
# # print(next(i)) # prints 1
# # print(next(i)) # prints 2
# # print(next(i)) # prints 4
# # print(next(i)) # prints 8
# # print(next(i)) # raises StopIteration exception

# define Python user-defined exceptions
# class InvalidAgeException(Exception):
#     'Raised when the input value is less than 18'
#     pass


# you need to guess this number
# number = 18
#
# try:
#     input_num = int(input("Enter a number: "))
#     if input_num < number:
#         raise ValueError("not")
#     else:
#         print("Eligible to Vote")
#
# except ValueError:
#     print("Exception occurred: Invalid Age")
#
# abc = {"a":{1:11,2:22,3:33,4:43,5:53,}}
# # print(abc["a"])
#
# for i in abc:
#     for j in abc[i]:
#         print(abc[i][j])
        # print(i[j])