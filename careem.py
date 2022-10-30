from functions import *

# main body 
database_conn()         # this function coonect script to database
print("\t\t\t\t\t********|| CAREEM SERVICE ||*************\n\n")
print("\t\t\t\t\t\t     Your ride\n")
print("\t\t\t\t\t        They way you want it\n")
print("\t\t\t\t\t        Whenever you want it\n\n")
gen = cycle([0])
for abc in gen:  
    sign=int(input("\t\t\t\t\t\t   1- [ SIGN UP ]\n\t\t\t\t\t\t   2- [ SIGN IN ]\n"))# choose sign in or sign up
    if sign==1:                                     # check condition for signup
        signup()                                    # calling function
        
        break
    elif sign==2:                                           # check condition for signin
        signin()                                     # calling function
        break
    else:
        print("\t\t\t\t\tEnter wrong number\n\t\t\t\t\tTry valid numbber")
        continue

print("\t\t\t\t\t\t[ Available Options ]\n")
ride=int(input("\t\t\t\tRide now -Press 1\t\t   Ride Later -press any key\n"))                  # chose ride now or ride letter
if ride==1:                                     # checking for ride book or not
    Ride() 
    print("\n\n\t\t\t\t\t   WAIT CAPTAIN IS COMMING IN A WHILE")
else:
    print("\n\n\t\t\t\t\t      You Choose Ride Latter")
    print("\n\t\t\t\t\t      THNK YOU FOR SIGNING IN ")


database_close_conn()               #close connction with database