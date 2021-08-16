############# 1 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# count = 0
# def len_Using_recursion(str):
#     if str == "":
#         return 0
#     else:
#         return 1 + len_Using_recursion(str[1:])
#
# len = len_Using_recursion("Shobhit")
# print(len)




############### 2 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def frequency(str):
#     dict = {}
#     for i,j in enumerate(str):
#         if j in dict.keys():
#             dict[j] = dict[j] + 1
#         else:
#             dict[j] = 1
#
#     return dict
#
# d = frequency("vvvvvvviii")
# print(d)




########### 3 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def change(str):
#
#     Replace = input("Enter by which you wnat to replace : ")
#     list1 = str.split(" ")
#     list2 = []
#     for j in list1:
#         l = list(j)
#         first = l[0]
#         for i in range(1,len(l)):
#             if l[i] == first:
#                 l[i] = Replace
#         part =  "".join(l)
#         list2.append(part)
#     return " ".join(list2)
#
# x = input("Enter the string : ")
# y = change(x)
# print(y)


## By second method 2nd question

# def change(str):
#     s = ""
#     for i,j in enumerate(str):
#         if j == str[0] and i != 0:
#             s = s + "$"
#         else:
#             s = s + j
#     return s
#
# print(change("vivekvv"))




############ 4 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def swap(s1,s2):
#     x1 = s1[0:2]
#     x2 = s1[2:]
#     y1 = s2[0:2]
#     y2 = s2[2:]
#     s = y1+x2+x1+y2
#     print(s)
#
# swap("abc",'xyz')




####### 5 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def add(str):
#     l = len(str)
#     if l >= 3 and not str.endswith("ing"):
#         str = str+"ing"
#     elif l>=3 and str.endswith("ing"):
#         str = str+"ly"
#     else:
#         pass
#     return str
#
# print(add((input("Enter the string : "))))




######### 6 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def check(str):
#     try:
#         n = str.index("not")
#         p = str.rindex("poor")
#         s = str[n:p+4]
#         str = str.replace(f"{s}","good")
#     except:
#         pass
#     else:
#         return str.replace(f"{s}","good")
#     return str
#
# print(check(input("Enter the string : ")))




######### 7 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def Largest_length_list(l):
#     l3 = []
#     for i in l:
#         l3.append(len(i))
#     i = l3.index(max(l3))
#     return l[i],max(l3)

# l = ['Shobhit','Deepak','Avni','Vivek']
# string,max_length = Largest_length_list(l)
# print(f"{max_length} is the max length of {string} word in list l")




######## 8 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def swap_firs_and_last_char(str):
#     list_str = list(str)
#     list_str[0],list_str[-1] = list_str[-1],list_str[0]
#     str = "".join(list_str)
#     return str

# print(f"{swap_firs_and_last_char(input('Enter a string : '))} after swapping first and last letter")




######## 9 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def odd_index_remover(str):
#     s = ''
#     for i,j in enumerate(str):
#         if i%2 != 0 or j == ' ':
#             s =  s + j
#     return s
#
# print(f"{odd_index_remover(input('Enter a string : '))} after removing odd index but living index as it is if present")




######### 10 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def count_occurence(str):
#     s = set(str)
#     for i in s:
#         count = 0
#         for j in str:
#             if i == j:
#                 count+=1
#         else:
#             print(f"frequency of {i} -------> {count}")
#
# count_occurence(input('Enter the string : '))




######### 11 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def upper_lower(str):
#     s =  ''
#     for i in str:
#         if i.isupper():
#             s = s + i.lower()
#         elif i.islower():
#             s = s + i.upper()
#         else:
#             s = s + i
#     return s
#
# print(f"{upper_lower(input('Enter the string : '))} ")




########## 12 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def sort_comma_seprated(str):
#     l = str.split(',')
#     l.sort()
#     str = " ".join(l)
#     return str
#
# s = input('Enter the comma seprated string : ')
# sort = sort_comma_seprated(s)
# print(sort)




