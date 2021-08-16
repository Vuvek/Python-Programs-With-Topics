############ 1  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# from functools import reduce
# l = [int(i) if i.isdigit() else float(i) if i.isdecimal() else i for i in [input(f"Enter the {i+1} element of list : ") for i in range(int(input("Enter the size of the element : ")))]]
# print(l)
# list1 = reduce(lambda x,y:x+y,l)
# print(list1)



########### 2  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# l = [int(i) if i.isdigit() else float(i) if i.isdecimal() else i for i in [input(f"Enter the {i+1} element of list : ") for i\
#                                                                            in range(int(input("Enter the size of the element : ")))]]
# print(max(l))


########### 3 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


# l =  [input(f"Enter the {i+1} element of list : ") for i in range(int(input("Enter the size of the element : ")))]
#
# count = 0
# m = []
# for i,j in enumerate(l):
#     if (len(j) > 2) and (j[0] == j[-1]):
#         print(j)
#         count+=1
#         m.append(j)
#
# print(f"Total string present in the list which satisfy the condition is {count} and strings are {m}")


######### 4 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@



# l = [int(i) if i.isdigit() else float(i) if i.isdecimal() else i for i in [input(f"Enter the {i+1} element of list : ") for i in range(int(input("Enter the size of the element : ")))]]
#
# for i in range(len(l)-1):
#     c = i+1
#     for k in range(i+1,len(l)):
#         m,n = l[i],l[c]
#         if l[i] == l[c]:
#             l.remove(l[c])
#         if m != n:
#             c+=1
# print(l)


########## 5 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# l = [int(i) if i.isdigit() else float(i) if i.isdecimal() else i for i in [input(f"Enter the {i+1} element of list : ") for i in range(int(input("Enter the size of the element : ")))]]
# if len(l) == 0:
#     print(f"lsit {l} is empty list")
# else:
#     pritn(f"lsit {l} is not empty list")




############ 6 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2



# l = [int(i) if i.isdigit() else float(i) if i.isdecimal() else i for i in [input(f"Enter the {i+1} element of list : ") for i in range(int(input("Enter the size of the element : ")))]]
# rem = [0,4,5]
# rem.reverse()
# try:
#     for i in rem:
#         l.remove(l[i])
#     print(l)
# except:
#     print(f"your string length is insufficiet to satisfy the condition please give sufficient length")


####### 7 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# l = [int(i) if i.isdigit() else float(i) if i.isdecimal() else i for i in [input(f"Enter the {i+1} element of list : ") for i in range(int(input("Enter the size of the element : ")))]]
# l1 = []
# for i,j in enumerate(l):
#     if j%2 == 0:
#         l1.append(i)
# l1.reverse()
# print(l1)
# for j in l1:
#     l.remove(l[j])
# print(f"List after removing all even number in the lsit is {l}")


########## 8 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


# l = [int(i) if i.isdigit() else float(i) if i.isdecimal() else i for i in [input(f"Enter the {i+1} element of list : ") for i in range(int(input("Enter the size of the element : ")))]]
# for i,j in enumerate(l):
#     if not isinstance(i,str):
#         j = str(j)
#         l[i] = j
# print(l)
# print(type(l[0]))


########## 9 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


# l = [int(i) if i.isdigit() else float(i) if i.isdecimal() else i for i in [input(f"Enter the {i+1} element of list : ") for i in range(int(input("Enter the size of the element : ")))]]
# l.sort()
# print(l[-2])


########### 10 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


# l = [int(i) if i.isdigit() else float(i) if i.isdecimal() else i for i in [input(f"Enter the {i+1} element of list : ") for i in range(int(input("Enter the size of the element : ")))]]
# s = set(l)
# print(s)
# l = list(s)
# print(f"After remving the unque elemetns im the list {l} ")





































































# These are the two codes which are the best code for removing the duplicates from the list

### 1 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 49


# l1 = [[1,2 , 3 ],[11,12,'b','b','b'],[21,'t',223],[4,5,6],[7,8,9],'demo',12.5]
# for k,i in enumerate(l1):
#     if isinstance(i,list):
#         for l,j in enumerate(i):
#             if isinstance(j,str):
#                 print(f"{i[l]} is at index {k},{l}")
#                 while True:
#                     try:
#                         print(i[l])
#                         # del l1[k][l]
#                         i.remove(i[l])
#                         if isinstance(l1[k][l],str):
#                             continue
#                         else:
#                             break
#                     except:
#                         break
# print(l1)







### 2 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 49

# l = [[1,2 , 3 ],[11,12,'b','b','b'],[21,'t',223],[4,5,6],[7,8,9],'demo',12.5]
# len_list = len(l)
# i = 0
# while i < len_list:
#     j = 0
#     if type(l[i]) == list:
#
#         while j < len(l[i]):
#
#             if type(l[i][j]) == str:
#                 print(f"{l[i][j]} is present at index {i},{j}")
#             j += 1
#
#         j = 0
#
#         while j < len(l[i]):
#             if type(l[i][j]) == str:
#                 l[i].remove(l[i][j])
#                 continue
#
#             j+=1
#     i += 1
# print(l)






### 1 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 49

# l = [[i for i in range(3)] for i in range(3)]
# print(l)








### 1 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 49


# s = "hello bro hello bro bro bro bro hello hello gello hello i m here here"
# s = s.split()
# for i,item in enumerate(s):
#     j = i + 1
#     while j < len(s):
#         if item == s[j]:
#             s.pop(j)
#             if j != len(s) and s[j] == item:
#                 continue
#         j += 1
# d = {}
# d = d.fromkeys(s,'vivek')
# print(d)
# print(tuple(d.values()))
# print(list(d.keys()))






### 1 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 49

# def data_type(*k):
#     dt = {}
#     for i in k:
#         if type(i) in dt:
#             dt[type(i)].append(i)
#         else:
#             dt[type(i)] = [i]
#     return dt
# print(data_type(1,2.3,3+1j,[1,2,3,4],(1,2,3,4),{1,2,3,44,2},1,2,3,23.3))








### 1 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 49

# l1 = [j for i in [[1,2,3,4,5],[1,2,34,5,'hhkhh'],1,2,3,4,5,'jkh']  if type(i) == list for j in i if type(j) != int]
# a = []
# l = [[a.append(j) for j in i] if type(i) == list else a.append(i) for i in [["hello","mhi",'hiiwj f['],[1,9,99,19,10,11],1,2,3,4,5,6]]
# print(a)



