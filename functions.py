from itertools import cycle
import sqlite3
from random import choice
import getpass
    
def database_conn():                           #database connection function for connecting to database
    global sqliteconnection,cursor
    try:
        sqliteconnection =sqlite3.connect('careem database.db')
        cursor = sqliteconnection.cursor()
        print("successfully connected to sqlite")
    except sqlite3.Error as error:
        print("error while connecting to sqlite", error)
            
def database_close_conn():
    if (sqliteconnection):
        sqliteconnection.close()
        print("the sqlite connection is closed")
                 
def signup():                                     #function for making account
    print("\n\t\t\t\t\t\t    [ SIGN UP ]")
    name=input("\nYour Name->\n\t")
    email=input("Your Email->\n\t")
    password=getpass.getpass("Enter Password\n\t") #input("Enter Password->\n\t")
    number=input("Your Contact Number->\n\t")
    print("\n\t\t\t\b********** YOU ARE REGISTERED **********\n\n")
    
    Sign_up_values_insert(name,email, number, password)
    
def signin():                                    # funnction for login to the account
    # global registered_email,registered_password
    print("\n\n\t\t\t\t\t\t     [ SIGN IN ]")
    registered_email=input("\nYour email->\n\t")
    registered_password=getpass.getpass("Enter Password\n\t") # input("Enter Password->\n\t")
    check_registered_values(registered_email,registered_password)
    
def Ride():                                      # function for choosing car or bike
    print("\n\t\t\t\t\t\t [ CHOOSE A RIDE ]\n\n")
    global vehical
    gen = cycle([0])
    for k in gen:
        vehical=int(input("1-Car\n2-Bike\n"))
        if vehical == 1:                              # checking for vehical selected
            car()
            break

        if vehical == 2:
            bike()
            break

        if vehical >= 3:
            print("\t\t\t\tEnter wrong number\n\t\t\t\tTry valid numbber")
            continue

def car():                                       # function for selecting models of car
    global model
    gen = cycle([0])
    for elt in gen:
        model = int(input(
            "\n\t\t\t\t\t[ LIST OF DIFFERENT TYPES OF CARS ]\n1- Honda Civic \n2- Suzuki Alto\n3- Corolla\n4- Toyota\n\n"))
        if model == 1 or model == 2 or model == 3 or model == 4:
            RideDetail(model)
            break

def bike():
    print("\n\t\t\t\t\t [ LIST OF DIFFERENT TYPES OF BIKES ]\n")
    global BikeType
    gen = cycle([0])
    for x in gen:
        BikeType=int(input("1- Super Power\n2- Yamaha\n\n"))
        if BikeType == 1 or BikeType == 2:
            RideDet(BikeType)
            break

def RideDetail(modelnum):
    CarName=['LX-6 Sedan','VXR (CNG)','GLI','VITZ']
    ModelName=['2016','2017','2015','2018']
    CarColor=['white','black','light blue','gray']
    CapName=['Babar Azam','HAssan Ali','Shadab Khan','Faheem Ashraf']
    print("\n\n\t\t\t\t\t\t  [ RIDE DETAILS ]\n")
    print("Your Captain is >", choice(CapName))
    print("car model >", choice(CarName))
    print("Model Name >", choice(ModelName))
    print("Car color  >>", choice(CarColor))

def RideDet(bikenum):
    BikeName = ['1500CC', 'SP70']
    Modelname = [2017, 2016]
    Capname = ['M Waseem Jr', 'Shaheen Shah Afridi']
    print("\nYour Captain is >", choice(Capname))
    print("Bike Namae >", choice(BikeName))
    print("Model Name >", choice(Modelname))

def Sign_up_values_insert(na_me,ema_il, cont_act, pass_word):
    sqlite_insert_with_param = """INSERT INTO 'Sign up table'
                        ('Name','Email','Password','Contact') 
                        VALUES (?, ?, ?, ?);"""

    data_tuple = (na_me,ema_il, pass_word, cont_act)
    cursor.execute(sqlite_insert_with_param, data_tuple)
    sqliteconnection.commit()
    #print("Python Variables inserted successfully into SqliteDb_Sign up table")
    
    cursor.close()

def check_registered_values(regis_tered_email,regis_tered_password):
    # sqliteConnection =sqlite3.connect('careem database.db')
    # cursor = sqliteconnection.cursor()
    sqlite_select_query = """SELECT * from 'Sign up table'"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    
    for row in records:
        if (row[1]==regis_tered_email and row[2]==regis_tered_password):
            print("\n\t\t\t\t\t********** YOU ARE SIGN IN ***********\n\n")
            break
        if (row[1]==regis_tered_email or row[2]==regis_tered_password):
            print("\n\t\t\t\t\t  Your Email or Password is Incorrect. Try again  \n\n") 
            signin()
            break
    else:
        print("\n\t\t\t\t\t       You are not Registered")
        print("\t\t\t\t\t\t   SIGN UP FIRST")
        name, email,password,number = signup()
        Sign_up_values_insert(name,email, number, password)

            
    cursor.close()
        
    
