# Python Pattern Programs

### 1 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
'''
*****
*****
*****
*****
'''

# for x in range(1,6):
#     for y in range(1,6):
#         print("*",end = " ")
#     print()





### 2 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
'''
11111
22222
33333
44444
'''

# for x in range(1,6):
#     for y in range(1,6):
#         print(x,end = " ")
#     print()





### 3 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
'''
1234
1234
1234
1234
'''

# for x in range(1,6):
#     for y in range(1,6):
#         print(y,end = " ")
#     print()





### 4 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
'''
55555
44444
33333
22222
'''

# for x in range(5,0,-1):
#     for y in range(1,6):
#         print(x,end = " ")
#     print()





### 5 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
'''
54321
54321
54321
54321
'''

# for x in range(1,6):
#     for y in range(5,0,-1):
#         print(y,end = " ")
#     print()





### 6 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
'''
 1  2  3  4  5
 6  7  8  9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
'''

# j = 1
# for x in range(1,6):
#     for y in range(1,6):
#         # print(j,end = " ")
#         print("{:3d}".format(j),end = " ")
#         j+=1
#     print()


### Here we learning about formating string

'''
This technique is okay for simple formatting but what if you want to specify precision in floating point number?
For such thing you need to learn more about format codes. Here is the full syntax of format codes.

Syntax: {[argument_index_or_keyword]:[width][.precision][type]}

Format codes	Description
  d	          for integers
  f	          for floating point numbers
  b	          for binary numbers
  o	          for octal numbers
  x	          for octal hexadecimal numbers
  s	          for string
  e	          for floating point in exponent format

for x in range(1,11):
    print('{:2d} {:3d} {:4d}'.format(x,x**2,x**3))

for x in range(1,11):
    print('{0:2d} {1:3d} {2:4d}'.format(x,x**2,x**3))
    
    
>>> "Floating point {0:.2f}".format(345.7916732)
Here we specify 2 digits of precision and f is used to represent floating point number.
'''





### 7 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
 1  3  5  7  9 
11 13 15 17 19 
21 23 25 27 29 
31 33 35 37 39 
41 43 45 47 49 
'''

# i = list(range(1,50,2))
# j = 0
# for x in range(0,5):
#     for y in range(0,5):
#         print("{:2d}".format(i[j]),end = " ")
#         j+=1
#     print()






### 8 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
 2  4  6  8 10 
12 14 16 18 20 
22 24 26 28 30 
32 34 36 38 40 
42 44 46 48 50
'''

# i = 2
# for x in range(0,5):
#     for y in range(0,5):
#         print("{:2d}".format(i),end = " ")
#         i +=2
#     print()







### 9 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
 1  2  3  4  5 
 6  7  8  9 10 
11 12 13 14 15 
16 17 18 19 20 
21 22 23 24 25  
'''

# i = 1
# for x in range(0,5):
#     for y in range(0,5):
#         print("{:2d}".format(i),end = " ")
#         i +=1
#     print()






### 10 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
1 1 2 1 3 1 
1 2 2 2 3 2 
1 3 2 3 3 3 
1 4 2 4 3 4 
1 5 2 5 3 5  
'''

# for x in range(1,6):
#     for y in range(1,4):
#         print("{} {}".format(y,x),end = " ")
#     print()






### 10 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
1 1 1 2 1 3 
2 1 2 2 2 3 
3 1 3 2 3 3 
4 1 4 2 4 3 
5 1 5 2 5 3   
'''

# for x in range(1,6):
#     for y in range(1,4):
#         print("{} {}".format(x,y),end = " ")
#     print()






### 11 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
1 1 1 2 1 3 
2 1 2 2 2 3 
3 1 3 2 3 3 
4 1 4 2 4 3 
5 1 5 2 5 3   
'''

# for x in range(1,6):
#     for y in range(1,4):
#         print("{} {}".format(x,y),end = " ")
#     print()






### 12 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
 1  6 11 16 21 
 2  7 12 17 22 
 3  8 13 18 23 
 4  9 14 19 24 
 5 10 15 20 25   
'''

# n = 5
# for x in range(1,n+1):
#     p = x
#     for y in range(1,n+1):
#         print("{:2d}".format(p),end = " ")
#         p+=n
#     print()






### 13 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
 1 10 11 20 21 
 2  9 12 19 22 
 3  8 13 18 23 
 4  7 14 17 24 
 5  6 15 16 25   
'''

