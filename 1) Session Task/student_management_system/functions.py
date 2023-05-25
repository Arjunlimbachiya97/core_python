from operator import itemgetter
def options():
    try:
        optionsno = input("Enter your choise : ")
        print(optionsno)
        if type(optionsno) == str:
            if optionsno.isdigit() == True:
                optionsno = int(optionsno)
                if optionsno>=1 and optionsno<=7:
                    print(optionsno)
                    # op = optionsno
                    return optionsno
                else:
                    print("Enter valid choise1")
                    return options()
            else:
                print("Enter valid choise2")
                return options()
        else:
            print("Enter valid choise3")
            return  options()
    except:
        print("error")

def new_option(opt_range):
    try:
        choice = int(input("Enter your choise : "))
        if choice >=1 and choice <= opt_range:
            return choice
        else:
            print("Enter Valid Choice!!")
            return new_option(opt_range)
    except:
        print("Enter Valid Choice!!")
        return new_option(opt_range)
def add_student_1():
    global all
    global student
    def roll_validation():
        roll = input("Enter Roll No :")
        if roll.isalpha() != True:
            if roll.isdigit() == True:
                roll_list = []
                for i in all:
                    roll_list.append(i["Roll No"])
                if roll not in roll_list:
                    student["Roll No"] = roll
                else:
                    print("Enter valid Roll No!!")
                    roll_validation()
            else:
                print("Enter valid Roll No!!")
                roll_validation()
        else:
            print("Enter valid Roll No!!")
            roll_validation()
    roll_validation()

    def name_validation():
        name = input("Enter Name :")
        if name.isalpha() == True:
            student["Name"] = name
        else:
            print("Enter valid Name!!")
            name_validation()
    name_validation()

    # def department_validation():
    student["Department"] = input("Enter Department :")
    student["Address"] = input("Enter Address :")
    all.append(student)
    print("Student add successfully".center(50, "="))
    print(f"Roll NO    = {student['Roll No']}", f"Name       = {student['Name']}", f"Department = {student['Department']}",
          f"Address    = {student['Address']}", sep="\n")
    # print(student)
    del student
    student= {}


def delete_student_2():
    roll = (input("Enter your Roll No : "))
    roll_list = []

    for i in all:
        roll_list.append(i["Roll No"])

    for j in all:
        if roll in roll_list:
            if roll == j["Roll No"]:
                print("Delete student".center(50,"="))
                print(f"Roll NO    = {j['Roll No']}", f"Name       = {j['Name']}", f"Department = {j['Department']}",
                      f"Address    = {j['Address']}", sep="\n")
                all.remove(j)
                # print(all)
                break
        else:
            print("Enter valid Roll No")
            delete_student_2()


def student_detail_3():
    roll = input("Enter your Roll No : ")
    roll_list = []

    for i in all:
        roll_list.append(i["Roll No"])

    for j in all:
        if roll in roll_list:
            if roll == j["Roll No"]:
                print("Student detail".center(50,"="))
                print(f"Roll NO    = {j['Roll No']}",f"Name       = {j['Name']}",f"Department = {j['Department']}",f"Address    = {j['Address']}",sep="\n")
                break
        else:
            print("Enter valid Roll No")
            student_detail_3()


def update_student_4():
    roll = input("Enter your Roll No : ")
    if roll.isdigit() == True:
        roll_list = []

        for i in all:
            roll_list.append(i["Roll No"])

        for j in all:
            if roll in roll_list:
                if roll == j["Roll No"]:
                    print("Update detail".center(50,"="))
                    j['Roll No'] = input("Update Roll No :")
                    j['Name'] = input("Update Name :")
                    j['Department'] = input("Update Department :")
                    j['Address'] = input("Update Address :")
                    print("details updated successfully".center(50,"="))
                    print(f"Roll NO    = {j['Roll No']}",f"Name       = {j['Name']}",f"Department = {j['Department']}",f"Address    = {j['Address']}",sep="\n")
                    break
            else:
                print("Enter valid Roll No!!")
                update_student_4()
    else:
        print("Enter valid Roll No!!")
        update_student_4()

def display_all_student_5():
    print(f"Display All Student".center(50, "="))
    for i in all:
        print(f"Student {all.index(i)+1}".center(50,"="))
        for j in i:
            print(f"{j} = {i[j]}")

def display_student_by_Roll_No_6(name):
    print("1)ASC","2)DESC",sep="\n")
    c = new_option(2)
    if c == 1:
        all.sort(key=itemgetter(name))
        display_all_student_5()
    elif c == 2:
        all.sort(key=itemgetter(name),reverse=True)
        display_all_student_5()


def search_student_7(pera):
    search_student = input("Search Student :")
    string = str(dict)
    if search_student in string:
        for i in all:
            if search_student in i[pera] or search_student.upper() in i[pera]:
                print(f" Student {all.index(i) + 1} ".center(50, "="))
                print(f"Roll NO    = {i['Roll No']}", f"Name       = {i['Name']}", f"Department = {i['Department']}",
                      f"Address    = {i['Address']}", sep="\n")
                # print(i)
    else:
        print(f" Not match {pera} ".center(50, "*"))
    # search_student = input("Search Student :")
    # for i in all:
    #     if search_student in i[pera]:
    #         print(f"Roll NO    = {i['Roll No']}", f"Name       = {i['Name']}", f"Department = {i['Department']}",
    #               f"Address    = {i['Address']}", sep="\n")
    #         # print(i)


def main():
    global all, student
    all = [{'Roll No': "1", 'Name': 'Arjun', 'Department': 'mca', 'Address': 'bhabhar'}, {'Roll No': "2", 'Name': 'vishal', 'Department': 'b.com', 'Address': 'deesa'}]
    student = {}
    # count = 0
    while True:
        print(f" Student Management System ".center(50, "="))
        print("1) Insert Student", "2) Delete Student", "3) Student Detail", "4) Update Student", "5) Display All Student",
              "6) Short Student","7) Search Student","8) Exit", sep="\n")
        # print(all)
        # print("hi",options(7))
        # a = options()
        a = new_option(8)
        # print("abc",a)
        if a == 1:
            add_student_1()
        elif a == 2:
            delete_student_2()
        elif a == 3:
            student_detail_3()
        elif a == 4:
            update_student_4()
        elif a == 5:
            display_all_student_5()
        elif a == 6:
            print("1) Short By Roll No", "2) Short By Name","3) Short By Department","4) Short By City",sep="\n")
            b = new_option(4)
            if b == 1:
                display_student_by_Roll_No_6("Roll No")
            elif b == 2:
                display_student_by_Roll_No_6("Name")
            elif b == 3:
                display_student_by_Roll_No_6("Department")
            elif b == 4:
                display_student_by_Roll_No_6("Address")
        elif a == 7:
            print("1) Search by Roll No", "2) Search by Name","3) Search By Department", "4) Search by city",sep="\n")
            c = new_option(4)
            if c == 1:
                search_student_7("Roll No")
            elif c == 2:
                search_student_7("Name")
            elif c == 3:
                search_student_7("Department")
            elif c == 4:
                search_student_7("Address")
        elif a == 8:
            print("Thank you!")
            exit()