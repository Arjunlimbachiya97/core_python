# Function
# Type of function
#   1) Inbuilt function
#   2) Use define function

# 2) User define function
print("============================ 1) Required arguments:==========================================")
def fn1(a):
    print(a)

fn1("Hello World")


print("============================ 2) Keyword arguments:===========================================")
def fn2(str,name):
    print(str,name)

fn2(str=10,name = "Arjun")


print("============================ 3) Default arguments:===========================================")
def fn3(name, marks=35):
    print("Name=", name)
    print("Marks=", marks)

fn3(marks=50, name="XYZ")
fn3(name="ABC")


print("============================ 4) Variable-length arguments / Arbitrary Arguments, *args===========================================")
def fn4(*tuplevar):
    print(type(tuplevar))
    print(tuplevar)
    print(tuplevar[0])

fn4(50)
# Output:50
fn4("string", 70, "Hello", "disha", "rushika", "smit",70)


print("============================ 5) Dictionary arguments / Arbitrary Keyword Arguments, **kwargs===========================================")
def fn5(**std):
    print(std)
    print(type(std))
    print(std.items())
    if std is not None:
        for key, value in std.items():
            print("%s = %s" % (key, value))

fn5(fn='Abc', ln='Def', name="Yash", demo="Hemil")

fun = ([("arjun","limbachiya","A"),("ronak","shah","k")])
for i,j,k in fun:
    print(i,j,k)


print("============================ Recursion===========================================")
def recursion(n):
    if n == 1:
        return 1
    else:
        return n * recursion(n - 1)
n = 5
print(recursion(n))

print("============================ Lambda_Anonymous Function===========================")
print("Lambda_Anonymous Function")
lamb1 = lambda x : x*x
print(lamb1(10))

lamb2 = lambda x,y : x + y
print(lamb2(10,50))

old_list = [10, 11, 20, 21, 30, 31, 40, 41, 50]

newlist = list(map(lambda x : x * x ,old_list))
print(newlist)

newtuple = tuple(map(lambda x : x * x ,old_list))
print(newtuple)

newset = set(map(lambda x : x * x ,old_list))
print(newset)

# newdict = dict(map(lambda x : x * x ,old_list))
# print(newdict)

f_newlist = list(filter(lambda x : (x % 2 == 0), old_list))
print(f_newlist)

f_newtuple = tuple(filter(lambda x : (x % 2 == 0), old_list))
print(f_newtuple)

f_newset = set(filter(lambda x : (x % 2 == 0), old_list))
print(f_newset)

f_newtuple = tuple(filter(lambda x : (x % 2 == 0), old_list))
print(f_newtuple)

# f_newdict = dict(filter(lambda x : (x % 2 == 0), old_list))
# print(f_newlist)