# n = 5
# for x in range(1,n+1):
#     p1 = x
#     p2 = n - x + 1
#     for y in range(1,n+1):
#         if y%2 == 1:
#             print("{:2d}".format(p1),end = " ")
#         else:
#             print("{:2d}".format(p2),end = " ")
#         p1 = p1 + n
#         p2 = p2 + n
#     print()







### 14 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
 5 10 15 20 25 
 4  9 14 19 24 
 3  8 13 18 23 
 2  7 12 17 22 
 1  6 11 16 21   
'''


# n = 5
# i = 0
# for x in range(1,n+1):
#     q = n
#     p = q
#     for y in range(1,n+1):
#         print("{:2d}".format(p-i),end = " ")
#         p+=q
#     i +=1
#     print()



'''
def function_decorator(fun):
    def wrapper():
        print("Hello")
        fun()
    print("helo")
    return wrapper


@function_decorator
def show():
    print("In show")

show()
'''


### 15 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
 5  6 15 16 25 
 4  7 14 17 24 
 3  8 13 18 23 
 2  9 12 19 22 
 1 10 11 20 21  
'''


# n = 5
# for x in range(1,n+1):
#     p1 = x
#     p2 = n - x +1
#     for y in range(1,n+1):
#         if y%2 == 0:
#             print("{:2d}".format(p1),end = " ")
#         else:
#             print("{:2d}".format(p2),end = " ")
#         p1 = p1 + n
#         p2 = p2 + n
#     print()






### 16 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
 1  2  3  4  5 
 2  3  4  5  6 
 3  4  5  6  7 
 4  5  6  7  8 
 5  6  7  8  9  
'''

# i = 0
# n = 5
# for x in range(1,n+1):
#     p = 1
#     p = p + i
#     for y in range(1,n+1):
#         print("{:2d}".format(p),end = " ")
#         p+=1
#     i += 1
#     print()






### 17 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
 1  3  5  7  9 
 3  5  7  9 11 
 5  7  9 11 13 
 7  9 11 13 15 
 9 11 13 15 17 
'''

# i = 0
# n = 5
# for x in range(1,n+1):
#     p = 1
#     p = p + i
#     for y in range(1,n+1):
#         print("{:2d}".format(p),end = " ")
#         p+=2
#     i += 2
#     print()






### 18 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
 0  1  0  1  0 
 1  0  1  0  1 
 0  1  0  1  0 
 1  0  1  0  1 
 0  1  0  1  0 
'''

# n = 5
# i = 0
# for x in range(1,n + 1):
#     for y in range(1,n+1):
#         if i % 2 == 0:
#             p = 0
#         else:
#             p = 1
#         print("{:2d}".format(p),end = " ")
#         i += 1
#     print()






### 19 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
 1  0  1  0  1 
 0  1  0  1  0 
 1  0  1  0  1 
 0  1  0  1  0 
 1  0  1  0  1 
'''

# n = 5
# for x in range(1,n + 1):
#     for y in range(1,n+1):
#         print("{:2d}".format((x+y+1)%2),end = " ")
#     print()






### 20 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
 1  0  1  0  1 
 0  0  0  0  0 
 1  0  1  0  1 
 0  0  0  0  0 
 1  0  1  0  1 
'''

# By first logic
# n = 5
# i = 0
# for x in range(1,n + 1):
#     for y in range(1,n+1):
#         if i % 2 == 0:
#             print("{:2d}".format((x+y+1)%2),end = " ")
#         else:
#             print("{:2d}".format(0), end=" ")
#     i += 1
#     print()

# By second logic

# n = 5
# for x in range(1,n + 1):
#     for y in range(1,n+1):
#         print("{:2d}".format((x*y)%2),end = " ")
#     print()








### 21 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
 0  1  0  1  0 
 0  0  0  0  0 
 0  1  0  1  0 
 0  0  0  0  0 
 0  1  0  1  0 
'''
# n = 5
# for x in range(1,n + 1):
#     for y in range(0,n):
#         print("{:2d}".format((x*y)%2),end = " ")
#     print()






### 22 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
 0  0  0  0  0 
 1  1  1  1  1 
 0  0  0  0  0 
 1  1  1  1  1 
 0  0  0  0  0  
'''

# n = 5
# for x in range(0,n):
#     for y in range(1,n+1):
#         print("{:2d}".format(x%2),end = " ")
#     print()






### 23 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
 1  1  1  1  1 
 0  0  0  0  0 
 1  1  1  1  1 
 0  0  0  0  0 
 1  1  1  1  1 
'''

