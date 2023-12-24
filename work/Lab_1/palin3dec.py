
"""
    ตัวเลข palindrome คือตัวเลขที่อ่านได้ทั้ง 2 ทาง แล้วมีค่าเท่ากัน เช่น 9009 โดย 9009 คือ palindrome
    ที่เกิดจากการคูณของตัวเลข 2 หลักที่มากที่สุด คือ 91x99 จงหา palindrome ที่มากที่สุดของตัวเลข 3 หลัก
"""

# str = input("Enter string : ")
# if(str == str[::-1]) :
#     print("Palindrome")
# else :
#     print("Not Palindrome")

m = 999
n = 999
palin = []

while m >= 0 :
    while n >= 0 :
        result = m * n
        result_str = str(result)

        if result_str == result_str[::-1]: # make it to string to use function
            # palin.append(result) use when you need to add the list, always add one item
            palin = palin + [result]

        n = n - 1

    m = m - 1
    n = 999

palin = max(palin)
print(palin)
