### 1 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
'''
_/\      _
   \    /
    \/\/
'''


'''
class stack:
    Top = -1
    size = 0
    __s = [-1]
    # def __init__(self,x):
    #     self.x = x

    def push(self,x):
        self.__s.append(x)
    def pop(self):
        self.__s.pop()
    def top(self):
        return self.__s[-1]
    def isnull(self):
        if self.__s[-1] == -1:
            return True
        else:
            return False

class WrongInput(Exception):
    def __init__(self,msg):
        self.msg = msg

def hike(x):
    s = stack()
    count = 0
    size = 0
    sea_level = 0
    u = 1
    d = -1
    flag = 0
    x = x.lower()
    path = list(x)
    for i in path:
        size += 1
        if i == 'd':
            sea_level += d
        else:
            sea_level += u
        if i != 'u'and i!= 'd':
            raise WrongInput("Wrong Character present in the string")
        elif i == s.top() or s.top() == -1:
            s.push(i)

        elif i!=s.top():
            s.pop()
        if sea_level < 0:
            flag = 1
        if s.isnull():
            if flag == 1:
                count+=1
                flag = 0
    print(size)
    print(count)



if __name__ == '__main__':
    x = input()
    hike(x)
'''



### 2 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# l = input("Enter : ")
# l = list(l)
# l = [i for i in l if i!=' ']
# l = [int(i) for i in l]
# count = 0
# index = 0
# flag = 0
# while index<len(l)-1:
#     try:
#         if flag == 0:
#             if l[index+1] == 0 and l[index+2] == 0:
#                 count+=1
#                 index +=2
#             elif l[index+1] == 0:
#                 count+=1
#                 index+=1
#
#         if l[index+1] == 1:
#             index+=1
#             flag = 1
#         elif l[index + 1] == 0 and l[index + 2] == 0 and l[index]!=1:
#             flag = 0
#             count += 1
#             index += 2
#                                                         #  index = 5
#         elif l[index+1] == 0:
#             flag = 0                                    # count = 3
#             index+=1
#             count+=1                                    #  0010000100
#
#     except:
#         try:
#                         if l[index+1] == 0:
#                 count+=1
#                 index+=1
#             elif l[index+1] == 1:pass
#         except:
#             pass
# print(count)






### 3 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# s = input()
# i = int(input())
# count = i//len(s)
# s = s*count
# n = i%len(s)
# s = s+s[:n]
# check = s.count('a')
# print(check)






### 45 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# import numpy as np
# np.random.seed(0)
# arr = '''0 6 -7 1 6 3
# -8 2 8 3 -2 7
# -3 3 -6 -3 0 -6
# 5 0 5 -1 -5 2
# 6 2 8 1 3 0
# 8 5 0 4 -7 4
# '''
# arr = arr.splitlines()
# l1 = []
# l2 = []
# for i  in arr:
#     l1.append(i.split())
#
# arr = np.array(l1).astype(dtype='int32')
# l = []
# for i in range(0,4):
#     for j in range(0,4):
#         a1 = arr[i:3+i:2,j:3+j]
#         print(a1,end = "     ")
#         a2 = arr[i+1,j+1]
#         print(a2)
#         l.append(a1.sum()+a2)
# print(max(l))







### 45 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# size = input()
# l = []
# s1,s2 = size.split()
# for i in range(int(s1)):
#     x = input()
#     l.append(x)
# for i in range(int(s2)):
#         x = l[0]
#         print(x)
#         del l[0]
#         l.append(x)
# for i in l:
#     print(i,end = " ")










