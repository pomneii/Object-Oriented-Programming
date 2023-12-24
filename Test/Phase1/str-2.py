
# merge string
fname = "Woranuch"
lname = "Pluengnuch"
age = "80"

fullname = fname + ' ' + lname + ' ' + age
print(fullname)

# arrange string
text = "Firstname : {1}\tLastname : {1}\tAge : {2}"
print(text.format(fname, lname, age))
#                   0      1     2

# count words in string
fruits = "apple apple apple papaya papaya papaya banana banana banana orange orange orange apple papaya banana orange banana orange"
print(fruits.count("banana"))
print(fruits.count("grape"))

# check start word
name = "Miss Woranuch"
print(name.startswith("Miss"))

if name.startswith("Mr.") :
    print("Male")
else :
    print("Female")

# check end word
num = "2354"

if num.endswith("0") :
    print("Lucky!")
else :
    print("Not lucky T-T")