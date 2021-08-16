# ######  1 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


# sm1 = int(input("enter marks of first subject :"))
# sm2 = int(input("enter marks of Second subject :"))
# sm3 = int(input("enter marks of third subject :"))
# sm4 = int(input("enter marks of forth subject :"))
# sm5 = int(input("enter marks of fivfth subject :"))
#
# Avarage_Of_marks = (sm1 + sm2+ sm3 + sm4 + sm5)/5
#
# if Avarage_Of_marks >= 60:
#     print("First Division")
# elif Avarage_Of_marks >=50 and Avarage_Of_marks <=59:
#     print("Second division ")
# elif Avarage_Of_marks >=40 and Avarage_Of_marks <=49:
#     print('Third Division')
# else:
#     print("you are fail")





# ######  2 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# sm1 = int(input("enter marks of first subject :"))
# sm2 = int(input("enter marks of Second subject :"))
# sm3 = int(input("enter marks of third subject :"))
#
# if sm1 >= 60 and sm2 >= 50 and sm3 >= 40:
#     print("You are admitted ot professional college ")
# else:
#     print("Sorry you are admitted to professional college")

# sm1 = int(input("enter marks of first maths :"))
# sm2 = int(input("enter marks of Second physics :"))
# sm3 = int(input("enter marks of third subject :"))
#
# if sm1 + sm2>=150:
#     print("you qualified for admission ")
# else:
#     print("Sorry you are not able in qualifying exam")





# ###### 3 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# print("Enter 1 to find the area of rectange : ")
# print("Enter 2 to find the area of Circle : ")
# print("Please Enter you choice --> :",end = "")
#
# p1 = int(input())
# if p1 == 1:
#     l = int(input("Enter the length of rectagle : "))
#     b = int(input("Enter the breadth of rectagle : "))
#     area = l*b
#     print(f"Area of the circle is {area}")
#
# elif p1 == 2:
#     r = int(input("Enter the readious of rectagle : "))
#     area = 3.14*r*r
#     print(f"Area of the circle is {area}")





# ########  4 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# print("Enter 1 to find the addition of two numbers : ")
# print("Enter 2 to find the Sbutraction of two numbers : ")
# print("Enter 3 to find the multiplication of two numbers : ")
# print("Enter 4 to find the Division of two numbers : ")
# print("Enter 5 to find the inverse of two numbers : ")
# print("Enter 6 to find the Sqaure of two numbers : ")
# print("Enter 7 to find the Cube of two numbers : ")
#
# i = int(input("Please Enter you Choice to perform operation : "))
# if i >=1 and i <=7:
#     x = int(input("Enter the value of x : "))
# elif i >=1 and i <=4:
#     y = int(input("Enter the value of y : "))
#
# if i == 1 :
#     z = x + y
#     print(f"Sum of two numbers is {z}")
#
# elif i == 2 :
#     z = x - y
#     print(f"Subraction of two numbers is {z}")
#
# elif i == 3 :
#     z = x * y
#     print(f"Multiplication of two numbers is {z}")
#
# elif i == 4 :
#     z = x / y
#     print(f"Division of two numbers is {z}")
#
# elif i == 5 :
#     z = 1/x
#     print(f"Inverse of x number is {z}")
#
# elif i == 6 :
#     z = x*x
#     print(f"Square of x number is {z}")
#
# elif i == 7 :
#     z = x*x*x
#     print(f"Cube of x number is {z}")
#
# else:
#     print("Invalid choice")




####### 5 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# Balance = 2000
# while True:
#     print("\n\n\nEnter code w for withdraw ")
#     print("Enter code d for deposit ")
#     print("Enter code c for Checking balance ")
#     print("Enter code e for exit ")
#     i = input("   \n\nPlease Enter your Choice : ")
#
#     if i == "d":
#         amount = int(input("Enter the amount you want to Deposit : "))
#         Balance = amount+Balance
#         print("Deposit Completed Succefully ")
#
#     elif i == "w":
#         class NotSufficientAmount(Exception):
#             def __init__(self,value):
#                 self.value = value
#         amount = int(input("Enter the amount you want to Withdraw : "))
#         try:
#             if Balance <= amount:
#                 raise NotSufficientAmount("UnSufficient Amount in the bank")
#         except NotSufficientAmount as e:
#             print(e.args)
#         else:
#             Balance = Balance - amount
#             print("Withdraw Amount Successfully")
#         finally:
#             print("Sources closed successfully")
#
#     elif i == "c":
#         print(f"Total amount in the bank is {Balance}")
#
#     elif i == "e":
#         break
#
#     else:
#         print("Pleasee Select the valid Choice ")





