# array = []
# size = int(input("Enter the size check you want to check test cases :"))
# for i in range(size):
#     size_of_array = int(input("Enter the size of array : "))
#     arra = input(f"Enter the array of length {size_of_array} by space : ")
#     arra = arra.replace('\n','')
#     array = [int(i) for i in arra.split()]
#     count = 0
#     flag = 0
#     for i,j in enumerate(array,1):
#         if i <= j:
#             pass
#         elif i > j:
#             k = array.index((j + 1))
#             k += 1
#             print(k>array.index(j),k<=j,k,j,array.index(j)+1)
#             if (k > array.index(j) + 1) or (k <= j):
#                 pass
#             else:
#                 flag = 1
#                 count += 1
#
#
#         index = array.index(i)
#         index+=1
#         sub = i-index
#         if sub<0:
#             check = array[array.index(i)-1]
#
#             if check>i and check<=(index-1) and flag == 0:
#                 count+=1
#             else:
#                 flag = 1
#                 continue
#         elif sub >2:
#             print("Too chaotic")
#             break
#         elif sub>0 and sub<=2:
#             count+=sub
#
#     print(count)






# # 45 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# 16 coin puzzle problem
#
# print("----------------------- 16 Coin Puzzle -----------------------")
# print("---------------------  Coins -> 1 2 3 4 -----------------------")
# import random
# l = [1,2,3,4]
# player = input("Enter what you want to take {head or tail} : ")
# player = player.lower()
# if player != 'head' and player != 'tail':
#     raise Exception("Please Enter head or tail only")
# choice = ['head','tail']
# chance = random.choice(choice)
# input("Please Enter to Toss the coin ")
# if chance == player:
#     print(f"{chance} Came Congratulation! Player1 won the toss")
#     input("Please Enter to Start the Game")
# else:
#     print(f"{chance} Came Computer won the toss")
#     input("Press Enter to Start the Game")
# if chance == player:
#
#     player1 = int(input("Player1 Enter the coin : "))
#     coin = player1
#     # print(f"Total Coins = {coin}")
#     if 6 - player1 > 4:
#         computer = random.choice(l)
#         print(f"Computer Entered = {computer}")
#         coin += computer
#         print(f"Total Coins = {coin}")
#         player1 = int(input("Player1 Enter the coin : "))
#         coin += player1
#         if coin < 6:
#             computer = 6 - coin
#             coin += computer
#             print(f"Computer Entered = {computer}")
#             print(f"Total Coins = {coin}")
#             player1 = int(input("Player1 Enter the coin : "))
#             coin += player1
#             print(f"Total Coins = {coin}")
#             computer = 11 - coin
#             print(f"Computer Entered = {computer}")
#             coin += computer
#             print(f"Total Coins = {coin}")
#             player1 = int(input("Player1 Enter the coin : "))
#
#             coin += player1
#             # print(f"Total Coins = {coin}")
#             computer = 16 - coin
#             coin += computer
#             print(f"Computer Entered = {computer}")
#             print(f"Total Coins = {coin}")
#             print("Computer win the game")
#         elif coin == 6:
#             computer = random.choice(l)
#             print(f"Computer Entered = {computer}")
#             coin += computer
#             print(f"Total Coins = {coin}")
#             player1 = int(input("Player1 Enter the coin : "))
#             coin += player1
#             if coin < 11:
#                 computer = 11 - coin
#                 print(f"Computer Entered = {computer}")
#                 coin += computer
#                 print(f"Total Coins = {coin}")
#                 player1 = int(input("Player1 Enter the coin : "))
#
#                 coin += player1
#                 # print(f"Total Coins = {coin}")
#                 computer = 16 - coin
#                 print(f"Computer Entered = {computer}")
#                 coin += computer
#                 print(f"Total Coins = {coin}")
#                 print("Computer win the game")
#             elif coin == 11:
#                 computer = random.choice(l)
#                 print(f"Computer Entered = {computer}")
#                 coin += computer
#                 print(f"Total coin = {coin}")
#                 player1 = int(input("Player1 Enter the coin : "))
#                 coin += player1
#                 if coin == 16:
#                     print(f"Total Coins = {coin}")
#                     print(f"Player1 won the game ")
#                 elif coin < 16:
#                     computer = 16 - coin
#                     print(f"Computer Entered = {computer}")
#                     coin += computer
#                     print(f"Total Coins = {coin}")
#                     print("Computer won the game ")
#
#             elif coin > 11:
#                 computer = 16 - coin
#                 print(f"Computer Entered = {computer}")
#                 coin += computer
#                 print(f"Total Coins = {coin}")
#                 print("Computer won the game ")
#         elif coin > 6:
#             computer = 11 - coin
#             print(f"Computer Entered = {computer}")
#             coin += computer
#             print(f"Total Coins = {coin}")
#             player1 = int(input("Player1 Enter the coin : "))
#
#             coin += player1
#             # print(f"Total Coins = {coin}")
#             computer = 16 - coin
#             coin += computer
#             print(f"Computer Entered = {computer}")
#             print(f"Total Coins = {coin}")
#             print("Computer win the game")
#
#
#
#
#     else:
#         computer = 6 - player1
#         print(f"Computer Entered = {computer}")
#         coin += computer
#         print(f"Total Coins = {coin}")
#         player1 = int(input("Player1 Enter the coin : "))
#         coin += player1
#         # print(f"Total Coins = {coin}")
#         computer = 11 - coin
#         print(f"Computer Entered = {computer}")
#         coin += computer
#         print(f"Total Coins = {coin}")
#         player1 = int(input("Player1 Enter the coin : "))
#
#         coin += player1
#         # print(f"Total Coins = {coin}")
#         computer = 16 - coin
#         coin += computer
#         print(f"Computer Entered = {computer}")
#         print(f"Total Coins = {coin}")
#         print("Computer win the game")
#
# else:
#     computer = 1
#     coin = computer
#     print(f"Computer Entered = {computer}")
#     print(f"Total Coins = {coin}")
#     player1 = int(input("Player1 Enter the coin : "))
#     coin += player1
#     computer = 6 - coin
#     print(f"Computer Entered = {computer}")
#     coin += computer
#     print(f"Total Coins = {coin}")
#     player1 = int(input("Player1 Enter the coin : "))
#     coin += player1
#     # print(f"Total Coins = {coin}")
#     computer = 11 - coin
#     print(f"Computer Entered = {computer}")
#     coin += computer
#     print(f"Total Coins = {coin}")
#     player1 = int(input("Player1 Enter the coin : "))
#
#     coin += player1
#     # print(f"Total Coins = {coin}")
#     computer = 16 - coin
#     coin += computer
#     print(f"Computer Entered = {computer}")
#     print(f"Total Coins = {coin}")
#     print("Computer win the game")


