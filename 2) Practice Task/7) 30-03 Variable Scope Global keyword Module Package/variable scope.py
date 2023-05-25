heding = "Variable Scope"
print(heding.center(50,"="))


# global variable
name = "Arjun"

def variable_scop():
    #local variable
    name = "Vishal"
    def inner():
        # nonolocal variable
        nonlocal name
        print(name)
    inner()
variable_scop()


heding2 =  "Global keyword"
print(heding2.center(50,"="))

def global_keyword():
    global mobile
    mobile = 6354020482
    print(mobile)

global_keyword()
print("This variable use in global ->",mobile)


heding3 = "Module Package"
print(heding3.center(50,"="))

print("use in calculater function")