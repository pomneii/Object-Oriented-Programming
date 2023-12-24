
"""
    ให้เขียน function ชื่อ day_of_year(day, month ,year)
    โดยมีการคืนค่า คือ day_of_years เป็นวันที่ลําดับที่เท่าใดของปีคริสตศักราช year
    - ปีที่เป็น Leap Year เดือนกุมภาพันธ์จะมี 29 วัน
    - ให้สร้างฟังก์ชัน is_leap เพื่อตรวจสอบ leap year แยกออกมา และให้ฟังก์ชัน day_of_year
    เรียกใช้ is_leap อีกที
"""

def is_leap(year) :
    if year % 4 == 0 :
        if year % 100 == 0 :
            if year % 400 == 0 :
                return 366
            else :
                return 365
        else :
            return 366
    else :
        return 365

def day_of_year(day, month, year) :

    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap(year) == 366 :
        days_in_month[1] = 29

    for i in range(month - 1) :
        day = day + days_in_month[i]
    day_of_years = day
    return day_of_years

day = int(input())
month = int(input())
year = int(input())
x = day_of_year(day, month, year)
print(x)


