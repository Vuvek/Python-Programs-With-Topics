### 1 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# import operator
# dict1 = {"a":123,"b":2,"c":332,"d":42,"e":225,"f":62,"g":7}
#
# Asc_dict = sorted(dict1.items() ,key = lambda x:x[1])
# print(Asc_dict)
#
# Desc_dict = sorted(dict1.items() ,key = operator.itemgetter(1) ,reverse=True)
# print(Desc_dict)





### 2 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# d = {0:10,1:20}
# print(d)
# d[2] = 30
# print(d)
# d.update({3:30})
# print(d)





### 3 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# dic1 = {1:10,2:20}
# dic2 = {3:30,4:40}
# dic3 = {5:50,6:60}
# dic4 = {}
# for d in dic1,dic2,dic3,dic4:
#     dic4.update(d)
# print(dic4)


### 4 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# dic3 = {5:50,6:60,7:70,8:80,9:90,10:100,11:110}
# d = int(input("Enter the key : "))
# if d in dic3:
#     print("key is present in dictionary")
# else:
#     print("key is not present in the dictionary")





### 5 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# dic3 = {5:50,6:60,"Name":"Vivek",7:70,8:80,9:90,"Roll":23,10:100,11:110}
# print(dic3)
# for i,val in dic3.items():
#     print(f"key is {i} and value is {val}")





### 6 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# dic = {i:i*i for i in range(1,int(input('Enter the number : '))+1)}
# print(dic)





### 7 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# l = [i+1 for i in range(int(input("Enter the number to print the square of number : ")))]
# dic = dict.fromkeys(l,)
# for i in dic:
#     dic[i] = i*i
#
# print(dic)





### 8 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# d1 = {1:10,2:20,3:30,4:40}
# d2 = {5:50,6:60,7:70,8:80}
# d3 = {}
# d3.update(d1)
# d3.update(d2)
# print(d3)





### 9 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# d1 = {1:10,2:20,3:30,4:40}
# for i in d1.items():
#     print(f"key {i[0]} --> value {i[1]}")






### 10 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# d1 = {1:10,2:20,3:30,4:40}
# key = int(input("Enter the key to remove the from dictionary : "))
# if key in d1:
#     d1.pop(key)
#     print(d1)
# else:
#     print("Key is not present in dictionary")





### 11 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# keys = ['A','B','C','D','E']
# values = ['Apple','Ball','Cat','Dog','Elephant']
# dict = dict(zip(keys,values))
# print(dict)





### 12 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# import operator
# d = {'E': 'Elephant', 'B': 'Ball', 'D': 'Dog', 'C': 'Cat', 'A': 'Apple'}
# d = sorted(d.items(),key = operator.itemgetter(0))
# print(d)






### 13 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def Removing_Duplicates_From_List(l):
#     d2 = {}
#     for key,val in l.items():
#         if val not in d2.values():
#             d2[key] = val
#     return d2
#
#
# d = {1:10,2:20,3:30,4:40,5:30,6:40}
# print(d)
# d = Removing_Duplicates_From_List(d)
# print(d)






### 14 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# d = {}
# if len(d) == 0:
#     print("Dictionary is empty ")
# else:
#     print("Dictionary is not empty")





### 16 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

d1 = {'a':100,'b':300,'c':100,'k':'kite'}
d2 = {'a':200,'b':20,'d':200,'e':'elephant'}
d3 = {}
for key,val in d1.items():
    for key1,val1 in d2.items():
        if key == key1:
            d3[key] = d1[key]+d2[key1]
        elif key1 not in d3 and key1 not in d1:
            d3[key1] = val1

else:
    d3[key] = val

print(d3)






### 17 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# d1 = {'item1':1234,'item2':232,'item3':345,'item4':899,'item5':233}
# d1 = sorted(d1.items(),key = lambda x:x[1],reverse=True)
# j = 0
# for i in d1:
#     if j < 3:
#         print(f"{i[0]} ---> {i[1]}")
#         j+=1
#     else:
#         break





### 18 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# d1 = {'a':100,'b':300,'c':100,'k':'kite'}
# d2 = {'a':100,'b':20,'d':200,'e':'elephant','c':100}
# print("The common key and values present in the both the dictionaries")
# for key,val in d1.items():
#     for key1,val1 in d2.items():
#         if key == key1 and val == val1:
#             print(f"{key} --> {val} ")















