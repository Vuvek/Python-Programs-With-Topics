################ 1 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2

# import re
# def is_allowed_specific_char(string):
#     charRe = re.compile(r'[^a-zA-Z0-9.]')
#     string = charRe.search(string)
#     return not bool(string)
#
# print(is_allowed_specific_char("ABCDEFabcdef123450"))
# print(is_allowed_specific_char("*&%@#!}{"))
#
#
# # write c program to identify the given identifyer is valid or not
#
# def valid_identifier_or_not(str):
#     if (ord(str[0]) >= 65 and ord(str[0]) <= 90)  or (ord(str[0]) >= 97 and ord(str[0]) <= 122) or ord(str[0]) == 95:
#         for i,j in enumerate(str):
#             print(ord(j))
#             if not ((ord(j) >= 65 and ord(j) <= 90) or (ord(j) >= 97 and ord(j) <= 122) or ord(j) == 95 or (ord(j) >= 48 and ord(j) <= 58)):
#                 return False
#             else:
#                 pass
#     else:
#         return False
#     return True
#
#
#
# s = valid_identifier_or_not(f"{input('Enter the string : ')}")
# print(s)
#
# # print(ord('a'))