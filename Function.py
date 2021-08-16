########### 1  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# f = lambda x: "even number" if x%2==0 else "odd number"
# print(f(int(input("Enter a number to check wether a number is even or odd : "))))


########### 2  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


# def reverse(n):
#     rev = 0
#     while n>0:
#         r = n%10
#         rev = rev*10 + r
#         n = n//10
#
#     return rev
# print(f"Reverse of number is {reverse(int(input('Enter the number to reverse : ')))}")


######### 3 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


# def Prime(n):
#     if n>1:
#         for i in range(2,n):
#             if n%i == 0:
#                 print(f"{n} is not a prime number")
#                 return
#         else:
#             print(f"{n} is a prime number ")
#     else:
#         print(f"{n} is not a prime number")
# Prime(int(input('Enter the number to check prime or not : ')))


########### 4  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


# f = lambda x:1 if x==0 else x*f(x-1)
# print(f"Reverse of number is {f(int(input('Enter the number to reverse : ')))}")


########### 5 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


# def fab(num):
#     first,second = 0,1
#     a = []
#     a = [0,1]
#     for i in range(2,num+1):
#         next = first + second
#         first = second
#         second = next
#         a.append(next)
#     return a
# print(fab(11))

# by recursion method

# def fab(num):
#     if num <= 1:
#         return num
#     else:
#         return fab(num-2) + fab(num-1)
#
#
# num = int(input(f"Enter how many fibonacci term you want to print : "))
# for i in range(num+1):
#     print(fab(i),end = " ")


############ 6 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def arms(num):
#     c = 0
#     n = num
#     while num > 0:
#         r = num%10
#         c = c + r*r*r
#         num = num//10
#     if c == n:
#         print(f"{n} is a armstrong number ")
#
#     else:
#         print(f"{n} is not a armstong number ")
#
# arms(int(input('Enter a number to find it is armstrong number or not : ')))





########### 7 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def palindrome(num):
#     s = 0
#     n = num
#     while num > 0:
#         r = num%10
#         s = s*10 + r
#         num = num//10
#     if n == s:
#         return True
#     else:
#         return False
#
# if palindrome(int(input(f"Enter a number to check wether the given number is palindrome or not : "))):
#     print("True")
# else:
#     print("False")






############ 8 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# print((lambda x:"Positive number" if x>0 else "Negative NUmber")(int(input("Enter a number : "))))





########## 9 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# print(f"{(lambda x,y:x if x>y else y)(int(input('Enter Two numbers :')),int(input()))} is a greatest number")





########## 10 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


# def calc(num):
#     s = 0
#     for i in num:
#         if i.isdigit():
#             i = int(i)
#             s += i
#         else:
#             pass
#     return s
# n = input("Enter a number to calulate the sum : ")
# print(calc(n))




########## 11 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def exp(a,b):
#     exp = a**b
#     return exp
#
# print(f"{exp(int(input('Enter the first number :')),int(input('Enter the second number : ')))} is the exponential of a^b")




#  -------------------------------  Done -------------------------------------------------







