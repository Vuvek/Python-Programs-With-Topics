### 1 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# with open('Regual expression.py','r') as f:
#     print(f.read())



### 2 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# with open('Regual expression.py','r') as f:
#     n = int(input("Enter the number of lines you want to read from the file : "))
#     for i in range(n):
#         text = f.readline()
#         if text == "":
#             print("\nNo more lines present in the file")
#             break
#         else:
#             print(text, end="")






### 3 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
f = open("hello.txt",'a+')
f.write(" Hello bro")
f.seek(0)
print(f.read())
f.close()
'''






### 4 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
f = open("hello.txt",'r+')
text = f.read()
lines = text.splitlines()
n_line = int(input("Enter how many last n lines you want to read : "))
l = len(lines)-1
for line in lines[-1:-(n_line+1):-1]:
    print(line)
f.close()
'''





### 5 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
f = open("hello.txt",'r')
l = []
text = f.read()
for line in text.split('\n'):
    l.append(line)

print(l)
'''





### 6 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
f = open("hello.txt",'r')
text = f.readlines()
text = [x.replace("\n","") for x in text]
print(text)
f.close()
'''






### 8 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
f = open("hello.txt",'r')
text = f.read().split()
print(text)
max_len = len(max(text,key = len))
print([word for word in text if len(word) == max_len])
'''





### 9 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
f = open("hello.txt",'r+')
s = 'Indore\n'
text = f.readlines()
l = 0
for x in text:
    print(x)
    l+=len(x)
    if x == "":
        break
    elif x == s:
        f.seek(l-len(s)+1,0)
        f.write("INDORE")
        break
f.close()
'''






### 10 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
with open("hello.txt") as f:
    text = f.read()
    text = text.splitlines()
    lines = len(text)
    print("Total Lines = ",lines)
'''






### 11 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
with open("hello.txt") as f:
    text = f.read()
    dict1 = {}
    for i in text.split():
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    print("Frequency of all the words present in the file : ")
    for key,value in dict1.items():
        print("{:2s}    -----    {:10d}".format(str(key),int(value)))
'''







### 12 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
import os
info = os.stat("hello.txt")
print(info.st_size)
'''






### 13 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
l = ["hello","bro","I","Am","Here","To","Help","You","Out","From","This","HOw","Are","You"]
#Writing list in the file
import pickle
pickle.dump(l,open("list.pkl","wb"))
# Reading list from the file
l = pickle.load(open("list.pkl","rb"))
for i in l:
    print(i,end = "  ")
'''






### 14 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
with open("hello.txt") as f:
    text = f.read()
    with open("hello1.txt","w") as f:
        f.write(text)
        print("Content written of one file to another file")
'''






### 15 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
with open('hello.txt','r') as f1,open('hello1.txt','r') as f2:
    for line1,line2 in zip(f1,f2):
        print(line1+line2)
'''



'''
with open('hello.txt','r') as f1:
    lines = f1.readlines()

with open('hello1.txt','r') as f2:
    lines1 = f2.readlines()

for i in zip(lines,lines1):
    print(i)
'''







### 16 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
import random

def random_line(fname):
    lines = open(fname,'r').read().splitlines()
    return random.choice(lines)

line = random_line('hello.txt')
print(line)
'''






### 17 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
f = open('hello.txt','r')
print(f.closed)
f.close()
print(f.closed)
'''







### best code @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
import os
import shutil
import pickle

if not os.path.isdir("vivek"):
    os.mkdir('vivek')
else:
    print("this directory is already exist")

l = []
for i in range(1,11):
    f = open(f"vivek\\file{i}.txt",'w+')
    f.write("hello bro what are you doing \nI am here to help you out")
    f.seek(0)
    l.append(f.read())
    f.close()

for i in l:
    print(i)

f = open(f"vivek\\list.pkl",'wb')
pickle.dump(l,f)
f.close()

if os.path.isdir("all_fles"):
    os.mkdir("E:\\all_fles")
    
else:
    print("Directory already exist")

l = os.listdir("vivek")

for i in l:
    if not i in "list.pkl":
        shutil.move(f"vivek\\{i}",f"E:\\all_fles\\{i}")
'''









### 18 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
f = open("hello.txt",'r')
data = f.read().split("\n")
data = [i.replace("\n","") for i in data if i != ""]
f.close()
for i in data:
    print(i,end = "  " )
'''







### 19 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
f = open('hello.txt','r')
words = f.read()
words = words.replace(","," ")
words = words.split()
print(words)
print(len(words))
for i in words:
    print(i)
'''









### 20 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
import glob,csv
char_list = []
file_list = glob.glob("*.txt")
print(len(file_list))
print(file_list)
for i in file_list:
    with open(i,'r') as f:
        d = f.read()
        char_list.append(d)

# char_list = [i.replace("\n","") for i in char_list]
print(char_list)
'''






### 21 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
import string
import os
alphabets = string.ascii_uppercase
if not os.path.isdir("Alphabetic_names_files"):
    os.mkdir('Alphabetic_names_files')
else:
    print('file exist')
for i in alphabets:
    f = open(f'Alphabetic_names_files\{i}.txt','w')
    f.write("hello my name unbreakable man")
    f.close()
'''








### 22 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

import string
user = int(input("Enter the number the number : "))
alphabets = string.ascii_uppercase
f = open("All_characters.txt", 'w')

for i in range(0,len(alphabets),user):
    f.write(alphabets[i:i+user]+'\n')
f.close()








    





















