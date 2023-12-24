
""""
    จงเขียนโปรแกรมที่คํานวณค่าของ a+aa+aaa+aaaa เมื่อรับข้อมูลเป็นตัวเลข 1 หลัก
    nput : 9
    Output : 11106 (=9+99+999+9999)
"""

num = input()

if num.isnumeric() and 0 <= int(num) <= 9 :
    num = int(num)
    print((num + num + (num * 10) + (num * 100) + (num * 10) + num + (num * 1000) + (num * 100) + (num * 10) + num))
else :
    print("Error") 