
"""

    ให้รับเวลาเข้าและออกของรถให้รับเวลาเข้าและออกของรถคันหนึ่ง (เปิดบริการตั้งแต่ 7:00 - 23:00) จากนั้น
    คํานวณค่าที่จอดรถที่ต้องจ่าย โดยหลักเกณฑ์การคํานวณมีดังนี้
        1) จอดรถไม่เกิน 15 นาทีไม่คิดค่าบริการ
        2) จอดรถเกิน 15 นาทีแต่ไม่เกิน 4 ชั่วโมง คิดค่าบริการชั่วโมงละ 10 บาท เศษของชั่วโมงคิดเป็น
        หนึ่งชั่วโมง
        3) จอดรถตั้งแต่ 4 ชั่วโมง ถึง 6 ชั่วโมง คิดค่าบริการชั่วโมงที่ 4-6 ชั่วโมงละ 20 บาท เศษของ
        ชั่วโมงคิดเป็นหนึ่งชั่วโมง
        4) จอดรถเกิน 6 ชั่วโมงขึ้นไป เหมาจ่ายวันละ 200 บาท
    ข้อมูลนําเข้า
        มี 1 บรรทัด แต่ละบรรทัดมีจํานวนเต็ม 4 จํานวนคั่นด้วย Space
        โดยบรรทัดที่ 1-2 เป็นชั่วโมงและนาทีของเวลาเข้า และบรรทัดที่ 3-4 เป็นชั่วโมงและนาทีของเวลาออก
    ข้อมูลส่งออก
        มีบรรทัดเดียว เป็นค่าที่จอดรถที่ต้องจ่าย ให้แสดงผลลัพธ์เป็นจํานวนเต็ม

    Input             Output

    7 0 7 15            0
    7 0 7 16            10
    7 30 10 30          30
    7 30 10 31          50
    7 30 13 31          200

"""


hour_in, minute_in, hour_out, minute_out = [int(e) for e in input().split()]

if (((hour_in == hour_out) and minute_in > minute_out) or (hour_in > hour_out)) or (hour_out == 23 and minute_out > 0) or (hour_in < 7) or minute_in > 59 or minute_out > 59 :
    print("Error")
else :
    if (hour_in == hour_out) and (minute_out - minute_in) <= 15 :
        print(0)
    elif (hour_in == hour_out) and (minute_out - minute_in) > 15 :
        print(10)
    elif (hour_out - hour_in) == 1 :
        if (60 - minute_in) + minute_out <= 15 :
            print(0)
        else :
            print(10)
    elif (hour_out - hour_in) < 4 :
        if minute_in >= minute_out :
            print((hour_out - hour_in) * 10)
        else :
            print(((hour_out - hour_in) * 10) + 20)
    elif 4 <= (hour_out - hour_in) <= 6 :
        if minute_in >= minute_out :
            print((hour_out - hour_in - 3) * 20 + 30)
        else :
            if (hour_out - hour_in - 2) > 3 :
                print(200)
            else :
                print((((hour_out - hour_in) - 2) * 20) + 30)
    elif (hour_out - hour_in) > 6 :
        print(200)
    
    