########## 13 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def Insert_middle(str):
#     l = len(str)//2
#     first_half = str[0:l:]
#     second_half = str[l:]
#     i = input('Enter the string to insert in the middle :')
#     str = first_half + i + second_half
#     return str
#
# s = Insert_middle(input("Enter the string : "))
# print(s)




########## 14 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def Insert_end(str):
#     try:
#         if len(str) < 2:
#             raise Exception
#         end = str[-2:]
#         str = end * 4
#         return str
#     except:
#         print('Length of string must greater than or equal to two')
#         exit(0)
#
# s = input("Enter the string : ")
# str = Insert_end(s)
# print(str)




########## 15 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def first_three(str):
#     try:
#         if len(str) < 3:
#             raise Exception
#         str = str[0:3]
#         return str
#     except:
#         return str
#
# s = first_three(input("Enter the String : "))
# print(s)




########## 16 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# str = input("enter the string : ")
# c = input("Enter the specified charchter : ")
# l = str.split(f"{c}")[0]
# print(l)




########## 17 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def reverse_if_multiple_4(str):
#     l = len(str)
#     if l % 4 == 0:
#         str = str[::-1]
#         return str
#     else:
#         return str
# s = reverse_if_multiple_4(input("Enter the string : "))
# print(s)




########## 18 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def Upper_case(str):
#     s = str[:4]
#     j = 1
#     for i in s:
#         if i.isupper():
#             if j == 2:
#                 return str.upper()
#             j += 1
#         else:
#             pass
#     else:
#         return str
#
# str1 = Upper_case(input("Enter the string : "))
# print(str1)




########## 19 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def lexicographically(s):
#     return sorted(s,key = str.upper)
#
# s = lexicographically(input("Enter the string : "))
# print(s)




########## 20 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def Remove_new_lines(str):
#     str = str.replace(r"\n","")
#     return str
#
# s = Remove_new_lines(input("Enter the string : "))
# print(s)




########## 21 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def Starts_with_or_not(str,c):
#     return str.startswith(c)
# print(Starts_with_or_not(input("Enter the the string  : "),input("Etner the specified character :")))




########## 22 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def Count_Occurance(str,sub_str):
#     return str.split().count(sub_str)
#
# print(Count_Occurance(input("Enter the string : "),input("Etner the substring to count the occurance : ")))




########## 23 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# str = input("Entr the string to reverse : ")
# str = str[-1::-1]
# print(str)




########## 24 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def reverse_word(str):
#     l = str.split()
#     for j,i in enumerate(l):
#         i = i[-1::-1]
#         l[j] = i
#     return " ".join(l)
# print(reverse_word(input("Enter the sentence to reverse the words : ")))




########## 25 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def strip_string(str,strip):
#     l = str.split()
#     list1 = []
#     for i in l:
#         for j in strip:
#             i = i.replace(f'{j}','')
#         list1.append(i)
#     str = " ".join(list1)
#     return str
#
# s = input("Enter the string :  ")
# strip = input("enter the words you want to strip in the string ")
# print(f"{strip_string(s,strip)} after striping {','.join(list(strip))}")




#### 26 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def counter(str):
#     l = list(str)
#     dictt = {}
#     s = set(str)
#     print(s)
#     for i in s:
#         c = l.count(i)
#         if c>1:
#             dictt[i] = c
#     return dictt
#
#
# s = input("Enter the string  : ")
# str1 = counter(s)
# for i,j in str1.items():
#     print(f"{i} ---> {j}")




#### 27 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def index_counter(str):
#     for i,j in enumerate(str):
#         print(f"Current Current {j} Position at {i}")
#
# s = input("Enter the string : ")
# d = index_counter(s)




#### 28 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def All_letter(str):
#
#
# str = input("Enter the string : ")
# print(All_letter(str))




#### 29 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def Convert_in_string(str):
#         s = str[1:-1].split(",")
#         for i,j in enumerate(s):
#             f = str[1]
#             if j[0] == '"' and j[-1] == '"' and j[0] == f and str[0] == "[" and str[-1] == "]":
#                 s[i] = j.strip('"')
#
#             elif j[0] == "'" and j[-1] == "'" and j[0] == f and str[0] == "[" and str[-1] == "]":
#                 s[i] = j.strip("'")
#
#             else:
#                 try:
#                     raise Exception
#                 except:
#                     print(f"Something is going wrong please check you are doing something wrong")
#                     exit(0)
#
#         return s
# str = input("Enter the string : ")
# print(Convert_in_string(str))





