
"""
    จากโปรแกรมในข้อ 8 ให้เขียนฟังก์ชัน date_diff เพิ่มเติม โดยให้มีการตรวจสอบ
    - วันที่ต้องเป็นวันที่ถูกต้องของเดือนนั้นๆ
    - เดือนต้องอยู่ระหว่าง 1-12
    - เดือนกุมภาพันธ์ของปีที่มี Leap Year เท่านั้นที่จะมี 29 วันได้
    - หากข้อมูล Input ผิดพลาด ให้ Return -1
"""

def is_leap(year) :
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) :
        return 366
    else :
        return 365 

def day_of_year(day, month, year) :

    if 1 <= month <= 12 :

        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if is_leap(year) == 366 :
            days_in_month[1] = 29

        if day > days_in_month[month - 1] :
            return -1 

        for i in range(month - 1) :
            day = day + days_in_month[i]
        day_of_years = day

        return day_of_years
    else :
        return -1


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

    if first == -1 or second == -1 :
        return -1

    if year_first == year_second :
        result = second - first + 1
        return result
    else :
        differ = 0
        for i in range(year_first + 1, year_second) :
            differ += day_in_year(i)
        return (total_first - first) + second + differ + 1
    
data_first = input()
data_second = input()
result = date_diff(data_first, data_second)
print(result)
