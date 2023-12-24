
tup = (1, 2, 3, 4, "kiki", True)
list1 = [1, 2, 3, 4, "kiki", True]

print(tup)
print(list1)
print(type(tup))
print(type(list))

# constructor
tup1 = tuple(("bobo", 1, 2))
list2 = list(["bibi", 1, 2])

print(tup1)
print(list2)

tup = (1, 2, 3, 4, "kiki", True)
list = [1, 2, 3, 4, "kiki", True]

list[0] = "Bangkok"
print(list)

# tuple cannot change data
# tup[0] = "Bangkok"
# print(tup)

tup = (1, 2, 3, 4, "kiki", True)

# print
print(tup[0:4])
print(tup[4])
print(tup[1:])
print(tup[-4:])

# tuple ==> list and change data then
# list ==> tuple

lis = list(tup)
print(lis)
lis[0] = "Bangkok"
print(lis)
tup = tuple(lis)
print(tup)

tup = (1, 2, 3, 4, "kiki", True)

for item in tup :
    print(item, end=' ')

# check tuple

if "bobo" in tup :
    print("Yes")
else :
    print("No")

# length of tuple
tup = (1, 2, 3, 4, "kiki", True)

print(len(tup))

for i in range(len(tup)) :
    print(tup[i])

x = ("kiki") # i want to have one member in tuple
print(x)
print(type(x)) # it shows that x is str

y = ("kuku", )
print(type(y))

# add data
a = ("Pink", "kiki", "koko")
new1 = "booboo" # its str ; str + tuple = cannot
new2 = ("booboo",)

a = a + new2
print(a)

# delete data
tup = (1, 2, 3, 4, "kiki", True)
print(tup)
lis = list(tup)
lis.remove("kiki")
tup = tuple(lis)
print(tup)

# count()
tup = (1, 2, 3, 4, "kiki", True, 3)
x = tup.count(3)
print(x)

# index()
y = tup.index(3)
print(y)
  
# sorting
tup = (20, 41, 3, 85, 61, 1, 2, 55, 75)
lis = list(tup)
lis.sort()
lis.reverse()
tup = tuple(lis)
print(tup)

  
