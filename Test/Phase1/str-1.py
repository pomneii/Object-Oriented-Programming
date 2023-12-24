
name = "Woranuch Pluengnuch"  # index ==> start 0

# index
print(name[0])
print(name[3])
print(name[7])

# start and end index
print(name[2:5]) # index 2 - 4 before :5 index
print(name[:8]) # start from 0 end index 7
print(name[:19])

# negative index
print(name[-1]) # last index
print(name[::-1])

# length of string
print(len(name))

# ' ' = 1 index

# delete space left and right
a = " Pink "
print(len(a))
a = a.strip() # delete space left and right
print(len(a))

# delete left space
b = " Pink"
print(len(b))
b = b.lstrip() # delete left space 
print(len(b))

# delete right space
c = "Pink "
print(len(c))
c = c.rstrip() # delete right space
print(len(c))

# upper()
a = "pink"
print(a.upper())

# lower()
print(a.lower())

# first letter is upper : capitalize()
print(a.capitalize())

# replace ("old string", "new string")
print(a.replace("pink", "kikikuku"))
print(a.replace("i", "ko"))

# replace by count ("old str", "new str", count)
b = "pink grade 4 in M.4"
print(b.replace("4", "fail", 2))

# check string
name = "kiki is kuku"
x = "kiki" in name
y = "bob" in name
print(x)
print(y)

if x :
    name = name.replace("kiki", "keke")
print(name)
