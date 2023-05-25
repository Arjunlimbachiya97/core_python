list1, list2 = [123, 'xyz', 'Nimesh'], [456, 'abc']
print("First list length : ", len(list1))
print("Second list length : ", len(list2))


aTuple = (123, 'xyz', 'Nimesh', 'abc')
aList = list(aTuple)
print(aTuple)
print("List elements : ", aList)



list1 = [123, 45, 3, 2]
print(max(list1))
print(min(list1))


aList.append(2009)
print("Updated List : ", aList)



aList = [123, 'xyz', 'Nimesh', 'abc', 123]

print("Count for 123 : ", aList.count(123))




aList = [123, 'xyz', 'Harshal', 'abc', 123]
bList = [2009, 'Nimesh']
aList.extend(bList)
print("Extended List : ", aList)


aList = [123, 'xyz', 'Nimesh', 'abc']
print("Index for Nimesh : ", aList.index('Nimesh'))



aList = [123, 'xyz', 'Nimesh', 'abc']
aList.insert(3, 2009)
print("Final List : ", aList)



aList = [123, 'xyz', 'Nimesh', 'abc']

print("A List : ", aList.pop())
print(aList)


print("B List : ", aList.pop(2))
print(aList)


aList = [123, 'xyz', 'Nimesh', 'abc', 'xyz']

aList.remove('xyz')
print("List : ", aList)


aList = [123, 'xyz', 'Nimesh', 'abc', 'xyz']
aList.reverse()
print("List : ", aList)



aList = [47.5, 123, 123456789.66666666]
aList.sort()
print("List : ", aList)

ls = [1, 1, "Asit", "Harshal", 'N', 45.5, 45.5, True]

print(ls)

print(ls[0])

print(ls[0:2])

print(ls[0:])

ls[5] = 66

print(ls)

print(type(ls))



name = [[1, 2, 3, 4, 5, 6], ["Dhairya", "Rahul", "ASit"]]

name[1][1] = 123456
print(name)

print(type(name))
