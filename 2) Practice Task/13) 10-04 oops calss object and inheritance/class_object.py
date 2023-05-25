# without use oops concept example
class Employee:
    pass


emp_1 = Employee()
emp_2 = Employee()


emp_1.firstName = "Vishal"
emp_1.lastName = "Modi"
emp_1.email = "Vishal.Modi@gmail.com"
emp_1.payment = 10000


emp_2.firstName = "Arjun"
emp_2.lastName = "Limbachiya"
emp_2.email = "limbachiya.arjun.97@gmail.com"
emp_2.payment = 20000



print(emp_1.email)
print(emp_2.email)


# with use oops concept example
class Employee1:
    def __init__(self, first, last, payment):
        self.first = first
        self.last = last
        self.payment = payment
        self.email = first + "." + last + "@gmail.com"


emp_1 = Employee1("Vishal", "Modi", 10000)
emp_2 = Employee1("Harshal", "Trivedi", 20000)

print(emp_1.email)
print(emp_2.email)

print(emp_1.payment)
print(emp_2.payment)
