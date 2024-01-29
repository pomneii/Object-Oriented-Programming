# phase = "Hello World!"
# print(phase.upper()) # upper characters
# print(phase.isupper()) # true / false that phase is upper characters
# print(phase.upper().isupper()) # true / false that phase is upper characters
#                                # it works in upper() and then check in isupper()
# print(len(phase)) # tell the length of phase
# print(phase[0]) # print the first index
# print(phase.index("o")) # tell the index of character
# print(phase.replace("Hello", "kiki")) # replace first with second

# print(2) # print number
# print(8 - 7 * 2)

# number = 5
# print(number)
# print(str(number) + " is number") # can change number to string

# numboo = -5
# print(abs(numboo)) # print absolute of numboo
# print(pow(3, 2)) # 3 ^ 2

# print(max(4, 6)) # print the max
# print(min(4, 6)) # print the min

# print(round(3.4)) # round down
# print(round(3.6)) # round up

# from math import *
# print(floor(3.7))
# print(ceil(3.7))
# print(sqrt(36))

# name = input("Enter your name : ")
# age = input("Enter your age : ")
# print("Hello " + name + "! You are " + age)

# friends = ["kiki", "kuku", "kaka", "koko", "keke"]
# lucky_numbers = [4, 6, 75, 24, 55, 19]
# # print(friends[2])
# # print(friends[1:3])
# friends.extend(lucky_numbers)
# print(friends)

# list = []
# while True :
#     weight = int(input())
#     if weight != 0 :
#         list = list + [weight]
#     else :
#         break

# pro = input() 
# if pro == "min" or pro == "Min" or pro == "miN" or pro == "mIn" or pro == "mIN" or pro == "MIn" or pro == "MIN":
#     list = sorted(list)
#     for i in list :
#         print(i, end=' ')
# elif pro == "Max" or pro == "max" or pro == "MaX" :
#     list = sorted(list)
#     list = list[::-1]
#     for j in list :
#         print(j)
# else :
#     print("Error!")

# num = int(input())
# i = 1
# list = []
# a = int(input())
# find_num = int(input())
# if find_num in a :
#   print("Yes")
# else :
#   print("No")

# lis = [i for i in 'Hello']
# for i in 'Hello' :
#     lis.append(i)

# print(lis)

# lis = [x for x in range(20) if x % 2 == 0]
# print(lis)

# var = 100
# def bobo(kiki) :
#     return kiki + 1

# print(bobo(var))

# str = input()
# print(str)
# print(str.capitalize())
# print(str.title())

# num = int(input())
# str = input().split(' ')
# lis = []
# for i in range(len(str)) :
#     lis.append('e' * len(str[i]))

# result = ' '.join([e for e in lis])
# print(result)

# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         s = s.split()
#         return len(s[len(s) - 1])

# x = input()
# y = Solution()
# print(y.lengthOfLastWord(x))