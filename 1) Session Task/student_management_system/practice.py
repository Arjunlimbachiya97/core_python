# import calculater.calculater_functions as cf
# def options():
#     optionsno = input("Enter your choise : ")
#     if type(optionsno) == str:
#         if optionsno.isdigit() == True:
#             optionsno = int(optionsno)
#             if optionsno>=1 and optionsno<=13:
#                 return optionsno
#             else:
#                 print("Enter valid choise")
#                 options()
#         else:
#             print("Enter valid choise")
#             options()
#     else:
#         print("Enter valid choise")
#         options()
#
#
# def add_student():
#     global all
#     global student
#     global count
#     count += 1
#     # all[count] = student
#     # all.append()
#     student["Roll No"] = count
#     student["Name"]= input("Enter Name :")
#     student["Department"] = input("Enter Department :")
#     student["Address"] = input("Enter Address :")
#     all.append(student)
#     del student
#     student= {}
#
# def delete():
#     student_id = int(input("Enter your ID : "))
#     keys = all.keys()
#     if student_id in keys:
#         del all[student_id]
#     else:
#         print("Enter valid ID")
#         delete()
#
#
# def one_student_detail():
#     student_id = int(input("Enter your ID : "))
#     keys = all.keys()
#     if student_id in keys:
#          print(all[student_id])
#     else:
#         print("Enter valid ID")
#         delete()
#
#
#
# def update_student_detail():
#     student_id = int(input("Enter update student ID : "))
#     pass
#
# def sort_rollno():
#     s = all.keys()
#     list1 = []
#     for i in s:
#         list1.append(i)
#     (list1.sort(reverse=True))
#
#     desc = []
#     for j in list1:
#         desc.append(all[j])
#     print(desc)
#
#
# print("1) Insert Student", "2) Delete Student", "3) Student Detail", "4) Update Student", "5) Display All Student",
#       "6) Display student by Roll No (ASC/DESC)", "7) Dispaly studnet by Name (ASC/DESC)",
#       "8) Dispaly studnet by Department (ASC/DESC) For Ex. BCA, B.Tech,etc.",
#       "9) Dispaly studnet by City (ASC/DESC)", "10) Search by Roll No", "11) Search by Name",
#       "12) Search By Department", "13) Search by city", sep="\n")
# all = [{'Roll No': 1, 'Name': 'Arjun', 'Department': 'mca', 'Address': 'bhabhar'}, {'Roll No': 2, 'Name': 'vishal', 'Department': 'b.com', 'Address': 'deesa'}]
# student = {}
# count = 0
# while True:
#     print(all)
#     a = options()
#     if a == 1:
#         add_student()
#     elif a == 2:
#         delete()
#     elif a == 3:
#         one_student_detail()
#     elif a == 4:
#         pass
#     elif a == 5:
#         print(all)
#     elif a == 6:
#         sort_rollno()
#
#
#
#
#     cf.exit_program()
