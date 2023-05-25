from student_management_system.functions import *
from operator import itemgetter
from datetime import datetime
import re
class Main():
    # define main variable
    def __init__(self,warehouse):
        self.warehouse = warehouse
        # self.list = [["pants","cotton","40","Added date"],
        #             ["a","csd","20","Added date"],
        #             ["b","fsd","1","Added date"],
        #             ["zpants","arh","50","Added date"]]
        # for i in self.list:
        #     self.warehouse.append(i)

    # for add product in warehouse
    def add_product(self):
        product_list = []
        name = []
        for i in self.warehouse:
            print(i[0])

        # product name validation
        def prduct_name_validation():

            product_name = input("Enter Product Name :")
            if product_name.isalpha():
                product_list.append(product_name)
            else:
                print("Enter valid Product Name!!")
                prduct_name_validation()
        prduct_name_validation()

        product_detail = input("Enter Product Detail :")
        product_list.append(product_detail)

        # product no of items validation
        def no_of_items_validation():
            try:
                number_of_items = input("Enter No of prduct :")
                if number_of_items.isdigit():
                    product_list.append(number_of_items)
                else:
                    print("Enter valid Number!!")
                    no_of_items_validation()
            except:
                print("Enter valid Number!!")
                no_of_items_validation()
        no_of_items_validation()

        def date_time_validation():
            date = input("Enter date in for mate (dd/mm/yy) :")
            # pattern = '^[1-31]{2}/[1-12]{2}/[10-99]{2}$'
            # a = int(date[3:5])
            # if a <= 12:
            try:
                date_time_obj = datetime.strptime(date, '%d/%m/%y')
                print(date_time_obj)
                date_value = date_time_obj.date()
                print(date_value(type))
                formate_date = datetime.strptime(date_value,'%d/%m/%y')
                print(formate_date)
                product_list.append(date_value)
            except:
                print("Enter valid date!!")
                date_time_validation()
            # else:
            #     print("Enter valid date!!")
            #     date_time_validation()
        date_time_validation()

        self.warehouse.append(product_list)
        print(self.warehouse)

    def show_all_product_with_details(self):
        for i in self.warehouse:
            print(i)

    def search_by_files(self,pera):
        search_data = input("search data :")
        if pera != 3:
            for i in self.warehouse:
                if search_data in i[pera]:
                    print(i)
        if pera == 3:
            for i in self.warehouse:
                j = str(i)
                if search_data in j:
                    print(i)


    def Sort_by_files(self,pera):
        self.warehouse.sort(key=itemgetter(pera))
        print(self.warehouse)

    def delete_product(self):
        for index,i in enumerate(self.warehouse):
            print(f"{index + 1} ==> {i}")
        delete_id = int(input("Enter id :"))
        for index1,j in enumerate(self.warehouse):
            if (index1+1) == delete_id:
                    self.warehouse.remove(j)
        for index,k in enumerate(self.warehouse):
            print(f"{index + 1} ==> {k}")


    def main(self):
        while True:
            print(" Warehouse Management ".center(50, "*"))
            print("1) Add Product", "2) Show Product Details", "3) Search Products According Field's.",
                  "4) Sort products according added date", "5) Delete product","6) Exit", sep="\n")
            option = new_option(6)
            if option == 1 :
                self.add_product()
            elif option == 2:
                self.show_all_product_with_details()
            elif option == 3:
                print("1) Search By Name", "2) Search By Detail", "3) Search By No of prduct",
                      "4) Search By Date", sep="\n")
                option_2 = new_option(4)
                if option_2 == 1:
                    self.search_by_files(0)
                elif option_2 == 2:
                    self.search_by_files(1)
                elif option_2 == 3:
                    self.search_by_files(2)
                elif option_2 == 4:
                    self.search_by_files(3)
            elif option == 4:
                print("1) Sort By Name", "2) Sort By Detail", "3) Sort By No of prduct",
                      "4) Sort By Date", sep="\n")
                option_2 = new_option(4)
                if option_2 == 1:
                    self.Sort_by_files(0)
                elif option_2 ==2:
                    self.Sort_by_files(1)
                elif option_2 == 3:
                    self.Sort_by_files(2)
                elif option_2 == 4:
                    self.Sort_by_files(3)
            elif option == 5:
                self.delete_product()
            elif option ==6 :
                print("Thank you!!")
                exit()

warehouse = []

call = Main(warehouse)
call.main()