# n = 5
# for x in range(1,n+1):
#     for y in range(1,n+1):
#         print("{:2d}".format(x%2),end = " ")
#     print()






### 24 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
 0  1  0  1  0 
 0  1  0  1  0 
 0  1  0  1  0 
 0  1  0  1  0 
 0  1  0  1  0 
'''

# n = 5
# for x in range(1,n+1):
#     for y in range(0,n):
#         print("{:2d}".format(y%2),end = " ")
#     print()






### 25 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
 1  0  1  0  1 
 1  0  1  0  1 
 1  0  1  0  1 
 1  0  1  0  1 
 1  0  1  0  1 
'''

# n = 5
# for x in range(1,n+1):
#     for y in range(1,n+1):
#         print("{:2d}".format(y%2),end = " ")
#     print()






### 26 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
 1  0  1  0  1 
 1  0  1  0  1 
 1  0  1  0  1 
 1  0  1  0  1 
 1  0  1  0  1 
'''

# n = 2
# for i in range(65,65+n):
#     for j in range(65,65+n):
#         print("{:2s}".format(chr(i)),end = " ")
#     print()






### 27 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
A  B  C  D  E  
A  B  C  D  E  
A  B  C  D  E  
A  B  C  D  E  
A  B  C  D  E  
'''

# n = 5
# for i in range(65,65+n):
#     for j in range(65,65+n):
#         print("{:2s}".format(chr(j)),end = " ")
#     print()






### 28 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
E  E  E  E  E  
D  D  D  D  D  
C  C  C  C  C  
B  B  B  B  B  
A  A  A  A  A  
'''

# n = 5
# for i in range(65+n-1,64,-1):
#     for j in range(65+n-1,64,-1):
#         print("{:2s}".format(chr(i)),end = " ")
#     print()







### 29 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
E  D  C  B  A  
E  D  C  B  A  
E  D  C  B  A  
E  D  C  B  A  
E  D  C  B  A  
'''

# n = 5
# for i in range(65+n-1,64,-1):
#     for j in range(65+n-1,64,-1):
#         print("{:2s}".format(chr(j)),end = " ")
#     print()







### 30 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
A  B  C  D  E  
F  G  H  I  J  
K  L  M  N  O  
P  Q  R  S  T  
U  V  W  X  Y  
'''

# n = 5
# x = 65
# for i in range(65+n-1,64,-1):
#     for j in range(65+n-1,64,-1):
#         print("{:2s}".format(chr(x)),end = " ")
#         x+=1
#     print()






### 31 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
A  B  C  D  E  
B  C  D  E  F  
C  D  E  F  G  
D  E  F  G  H  
E  F  G  H  I 
'''

# n = 5
# for i in range(65,65+n):
#     y = i
#     for j in range(y,y+n):
#         print("{:2s}".format(chr(j)),end = " ")
#     print()






### 32 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
A  F  K  P  U  
B  G  L  Q  V  
C  H  M  R  W  
D  I  N  S  X  
E  J  O  T  Y
'''

# n = 5
# for i in range(65,65+n):
#     p = i
#     for j in range(65,65+n):
#         print("{:2s}".format(chr(p)),end = " ")
#         p = p + 5
#     print()







### 33 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
E  J  O  T  Y  
D  I  N  S  X  
C  H  M  R  W  
B  G  L  Q  V  
A  F  K  P  U 
'''

# n = 5
# i = n
# for x in range(65+n-1,65-1,-1):
#     p  = x
#     for y in range(65+n-1,65-1,-1):
#         print("{:2s}".format(chr(p)),end = " ")
#         p+=i
#     print()






### 34 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
*  
*  *  
*  *  *  
*  *  *  *  
*  *  *  *  *
'''

# n = 5
# for x in range(1,n+1):
#     for y in range(1,x+1):
#         print("{:2s}".format("*"),end = " ")
#     print()





### 35 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
 1 
 2  2 
 3  3  3 
 4  4  4  4 
 5  5  5  5  5
'''

# n = 5
# for x in range(1,n+1):
#     for y in range(1,x+1):
#         print("{:2s}".format(f"{x}"),end = " ")
#     print()







### 36 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
 1 
 1  2 
 1  2  3 
 1  2  3  4 
 1  2  3  4  5 
'''

# n = 5
# for x in range(1,n+1):
#     for y in range(1,x+1):
#         print("{:2d}".format(y),end = " ")
#     print()






### 37 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
 5 
 4  4 
 3  3  3 
 2  2  2  2 
 1  1  1  1  1  
'''