# test_cases = int(input())
# for _ in range(test_cases):
#     t = int(input())
#     a = list(map(int, input().split()))
#     swaps = [0] * t
#
#     swapped = True
#
#     while swapped:
#         swapped = False
#
#         for i in range(t):
#             while i < t - 1 and a[i] > a[i + 1]:       # swaps[2,3] = 1              1<4  and 4>5
#                 swaps[a[i] - 1] += 1
#                 a[i], a[i + 1] = a[i + 1], a[i]        # a[0,1,2] = 4,3,3     a[1,2,3] = 5,3
#                 swapped = True
#                 i += 2
#
#     s = 0
#     for swap in swaps:
#         s += swap
#
#         if swap > 2:
#             print('Too chaotic')
#             break
#     else:
#         print(s)





# # 45 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# size = int(input())
# a = list(map(int, input().split()))
# a1 = set(a)
# a1 = sorted(a1,reverse = True)
# size1 = int(input())
# a2 = list(map(int, input().split()))
#
# i = 0
# m = 0
# len_a2 = len(a2)
# len_a1 = len(a1)
# k = len_a1-1
# while k>=0 and i<len_a2:
#     try:
#         if a2[m] <= a1[k]:
#             if a2[m]<a1[k]:
#                 print(k + 2)
#                 m+=1
#             elif a2[m] <= a1[k]:
#                 print(k + 1)
#                 m += 1
#             else:
#                     k-=1
#         elif k == 0:
#             print(k + 1)
#             m+=1
#         else:
#             k-=1
#     except:
#         break







