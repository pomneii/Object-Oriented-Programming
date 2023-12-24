
"""
    ให้ตรวจสอบว่า String ที่รับเข้ามาผ่านคีย์บอร์ด เป็นตัวอักษรพิมพ์เล็ก หรือตัวอักษรพิมพ์ใหญ่ อย่างละกี่ตัว
    ให้ตอบ 2 บรรทัด จํานวนตัวพิมพ์เล็ก 1 บรรทัด จํานวนตัวพิมพ์ใหญ่ 1 บรรทัด
"""

str = str(input("Enter the text : "))
large = 0
small = 0
for i in str :
    if(i.isupper()) :
        large += 1

    elif(i.islower()) :
        small += 1

print("Large :", large)
print("Small :", small)