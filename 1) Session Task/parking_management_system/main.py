from student_management_system.functions import *
from operator import itemgetter
import re
def insert():
    global no_of_vehicle
    no_of_vehicle = int(input("Enter NO of vehicle :"))
    def input11():
        count = 0
        for j in parking:
            for k in parking[j]:
                if k["Owner_Name"] == False:
                    count = count+1
                    def name_validation():
                        owner_name = input("Enter Owner Name :")
                        if owner_name.isalpha():
                            k["Owner_Name"] = owner_name
                        else:
                            print("Enter valid Name!!")
                            name_validation()
                    name_validation()

                    def vehicle_no_validation():
                        vehicle_no_list = []
                        for l in parking:
                            for m in parking[l]:
                                if m["Vehicle_No"] != False:
                                    vehicle_no_list.append(m["Vehicle_No"])
                        # print(vehicle_no_list)
                        def chek_vehicle_no():
                            vehicle_no = input("Enter Vehicle No :")
                            if vehicle_no.isalpha() or vehicle_no.isdigit():
                                if vehicle_no not in vehicle_no_list:
                                    k["Vehicle_No"] = vehicle_no
                                else:
                                    print("Vehicle is Exist Please Enter valid Vehicle Number!!")
                                    chek_vehicle_no()
                            else:
                                print("Enter valid Vehicle Number!!")
                                chek_vehicle_no()
                        chek_vehicle_no()

                    vehicle_no_validation()

                    def vehicle_type_validation():
                        vehicle_type = input("Enter Vehicle Type (2 wheeler / 4 wheeler) :")
                        if vehicle_type == "2" or vehicle_type == "4":
                            k["Vehicle_Type"] = vehicle_type
                        else:
                            print("Enter valid Vehicle Type!!")
                            vehicle_type_validation()
                    vehicle_type_validation()

                    if count == no_of_vehicle:
                        print(parking)
                        exit()
    def malti_time():
        for i in range(no_of_vehicle):
            input11()
    malti_time()

def parked_vehicle(pera):
    for i in parking:
        for j in parking[i]:
            if j['Basement_No'] == pera and j['Owner_Name'] != False:
                print(j)

def basement_sorted_by_vehicle_type():
    for j in parking:
        for k in parking[j]:
            # print(k)
            if k["Vehicle_Type"] == False:
                k["Vehicle_Type"] = "0"

    for l in parking:
        parking[l].sort(key=itemgetter("Vehicle_Type"))

    for m in parking:
        for n in parking[m]:
            if n["Owner_Name"] != False:
                print(n)

    for j in parking:
        for k in parking[j]:
            if k["Vehicle_Type"] == "0":
                k["Vehicle_Type"] = False
def removed_Vehicle_by_id():
    count = 0
    for i in parking:
        for j in parking[i]:
            count +=1
            if j["Owner_Name"] != False:
                print("ID",count,j)
    remove_parking = int(input("Enter ID :"))
    count = 0
    for k in parking:
        for l in parking[k]:
            count += 1
            if count == remove_parking:
                l["Owner_Name"] = False
                l["Vehicle_No"] = False
                l["Vehicle_Type"] = False
    print(parking)


parking = {1:[{'Owner_Name': False, 'Vehicle_No': False, 'Vehicle_Type': False, 'Basement_No': '1'},
              {'Owner_Name': False, 'Vehicle_No': False, 'Vehicle_Type': False, 'Basement_No': '1'},
              {'Owner_Name': False, 'Vehicle_No': False, 'Vehicle_Type': False, 'Basement_No': '1'},
              {'Owner_Name': False, 'Vehicle_No': False, 'Vehicle_Type': False, 'Basement_No': '1'}],
           2:[{'Owner_Name': False, 'Vehicle_No': False, 'Vehicle_Type': False, 'Basement_No': '2'},
              {'Owner_Name': False, 'Vehicle_No': False, 'Vehicle_Type': False, 'Basement_No': '2'},
              {'Owner_Name': False, 'Vehicle_No': False, 'Vehicle_Type': False, 'Basement_No': '2'},
              {'Owner_Name': False, 'Vehicle_No': False, 'Vehicle_Type': False, 'Basement_No': '2'}],
           3:[{'Owner_Name': False, 'Vehicle_No': False, 'Vehicle_Type': False, 'Basement_No': '3'},
              {'Owner_Name': False, 'Vehicle_No': False, 'Vehicle_Type': False, 'Basement_No': '3'},
              {'Owner_Name': False, 'Vehicle_No': False, 'Vehicle_Type': False, 'Basement_No': '3'},
              {'Owner_Name': False, 'Vehicle_No': False, 'Vehicle_Type': False, 'Basement_No': '3'}]}
no_of_vehicle =0
def main():
    global parking
    while True:
        print(" Parking Management System ".center(50, "*"))
        print("1) Add Vehicle", "2) Display Parked Vehicle Basement No", "3) All Basement Sorted By Vehicle Type",
              "4) Removed parked Vehicle by ID", "5) exit", sep="\n")
        option = new_option(5)
        if option == 1:
            insert()
        elif option == 2:
            print("Enter Basement No (1, 2 or 3)")
            basement = new_option(3)
            basement = str(basement)
            parked_vehicle(basement)
        elif option == 3:
            basement_sorted_by_vehicle_type()
        elif option == 4:
            removed_Vehicle_by_id()
        elif option == 5:
            exit()

main()
