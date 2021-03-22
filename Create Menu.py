#Sakht menu
import os
studen_list = list()

while True:
    #**************Start Menu ***************
    flag = True # baraye hata vared kardan menu
    while True:
        print("1/Add student")
        print("2/show student")
        print("3/Exit")

        if flag == False: # baraye hata vared kardan menu
            print("Error!",end="") 
        selected_menu = int(input("Menu = "))
        if selected_menu in [1,2,3]:
            os.system("cls")
            break
        flag == False
        os.system("cls")
    #*************End Menu ************************


    #************* Star Main Section ***************
    if selected_menu == 1:
        info = list()
        info.append(input("Name = "))
        info.append(input("family = "))
        info.append(int(input("Age = ")))
        info.append(input("national_code = "))
        info.append(input("male/female = "))
        studen_list.append(info)
        os.system("cls")

    elif selected_menu == 2:
        for item in studen_list:
            for val in item:
                print(val,end="\t")
            print()    
    else:
        break
    #*************End Main Section *****************

    