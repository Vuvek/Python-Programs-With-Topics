###### 1 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# l = [f"{j} is even" if j %2 == 0 else f"{j} is odd" for j in [i for i in range(101)]]
# for i in l:
#     print(i)

##### 2 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


# l = [f"{int(j)} is even" if j %2 == 0 else f"{int(j)} is odd" for j in [i for i in range(100,0,-1)]]
# for i in l:
#     print(i,type(i))

##### 3 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# # l = [12,23,23,21,32,132,231]
# even = list(filter(lambda x:x%2==0,l))
# print(even)
# for i in even:
#     print(i)


########## 4 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# from functools import reduce
# l = [12,23,23,21,32,132,231]
# sum = reduce(lambda x,y:x+y,l)
# print(sum)



########### 4  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# sum = lambda x:x**2+sum(x-1) if x>1 else 1
# print(sum(5))

########## 5  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# fac = lambda x:x*fac(x-1) if x>1 else 1
# print(fac(5))


########## 6 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# k = 1
# for i in range(3):
#     for j in range(3):
#         if j+i>=3-1:
#             print(f"{k}",end = " ")
#             k+=1
#         else:
#             print(" ", end=" ")
#     print()


####### 7 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# for i in range(3):
#     for j in range(3):
#         if i>=j:
#             print(f"*",end = " ")
#     print()

###### 8 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


# for i in range(1,6):
#     k = 1
#     for j in range(1,6):
#         if j>=i:
#             print(f"{k}",end = " ")
#             k+=1
#
#     print()



########## 9 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

for i in range(1,5):
    for j in range(1,5):
        if i>=j:
            print(i,end = ' ')
    print()












