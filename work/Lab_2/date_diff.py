
"""
    จากโปรแกรมในข้อ 7 ให้เขียนฟังก์ชัน เพิ่มเติมเป็น date_diff
    - รับข้อมูลในรูปแบบ “dd-mm-yyyy” เช่น
        date_diff(“1-1-2018”, “1-1-2020”) จะได้ 731 วัน
        date_diff(“25-12-1999”, “9-3-2000”) จะได้ 76 วัน
    - ให้เขียนฟังก์ชัน day_in_year โดยจะส่งค่าจํานวนวันของปี (365 หรือ 366) โดยรับข้อมูลเป็น ปี
    - ส่งคืนข้อมูลเป็นจํานวนวันตั้งแต่วันที่แรก จนถึงวันที่สอง โดยรวมทั้ง 2 วันนั้นเข้าไปด้วย
    - ให้สมมติว่าวันแรก จะต้องมาก่อนวันที่สองเสมอ ดังนั้นไม่ต้องตรวจสอบ
"""

def is_leap(year) :
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) :
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


def day_in_year(year) :
    return is_leap(year)


def date_diff(data_first, data_second) :
    data_first = [int(e) for e in data_first.split('-')]
    data_second = [int(e) for e in data_second.split('-')]
    day_first, month_first, year_first = [data_first[i] for i in range(3)]
    day_second, month_second, year_second = [data_second[i] for i in range(3)]

    total_first = day_in_year(year_first)

    first = day_of_year(day_first, month_first, year_first)
    second = day_of_year(day_second, month_second, year_second)

    if year_first == year_second :
        result = second - first + 1
        return result
    else :
        differ = 0
        for i in range(year_first + 1, year_second) :
            differ += day_in_year(i)
        return (total_first - first) + second + differ + 1
    

data_first = [int(e) for e in input().split('-')]
data_second = [int(e) for e in input().split('-')]
print(date_diff(data_first, data_second))