# n = 5
# for x in range(n,0,-1):
#     for y in range(n,x-1,-1):
#         print("{:2d}".format(x),end = " ")
#     print()



### 38 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
 5 
 5  4 
 5  4  3 
 5  4  3  2 
 5  4  3  2  1 
'''

# n = 5
# for x in range(n,0,-1):
#     for y in range(n,x-1,-1):
#         print("{:2d}".format(y),end = " ")
#     print()







### 39 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
 5 
 4  5 
 3  4  5 
 2  3  4  5 
 1  2  3  4  5 
'''

# n = 5
# for x in range(n,0,-1):
#     for y in range(x,n+1,1):
#         print("{:2d}".format(y),end = " ")
#     print()






### 40 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
 2 
 2  4 
 2  4  6 
 2  4  6  8 
 2  4  6  8 10 
'''

# n = 5
# n = n*2+1
# for x in range(2,n,2):
#     for y in range(2,x+1,2):
#         print("{:2d}".format(y),end = " ")
#     print()








### 41 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
 1 
 2  3 
 4  5  6 
 7  8  9 10 
11 12 13 14 15 
'''

# n = 5
# i = 1
# for x in range(1,n+1):
#     for y in range(i,x+i):
#         print("{:2d}".format(y),end = " ")
#         i+=1
#     print()



### 42 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
 1 
 2  3 
 3  4  5 
 4  5  6  7 
 5  6  7  8  9 
'''

# n = 5
# for x in range(1,n+1):
#     for y in range(x,x+x):
#         print("{:2d}".format(y),end = " ")
#     print()








### 43 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
 1 
 3  5 
 5  7  9 
 7  9 11 13 
 9 11 13 15 17 
'''

# n = 5
# n = n*2
# for x in range(1,n+1,2):
#     for y in range(x,x+x,2):
#         print("{:2d}".format(y),end = " ")
#     print()








### 44 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
 1 
 3  2 
 6  5  4 
10  9  8  7 
15 14 13 12 11 
'''

# n = 5
# i = 0
# for x in range(1,n+1):
#     for y in range(x+i,i,-1):
#         print("{:2d}".format(y),end = " ")
#         i +=1
#     print()







### 45 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
 1 
 3  5 
 7  9 11 
13 15 17 19 
21 23 25 27 29 
'''

# n = 6
# i = 1
# for x in range(1,n+1):
#     for y in range(1,x+1):
#         print("{:2d}".format(i),end = " ")
#         i+=2
#     print()







### 46 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
 2 
 4  6 
 8 10 12 
14 16 18 20 
22 24 26 28 30 
'''

# n = 5
# i = 2
# for x in range(1,n+1):
#     for y in range(1,x+1):
#         print("{:2d}".format(i),end = " ")
#         i+=2
#     print()







### 47 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
 1 
 2  4 
 3  6  9 
 4  8 12 16 
 5 10 15 20 25 
'''

# n = 5
# for x in range(1,n+1):
#     first = x
#     for y in range(1,x+1):
#         print("{:2d}".format(first),end = " ")
#         first+=x
#     print()








### 48 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
 1 
 6  2 
10  7  3 
13 11  8  4 
15 14 12  9  5 
'''

# n = 5
# i = 1
# m = 0
# for x in range(n+1,1,-1):
#     flag = 0
#     k = 1
#     for y in range(n+1,x-1,-1):
#         if flag == 0:
#             print("{:2d}".format(i),end = ' ')
#             flag = 1
#         else:
#             j = x - k
#             m = m - j
#             k -= 1
#             print("{:2d}".format(m), end=' ')
#     i = x - 1 + i
#     m = i
#     print()







### 49 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

'''
 2 
 4  6 
 8 10 12 