#### 30 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def First_n_lower(str,n):
#     s1,s2 = str[:n],str[n:]
#     s1 = s1.lower()
#     str = s1+s2
#     return str
#
#
# n = int(input("enter the number to which you want to lower the starting chars :"))
# s = input("enter the string :")
# print(First_n_lower(s,n))




#### 31 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def Swap_Coma_dot(str):
#     str = str.replace(",","'")
#     str = str.replace(".",",")
#     str = str.replace("'",".")
#     return str
#
# s = input("Enter the string : ")
# st = Swap_Coma_dot(s)
# print(st)




#### 32 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# import re
# def count_and_display_vowel(str):
#     S = re.findall("[aioueAEIOU]",str)
#     l = len(S)
#     str = set(S)
#     return (str,l)
#
# s = count_and_display_vowel(input("Enter the string : "))
# print(f"Total {s[1]} Vowels present in the string are {s[0]}")




#### 33 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# import re
# def split_on_last_occurance(str):
#     string = str[-1::-1]
#     sep = re.search("[^a-zA-Z ]",string).group()
#     print(sep)
#     l = str.rsplit(f'{sep}',1)
#     return l
#
# print(split_on_last_occurance(input("Enter the string : ")))



#### 34 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def First_Non_Repeating_Character(str):
#     s = set(str)
#     for i,j in enumerate(str):
#         for k in range(len(str)):
#             if i != k:
#                 if str[i] == str[k]:
#                     break
#         else:
#             return j
#     else:
#         return False
#
# str = First_Non_Repeating_Character(input('Enter the string : '))
# if str:
#     print(f"{str} is the First non repeating character in the string ")
# else:
#     print("All characters are repeating in this string")




#### 35 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@






















#### 36 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def First_Repeating_Character(str):
#     s = set(str)
#     for i,j in enumerate(str):
#         for k in range(len(str)):
#             if i != k:
#                 if str[i] == str[k] and j!=' ':
#                     return j
#     else:
#         return False
#
# str = First_Non_Repeating_Character(input('Enter the string : '))
# if str:
#     print(f"{str} is the First repeating character in the string ")
# else:
#     print("All characters are non repeated in this string")


## by second method

# def First_Repeated_Character(str):
#     d = {}
#     list_unique = []
#     for i in str:
#         if i in d:
#             d[i] +=1
#         else:
#             d[i] = 1
#             list_unique.append(i)
#
#     for i in list_unique:
#         if d[i] > 1:
#             return i
#     else:
#         return False
#
# str = First_Repeated_Character(input('Enter the string : '))
# if str:
#     print(f"{str} is the First repeating character in the string ")
# else:
#     print("All characters are non repeated in this string")




#### 37 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def First_Repeated_Character(str):
#     d = {}
#     list_unique = []
#     for i in str:
#         if i in d:
#             d[i] +=1
#         else:
#             d[i] = 1
#             list_unique.append(i)
#
#     l = [f"{str.index(i,str.index(i)+1)}" for i,j in d.items() if j >1]
#     min_index_of_first_occurance = min(l)
#     return str[int(min_index_of_first_occurance)]
#
#
# str = First_Repeated_Character(input('Enter the string : '))
# if str:
#     print(f"{str} is the First repeating character in the string where index of first occurance is smallest ")
# else:
#     print("All characters are non repeated in this string")


#### 38 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def first_reapeted_word_in_string(str):
#     list_str = str.split(" ")
#     for word in list_str:
#         word_len = len(word)
#         if str.find(word,str.index(word)+1) == -1:
#             pass
#         else:
#             return word
#
# word = first_reapeted_word_in_string(input('Enter the string : '))
# if  word:
#     print(f"{word} is the first repeated character in the string")
# else:
#     print("There is no reapeated word in the string ")