# t = input()
# t_am_pm = t[-2::]
# t_am_pm = t_am_pm.lower()
# t_time_without_am_pm = t[:-2]
# time_list = t_time_without_am_pm.split(":",3)
# t_time_hr = time_list[0]
# t_time_min = time_list[1]
# t_time_sec = time_list[2]
# t_time_hr = int(t_time_hr)
# i = 1
# j = 13
# if t_am_pm == 'am':
#     if t_time_hr >= 1 and t_time_hr <12:
#         print(":".join(time_list))
#     elif t_time_hr == 12:
#         time_list[0] = '00'
#         print(":".join(time_list))
#
# else:
#     if t_time_hr >= 1 and t_time_hr <12:
#         time_list[0] = str((t_time_hr-1)+13)
#         print(":".join(time_list))
#     else:
#         time_list[0] = '12'
#         print(":".join(time_list))


# Abhishek Challenge @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


'''
s = input("Ente the string : ")
l = []
j = ''
flag = 0

for i in range(len(s)):
    if s[i] == ' ':
        flag = 1
        l.append(j)
        j = ''

    if flag != 1:
        j+=s[i]
        if len(s) -1  == i:
            l.append(j)
    else:
        flag = 0

print(l)


for i in range(len(l)):
    count = 1
    for j in range(i+1,len(l)):
        if l[i] == l[j] and l[i] != -1:
            count += 1
            l[j] = -1
    if l[i] != -1:
        print("frequency of ",l[i],"is ",count)












s = input("Ente the string : ")
j = ''
k = ''
flag = 0
len_rep = 1
len_non_rep = 0
for i in range(len(s)):
    if s[i] == ' ':
        flag = 1
        len_rep += 1
        if j not in k:
            len_non_rep += 1
            k += j + ' '
        j = ''

    if flag != 1:
        j+=s[i]
        if len(s) -1  == i and j not in k:
            k+= j
            len_non_rep += 1
    else:
        flag = 0

print(k)
print("len of repeated words " ,len_rep)
print("len of non repeated words " ,len_non_rep)
count = 0
for i in k:
    count = 0
    for j in s:
        if i == j:
            count+=1
    print("frequency of ",i,"is ",count)















def len(str):
    count = 0
    for i in str:
        count+=1
    return count

s = input("Ente the string : ")
j = ''
k = ''
flag = 0
len_rep = 1
len_non_rep = 0
for i in range(len(s)):
    if s[i] == ' ':
        flag = 1
        len_rep += 1
        if j not in k:
            len_non_rep += 1
            k += j + ' '
        j = ''

    if flag != 1:
        j+=s[i]
        if len(s) -1  == i and j not in k:
            k+= j
            len_non_rep += 1
    else:
        flag = 0


# print("len of repeated words " ,len_rep , s , len(s))
# print("len of non repeated words " ,len_non_rep , k , len(k))
count = 1
i = 0
j = 0
m = ''
n = ''
flag = 0
while i < len(k):
    j = 0
    count = 0
    if k[i] != ' ':
        m += k[i]
    while (j < len(s) and k[i] == ' ') or len(k)-1 == i:
        # print(m)
        if s[j] != ' ':
            n+=s[j]
        # print(n)
        if (m == n and s[j] == " ") or (m == n and len(s) -1 == j):
            count+=1
            n = ''
        elif s[j] == " ":
            n = ''
        if len(s) - 1  == j:
            flag = 1
            break

        j+=1

    i+=1
    if flag == 1:
        print("frequency of ",m,"is ",count)
        flag = 0
        m = ''

'''






'''
from itertools import combinations_with_replacement

l = []
str , n = input().split()
combination = list(combinations_with_replacement(str,int(n)))


for i in combination:
    l.append(tuple(sorted(i)))

l.sort()

for i in l:
    sub = "".join(i)
    print(sub)

'''













# test_cases = int(input())
# for _ in range(test_cases):
#     a,b = input().split()
#     try:
#         a = int(a)
#         b = int(b)
#         div = a//b
#         print(div)
#     except ZeroDivisionError as e:
#         print("Error Code: integer division or modulo by zero")
#     except ValueError as e:
#         print(f"Error Code: invalid literal for int() with base 10: '{b}'")





















