14 16 18 20 
22 24 26 28 30 
'''

# n = 5
# d = 1
# e = n
#
# for x in range(n,0,-1):
#     t1 = d
#     t2 = e
#     r1 = x
#     r2 = x+1
#     for y in range(n,x-1,-1):
#         if (x+y)%2 == 0:
#             print("{:2d}".format(t1),end = " ")
#         else:
#             print("{:2d}".format(t2),end = " ")
#         t1 = t1 - r1
#         t2 = t2 - r2
#
#         r1 = r1 + 1
#         r2 = r2 + 1
#
#     e = e + x - 1
#     d = d + x
#     print()






### 50 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 49

'''
---------*---------
--------*-*--------
-------*-*-*-------
------*-*-*-*------
-----*-*-*-*-*-----
----*-*-*-*-*-*----
---*-*-*-*-*-*-*---
--*-*-*-*-*-*-*-*--
---*-*-*-*-*-*-*---
----*-*-*-*-*-*----
-----*-*-*-*-*-----
------*-*-*-*------
-------*-*-*-------
--------*-*--------
---------*---------
'''

# num = 10
# for i in range(1,num+1):
#     for j in range(num,i-2,-1):
#         print("",end = "-")
#     for j in range(1,i+1):
#         print("*",end = "-")
#     for j in range(i,num+1):
#         print("",end = "-")
#     print()
#
#
# num = num - 1
# for i in range(1,num+1):
#     for j in range(1,i+3):
#         print("",end = "-")
#     for j in range(i,num+1):
#         print("*",end = "-")
#     for j in range(1,i+2):
#         print("",end = "-")
#     print()







### 51 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 49

'''
           *           
          * *          
         * * *         
        * * * *        
       * * * * *       
      * * * * * *      
     * * * * * * *     
    * * * * * * * *    
   * * * * * * * * *   
  * * * * * * * * * *  
   * * * * * * * * *   
    * * * * * * * *    
     * * * * * * *     
      * * * * * *      
       * * * * *       
        * * * *        
         * * *         
          * *          
           *   
'''

# num = 10
# for i in range(1,num+1):
#     for j in range(num,i-2,-1):
#         print("",end = " ")
#     for j in range(1,i+1):
#         print("*",end = " ")
#     for j in range(i,num+1):
#         print("",end = " ")
#     print()
#
#
# num = num - 1
# for i in range(1,num+1):
#     for j in range(1,i+3):
#         print("",end = " ")
#     for j in range(i,num+1):
#         print("*",end = " ")
#     for j in range(1,i+2):
#         print("",end = " ")
#     print()







### 52 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 49

'''
           *           
          * *          
         * * *         
        * * * *        
       * * * * *       
      * * * * * *      
     * * * * * * *     
    * * * * * * * *    
   * * * * * * * * *   
  * * * * * * * * * *  
'''

# num = 10
# for i in range(1,num+1):
#     for j in range(num,i-2,-1):
#         print("",end = " ")
#     for j in range(1,i+1):
#         print("*",end = " ")
#     for j in range(i,num+1):
#         print("",end = " ")
#     print()







### 53 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 49
'''
   * * * * * * * * * *   
    * * * * * * * * *    
     * * * * * * * *     
      * * * * * * *      
       * * * * * *       
        * * * * *        
         * * * *         
          * * *          
           * *           
            *  
'''

# num = 10
# for i in range(1,num+1):
#     for j in range(1,i+3):
#         print("",end = " ")
#     for j in range(i,num+1):
#         print("*",end = " ")
#     for j in range(1,i+2):
#         print("",end = " ")
#     print()
### 53 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 49

'''
    * * * * * * * * * * * * * * * * * * * 
      * * * * * * * * * * * * * * * * * 
        * * * * * * * * * * * * * * * 
          * * * * * * * * * * * * * 
            * * * * * * * * * * * 
              * * * * * * * * * 
                * * * * * * * 
                  * * * * * 
                    * * * 
                      * 
'''

# n = int(input("Enter : "))
# i = 1
# j = 1
# k = 1
# while i < n:
#     j = 0
#     while j < k+1:
#         print(" ",end = " ")
#         j+=1
#     j = i
#     k += 1
#     while j < n:
#         print("*",end = " ")
#         j += 1
#     print()
#     i += 2








### 53 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 49

'''
    * 
  * * * 
* * * * * 
'''
# i = 1
# n = 5
# while i <= n:
#     print(" " * (n-i) + "* "*i)
#     i += 2







### 54 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 49

'''
------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------
'''



# import string
# l = string.ascii_lowercase
# size = int(input())
# temp = 0
# num = (size * 2 - 1)
# num1 = num
# n = size
# for i in range(1,num+1,2):
#     temp += 1
#     m = size
#     n -= 1
#     s = n
#     for j in range(num,i,-1):
#         print("",end = "-")
#
#     for j in range(1,i+1):
#         if m > n:
#             m-=1
#             print(f"{l[m]}",end = "")
#         else:
#             s += 1
#             print(f"{l[s]}",end = "")
#         if temp != size or j != num:
#             print(end = "-")
#
#
#     for j in range(i,num-1):
#         print("",end = "-")
#     print()
#
#
# num = num - 2
# n1 = 1
# m1 = size
# for i in range(1,num+1,2):
#
#     s1 = n1
#     flag = 0
#     for j in range(1,i+2):
#         print("",end = "-")
#     for j in range(i,num+1):
#         if m1 > n1 and flag == 0:
#             m1-=1
#             # print(m1,n1)
#             print(f"{l[m1]}",end = "-")
#         else:
#             s1 += 1
#             # print(s1)
#             flag = 1
#             print(f"{l[s1]}", end="-")
#     n1 += 1
#     m1 = size
#     for j in range(1,i+1):
#         print("",end = "-")
#     print()






### 55 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 49
'''