#### 39 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# import  operator
# def Second_most_repeated_word(str):
#     dict = {}
#     for word in set(str.split(" ")):
#         count = 0
#         for i in str.split(" "):
#             if i == word:
#                 count += 1
#         dict[word] = count
#
#
#     length_of_dict = len(dict)
#     print(dict)
#     if length_of_dict >=2:
#         return f"{sorted(dict.items(),key = operator.itemgetter(1),reverse=True)[1][0]} is the second most repeated word in the string"
#     elif length_of_dict == 1:
#         return f"There is no second most repeated word in the string but only one repeated word presnet and this word is ---> {sorted(dict.items(),key = operator.itemgetter(1),reverse=True)[0][0]}"
#     else:
#         return False
#
#
# word = Second_most_repeated_word(input('Enter the string : '))
# if  word:
#     print(word)
# else:
#     print("There is no reapeated word in the string ")




#### 40 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def Remove_spaces(str):
#     l = str.split(" ")
#     str = "".join(l)
#     return str
#
# print(Remove_spaces(input("Enter the string to remove all the space from the string : ")))




#### 41 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def Move_space_front_of_string(str):
#     s = str.count(" ")
#     str = " "* s + "".join(str.split())
#     return str
#
# print( Move_space_front_of_string(input("enter the string : ")))




#### 42 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# import operator
# def Maximum_occuring_character(str):
#     d = {}
#     for i in str:
#         if i in d.keys():
#             d[i] += 1
#         else:
#             d[i] = 1
#
#     d = sorted(d.items(),key=operator.itemgetter(1),reverse=True)[0][0]
#     return d
#
# print(Maximum_occuring_character(input("Enter the string : ")),"is the most repeted charcater in string")




### 43 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def Capitalize_First_Last_Character(str):
#     l = str.split(" ")
#     l1 = []
#     for i in l:
#         if len(i) > 1:
#             s = i[0].upper() + i[1:-1] + i[-1].upper()
#         elif len(i) == 1:
#             s = i.upper()
#         l1.append(s)
#
#     str = " ".join(l1)
#     return str
#
# print(Capitalize_First_Last_Character(input("Enter the string : ")))




### 44 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# from collections import OrderedDict
# def Remove_duplicate_character(str):
#     return "".join(OrderedDict.fromkeys(str))
#
#
# print(Remove_duplicate_character(input("Enter the sting: ")))

# second method

# def Remove_duplicate_character(str):
#     l = []
#     for i in str:
#         if i in l:
#             pass
#         else:
#             l.append(i)
#     return "".join(l)
#
# print(Remove_duplicate_character(input("Enter the sting: ")))



### 45 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# name = input("Enter you first name : ")
# print(name)




### 46 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# name = input("Enter you full name : ")
# print(name)





### 47 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# str = input("Enter the string : ")
# if 'a' in str:
#     print(f"{str} contains the character a")
# else:
#     print(f"{str} --> do not contain a in the string")




### 48 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# str = input("Entr the string : ")
# c = 0
# for o in str:
#     if o == 'o' in str:
#         c +=1
#     else:
#         pass
# if c == 0:
#     print("o is not present in the entered string")
# elif c>0:
#     print(f"o present {c} times in the string ")




### 49 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# str = input("Enter the string : ")
# str = str[-1::-1]
# print(str)




### 50 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# str = input("Etner the string : ")
# vowel = 'AEIOUaeiou'
# for i in str:
#     if i in vowel:
#         print(i,end = ',')




### 51 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# str = input("Enter the string : ")
# if str == str[-1::-1]:
#     print("String is palindrome string")
# else:
#     print("String is not palindrome string")





### 52 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# string = input("Enter the string : ")
# sub_string = input("Enter the substring : ")
# len = len(sub_string)
# try:
#     index = string.index(sub_string)
#     print(string[index:len+1])
# except:
#     print("Sub string is not present in the string ")





### 53 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# str = input("Enter the string : ")
# s = ''
# vowel = "aeiouAEIOU"
# for i in str:
#     if i in vowel and len(str) == 15:
#         pass
#     else:
#         if len(str) == 15:
#             s = s+i
#         else:
#             s = s + i
# print(s)








