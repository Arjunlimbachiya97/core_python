str_ex = 'Arjunnnnn_hbahabhab'

print(str_ex)

'''
comment section
comment1
cooment2
'''
print(str_ex[0])

print(str_ex[2:7])

print(str_ex[2:])

print(str_ex * 2)

print(str_ex + "Hello")

print(str_ex, 'hello')

print(str_ex + "1")

print(str_ex, 1)


# Format method
print("Hey My name is: %s my roll no is : %d how are you: %s" % ('a', 44, 'Vishal'))

a = 10
b = "dharmesh"

print(str(a) + b)
print("%s %d" % (b, a))
print('{},{}'.format(a, b))



# String methods.
a = "hello"


print(len(a))


print(a.capitalize())


str = "this is zstring examplez"
sub = "i"
print("count:", str.count("z",4))


str1 = "this is string example"
str2 = "exam"
print(str1.find(str2))


s = "-"
seq = ("a", "b", "c")
c = s.join(seq)
print(c)
print(type(c))


str = "this is string example"
ls = str.split(' ')
print(ls)


str = "THIS IS STRING EXAMPLE"
print(str.isupper())


str = "THIS is string example"
print(str.isupper())


str = "hello"
print(str.islower())


str = "THIS IS STRING EXAMPLE"
print(str.lower())


str = "hello"
print(str.upper())


str = "this is string example"
print(str.replace("is", "was"))


b = "55"
print(b.isdigit())