'''

n = 5

for i in range(1,6):

    for j in range(1,i + 1):
        print("{:2d}".format(j),end = " ")






### 53 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 49
'''

'''
### 53 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 49


### 49 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
'''
# print("----------------------- 16 Coin Puzzle -----------------------")
# print("---------------------  Coins -> 1 2 3 4 -----------------------")
# import random
# l = [1,2,3,4]
# player1 = int(input("Player1 Enter the coin : "))
# coin = player1
# # print(f"Total Coins = {coin}")
# if 6 - player1 > 4:
#     computer = random.choice(l)
#     print(f"Computer Entered = {computer}")
#     coin += computer
#     print(f"Total Coins = {coin}")
#     player1 = int(input("Player1 Enter the coin : "))
#     coin += player1
#     if coin < 6:
#         computer = 6 - coin
#         coin += computer
#         print(f"Computer Entered = {computer}")
#         print(f"Total Coins = {coin}")
#         player1 = int(input("Player1 Enter the coin : "))
#         coin += player1
#         print(f"Total Coins = {coin}")
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
#     elif coin == 6:
#         computer = random.choice(l)
#         print(f"Computer Entered = {computer}")
#         coin += computer
#         print(f"Total Coins = {coin}")
#         player1 = int(input("Player1 Enter the coin : "))
#         coin += player1
#         if coin < 11:
#             computer = 11 - coin
#             print(f"Computer Entered = {computer}")
#             coin += computer
#             print(f"Total Coins = {coin}")
#             player1 = int(input("Player1 Enter the coin : "))
#
#             coin += player1
#             # print(f"Total Coins = {coin}")
#             computer = 16 - coin
#             print(f"Computer Entered = {computer}")
#             coin += computer
#             print(f"Total Coins = {coin}")
#             print("Computer win the game")
#         elif coin == 11:
#             computer = random.choice(l)
#             print(f"Computer Entered = {computer}")
#             coin += computer
#             print(f"Total coin = {coin}")
#             player1 = int(input("Player1 Enter the coin : "))
#             coin += player1
#             if coin == 16:
#                 print(f"Total Coins = {coin}")
#                 print(f"Player1 won the game ")
#             elif coin < 16:
#                 computer = 16 - coin
#                 print(f"Computer Entered = {computer}")
#                 coin += computer
#                 print(f"Total Coins = {coin}")
#                 print("Computer won the game ")
#
#         elif coin > 11:
#             computer = 16 - coin
#             print(f"Computer Entered = {computer}")
#             coin += computer
#             print(f"Total Coins = {coin}")
#             print("Computer won the game ")
#     elif coin > 6:
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
#
#
#
# else:
#     computer = 6 - player1
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






# By second method
# print("----------------------- 16 Coin Puzzle -----------------------")
# print("---------------------  Coins -> 1 2 3 4 -----------------------")
# import  random
#
# l1 = [1,2,3,4]
# sum_coin = 16
# n = len(l1)+1
# l2 = []
# count = 0
# flag = 0
# while count!=16:
#     flag = 0
#     l2 = []
#     player1 = int(input("player1 Enter Coin : "))
#     if player1 > 4:
#         raise Exception("Abe Sale Coins 1 2 3 4 Mai Chunna Hai To 4 Se Jyada Kiya Tera Bap Lakr Dega")
#     count+=player1
#     if count == 16:
#         print("Player1 won the game ")
#         break
#     for i in l1:
#         check = sum_coin - (count + i)
#         if  check % 5 == 0:
#             flag = 1
#             l2.append(i)
#             break
#     else:
#         l2.append(random.choice(l1))
#     computer = min(l2)
#     print(f"computer Entered : = {computer}")
#     count+=computer
#
# if flag == 1:
#     print("Computer won the game ")
'''


from itertools import permutations

str , n = input().split()
for i in permutations(str,int(n)):
    s = "".join(i)
    print("{:2s}".format(i))


















