
# break / continue

i = 1
while i <= 10 :
    print("Round :", i)
    if i == 5 :
        break
    i += 1
print("End of program!") 

i = 1
while i <= 10 :
    i += 1       # if you check before add it will do infinity loop
    if i % 2 != 0 :
        continue
    print("Round :", i)
print("End of program!") 

for i in range(1,11) :
    if i % 2 == 0 :
        continue
    print(i)

for i in range(1,11) :
    print(i)
    if i == 5 :
        break
