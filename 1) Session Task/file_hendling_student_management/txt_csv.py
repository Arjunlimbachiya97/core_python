from student_management_system.functions import *
# from file_hendling_student_management.file_functions import *
from operator import itemgetter
file_name = input("Enter file name With extension : ")
# with open(file_name,"w") as ff:
#     ff.write("Roll No,Name,Department,City,\n")
def insert_roll_no(pera):
    roll = (input("Enter Roll NO : "))
    if roll.isdigit() == True:
        with open(file_name,pera) as file1:
            file1.write(f"{roll},")
    else:
        print("Enter valid Roll NO!!")
        insert_roll_no("a")

# insert_roll_no("a")

def insert_name(pera):
    try:
        name = input("Enter Name : ")
        if name.isalpha() == True:
            with open(file_name,pera) as file2:
                file2.write(f"{name},")
        else:
            print("Enter valid Name!!")
            insert_name("a")
    except:
        print("Enter valid Name!!")
        insert_name("a")
# insert_name("a")

def insert_department(pera):
    department = input("Enter Department : ")
    with open(file_name,pera) as file3:
        file3.write(f"{department},")
# insert_department("a")

def insert_city(pera):
    city = input("Enter City : ")
    with open(file_name,pera) as file4:
        file4.write(f"{city},\n")
# insert_city("a")


def delete_student2():
    delete_roll = input("Enter Roll No :")
    with open(file_name,"r") as file:
        file_data = file.readlines()
        print(file_data)
        with open(file_name,"w") as delete_data:
            for i in file_data:
                if i[0] != delete_roll:
                    print(delete_data.tell())
                    delete_data.write(i)


def student_detail3():
    student_roll = input("Enter Roll No :")
    with open(file_name, "r") as file:
        file_data = file.readlines()
        heding = file_data[0]
        heading_list = heding.split(",")
        for i in file_data:
            if i[0] == student_roll:
                student_data = i.split(",")
                print(f"{heading_list[0]} = {student_data[0]}",f"{heading_list[1]} = {student_data[1]}",f"{heading_list[2]} = {student_data[2]}",f"{heading_list[3]} = {student_data[3]}",sep="\n")
                exit()
        else:
            print("Enter valid Roll NO!!")
            student_detail3()


def update_student4():
    student_roll = input("Enter Roll No :")
    with open(file_name, "r") as file:
        file_data = file.readlines()
        count = 0
        for i in file_data:
            if i[0] == student_roll:
                data = i.split(",")
                print(data)
                data[0] = (input("Enter Roll NO"))
                data[1] = (input("Enter Name"))
                data[2] = (input("Enter Department"))
                data[3] = (input("Enter City"))
                data[4] = "\n"
                # print(data)
                update = ",".join(data)
                # print(update)
                file_data[count] = update
            else:
                count = count+1
        # print(file_data)
        with open(file_name,"w") as update_data:
            for j in file_data:
                    update_data.write(j)


def display_all_student5():
    with open(file_name, "r") as file:
        file_data = file.readlines()
        heding = file_data[0]
        heading_list = heding.split(",")
        count = 1
        for i in file_data[1::]:
            student_data = i.split(",")
            print(f" Student {count} ".center(50,"*"))
            print(f"{heading_list[0]} = {student_data[0]}",f"{heading_list[1]} = {student_data[1]}",f"{heading_list[2]} = {student_data[2]}",f"{heading_list[3]} = {student_data[3]}",sep="\n")
            count += 1

def short_student6(pera):
    with open(file_name,"r") as file:
        new_list = []
        file_data = file.readlines()
        for i in file_data[1::]:
            data = i.split(",")
            new_list.append(data)
        print("1)ASC","2)DESC",sep="\n")
        c = new_option(2)
        if c == 1:
            new_list.sort(key=itemgetter(pera))
            with open("sort_ASC.txt","w") as sort_file:
                for j in new_list:
                    sort = ",".join(j)
                    sort_file.write(sort)
        elif c == 2:
            new_list.sort(key=itemgetter(pera),reverse=True)
            with open("sort_DESC.txt","w") as sort_file_d:
                for k in new_list:
                    sort_d = ",".join(k)
                    sort_file_d.write(sort_d)

def search_student7(pera):
    with open(file_name,"r") as file:
        new_list = []
        file_data = file.readlines()
        for i in file_data[1::]:
            data = i.split(",")
            new_list.append(data)
        search_student = input("Search Student :")
        with open("search_student.txt", "w") as search:
            for j in new_list:
                if search_student in j[pera]:
                    sort_d = ",".join(j)
                    search.write(sort_d)


def file_hendling():
    while True:
        print(f" Student Management System With File Hendling ".center(100, "="))
        print("1) Insert Student", "2) Delete Student", "3) Student Detail", "4) Update Student", "5) Display All Student",
              "6) Short Student", "7) Search Student", "8) Exit", sep="\n")
        a = new_option(8)
        if a == 1:
            insert_roll_no("a")
            insert_name("a")
            insert_department("a")
            insert_city("a")
        elif a == 2:
            delete_student2()
        elif a == 3:
            student_detail3()
        elif a == 4:
            update_student4()
        elif a == 5:
            display_all_student5()
        elif a == 6:
            print("1) Short By Roll No", "2) Short By Name", "3) Short By Department", "4) Short By City", sep="\n")
            b = new_option(4)
            if b == 1:
                short_student6(0)
            elif b == 2:
                short_student6(1)
            elif b == 3:
                short_student6(2)
            elif b == 4:
                short_student6(3)
        elif a == 7:
            print("1) Search by Roll No", "2) Search by Name", "3) Search By Department", "4) Search by city", sep="\n")
            c = new_option(4)
            if c == 1:
                search_student7(0)
            elif c == 2:
                search_student7(1)
            elif c == 3:
                search_student7(2)
            elif c == 4:
                search_student7(3)
        elif a == 8:
            print("Thank you!")
            exit()
file_hendling()

