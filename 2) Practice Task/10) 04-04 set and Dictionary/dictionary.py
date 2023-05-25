dict_1 = {'key': 'value', 'name': 'Nimesh', "marks": 99, 'k6': "Harshal", "k7": 88.8}

print(dict_1)

print(dict_1['k6'])

dict_1['k7'] = 99

print(dict_1)

print(type(dict_1))


# Dictionary functions

dict = {'Name': 'Abc', 'Age': 18}
print(len(dict))

asit = {'Name': 'Abc', 'Age': 18}
print(type(asit))


a = str(dict)
print(a[1])


print(type(str(dict)))


dict = {'Name': 'Abc', 'Age': 7}
print(len(dict))

dict.clear()

print(len(dict))

dict1 = {'Name': 'Abc', 'Age': 7}
abc = dict1.copy()
print(abc)


tupl = ('name', 'age')
the = dict.fromkeys(tupl)
print(the)


dict = dict.fromkeys(tupl, 10)
print(dict)


dict = {'Name': 'abc', 'Age': 7}
print(dict.get('Age'))


print(dict.get('Education', "Never"))


dict = {'Name': 'Abc', 'Age': 7}
print(dict.items())


print(dict.values())


print(dict.keys())


dict1 = {'Name': 'xyz', 'Age': 7}
dict2 = {'Gender': 'male'}
dict1.update(dict2)
print(dict1)
print(dict2)
