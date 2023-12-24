
# nested loop

i = 1

while i <= 3 :
    j = 1
    while j <= 5 :
        print("รอบที่ :", i, "ตำแหน่งที่ :", j)
        j += 1
    i += 1
print("End of program!")


for i in range(3) :
    j = 1
    for j in range(5) :
        print("รอบที่ :", i + 1, "ตำแหน่งที่ :", j + 1)

