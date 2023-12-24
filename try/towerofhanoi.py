
# Tower of Hanoi

"""
    n = number of dish
    pole ==> A, B, C
    n = 1
    n = 2 (n - 1)
    n = 3 (the biggest)

    A ==> 3
    C ==> 3 2 1
    B = จุดพักจาน

    A ==> S M L
    A ==> S M ==> B
    C ==> L
    B ==> S M 
    A ==> S
    C ==> L M
    A ==> C
    C ==> L M S

    C ==> S M L
"""

def hanoi(num, a, b, c) : # จำนวนจาน จุดย้าย จุดพัก จุดไป
    # a ==> c
    if num == 0 :
        return
    hanoi(num - 1, a, c, b) # ย้าย a  S M ==> b | ย้าย a ==> พัก c ==> ไป b
    print("จานที่ :", num, "จาก", a, "ไป", c)
    hanoi(num - 1, b, a, c)

hanoi(3, "A", "B", "C")



