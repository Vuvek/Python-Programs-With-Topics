############  1 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# n = int(input("Enter the number of element : "))
# set1 = set()
# for i in range(n):
#     s = input(f"Enter the {i+1} element in the set : ")
#     if s.isdigit():
#         s = int(s)
#         set1.add(s)
#     elif s.isalnum():
#         set1.add(s)
#     else:
#         try:
#             s = float(s)
#             set1.add(s)
#         except:
#             pass
#         set1.add(s)
#
# print(set1)

############  2 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@




# s = set([1,2,3,4,5,6,7,8,9,10])
# for i in s:
#     print(i)




############  3 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# n = int(input("Enter the number of elements you want to add : "))
# set1 = set()
# for i in range(n):
#     s = input(f"Enter the {i+1} element in the set : ")
#     if s.isdigit():
#         s = int(s)
#         set1.add(s)
#     elif s.isalnum():
#         set1.add(s)
#     else:
#         try:
#             s = float(s)
#             set1.add(s)
#         except:
#             pass
#         set1.add(s)
# print(set1)




############  4 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# s = {1,2,3,4,"vivek",8,9,8.2}
# print(s)
# n = input("Enter the element you want to remove from the set :")
# i = 1
# flag = 0
# while True:
#     if i == 1:
#         i +=1
#     else:
#         Y_N = input("You want to remove more element from the set Y/N ? : ")
#         Y_N = Y_N.lower()
#         if Y_N == 'y':
#             n = input("Enter the element you want to remove from the set :")
#         elif Y_N == 'n':
#             break
#         else:
#             print("Invalid Input Please enter the Y/N")
#             continue
#     try:
#
#         if n.isdigit():
#             n = int(n)
#         elif n.isalnum():
#             pass
#         else:
#             n = float(n)
#         if n in s:
#             s.discard(n)
#         else:
#             flag = 1
#             raise Exception("Sorry! The element you want to remove is not present in the set ")
#     except Exception as e:
#         if flag == 1:
#             print(e)
#         else:
#             s.discard(n)
#
# print(f"After removing the element from the set {s}")





############  5 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# s = {1,2,3,4,5,6,7,8,9,10,'vivek','an'}
# print(s)
# n = input("Enter the string you want to remove from the set : ")
# if n.isdigit():
#     n = int(n)
# elif n.isalnum():
#     pass
# else:
#     n = float(n)
# if n in s:
#     s.discard(n)
#     print(s)
# else:
#     print("The element you want to remove from the set is not present in the set ")




############  6 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# s1 = {1,2,34,5,6,7,8}
# s2 = {2,34,8,9,10,11}
# print("Sets before intersection")
# print(s1)
# print(s2)
# print("Set after the intersection")
# s3 = s1 & s2                                  # you can use this also for intersection of the set elements
# s3 = s1.intersection(s2)
# print(s3)





############  7 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# s1 = {1,2,34,5,6,7,8}
# s2 = {2,34,8,9,10,11}
# print("Sets before intersection")
# print(s1)
# print(s2)
# print("Set after the intersection")
# # s3 = s1 | s2                                  # you can use this also for union of the set elements
# s3 = s1.union(s2)
# print(s3)





############  8 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# s1 = {1,2,34,5,6,7,8}
# s2 = {2,34,8,9,10,11}
# print("Sets before intersection")
# print(s1)
# print(s2)
# print("Set after the intersection")
# # s3 = s1 - s2                                  # you can use this also for set difference of the set elements
# s3 = s1.difference(s2)
# print(s3)





############  9 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# s1 = {1,2,34,5,6,7,8}
# s2 = {2,34,8,9,10,11}
# print("Sets before intersection")
# print(s1)
# print(s2)
# print("Set after the intersection")
# # s3 = s1 | s2                                  # you can use this also for intersection of the set elements
# s3 = s1.union(s2)
# print(s3)




############  10 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# s1 = {1,2,34,5,6,7,8}
# s2 = {2,34,8,9,10,11}
# print("Sets before intersection")
# print(s1)
# print(s2)
# print("Set after the intersection")
# s3 = s1.symmetric_difference(s2)
# print(s3)





############  11 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# s1 = {1,2,34,5,6,7,8}
# print(f"set s1 {s1}")
# s2 = s1.copy()
# s2.discard(8)
# print("After deleting the one element from the s2 ")
# print(f"set s1 {s1}")
# print(f"set s2 {s2}")





############  12 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# s1 = {1,2,34,5,6,7,8}
# print(f"set s1 {s1}")
# print("After clearing the elements of the set  ")
# s1.clear()
# print(f"set s1 {s1}")





############  13 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# # Frozen set are mutable set and To make frozen set we pass set frozen construntor
# x = frozenset([1,2,34,5,9,10])
# y = frozenset([3,46,56,8,8,9])
# print(x)
# print(y)
# print(x.symmetric_difference(y))





############  14 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# s1 = {1,2,34,5,6,7,8}
# print(f"Maximum value in the set {max(s1)} and  Minimum value in the set {min(s1)}")





############  14 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# s1 = {1,2,34,5,6,7,8,9,10,11,12,101}
# i = 0
# for item in s1:
#     i+=1
# print(f"Length of the set is {i}")




