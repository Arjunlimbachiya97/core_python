from student_management_system.functions import *

def add_vehicle():
    # number = int(input("How many vehicle you wont to park : "))
    count = 0
    if len(parking) == 0:
        count += 1
        nes_dict["ID"] = str(count)
        nes_dict["Owner_Name"] = input("Enter Owner Name :")
        nes_dict["Vehicle_No"] = input("Enter Vehicle No :")
        nes_dict["Vehicle_Type"] = input("Enter Vehicle Type :")
        nes_dict["Basement_No"] = "1"
        parking.append(nes_dict)
        print(parking)
        print(count)
        del nes_dict
        # nes_dict = {}
        # nes_dict.clear()
    # print(count)
    elif len(parking) != 0:
        basement_1 = 0
        for i in parking:
            print(i)
            print("nested",nes_dict)
            if i["Basement_No"] == "1":
                basement_1 += 1
        if basement_1 < 4:
            count += 1
            nes_dict["ID"] = str(count)
            nes_dict["Owner_Name"] = input("Enter Owner Name :")
            nes_dict["Vehicle_No"] = input("Enter Vehicle No :")
            nes_dict["Vehicle_Type"] = input("Enter Vehicle Type :")
            nes_dict["Basement_No"] = "1"
            parking.append(nes_dict)
        print(parking)



# parking = [{'ID': '1', 'Owner_Name': 'Arjun', 'Vehicle_No': 'GJ-18-2020', 'Vehicle_Type': '2', 'Basement_No': '1'}]
parking = []
nes_dict = {}

def main():
    global parking,nes_dict
    while True:
        print(" Parking Management System ".center(50, "*"))
        print("1) Add Vehicle", "2) Parked Vehicle on basement No", "3) All Basement Sorted By Vehicle Type",
              "4) Removed parked Vehicle by ID", "5) exit", sep="\n")
        option = new_option(5)
        if option == 1:
            add_vehicle()
        elif option == 5:
            exit()

main()
