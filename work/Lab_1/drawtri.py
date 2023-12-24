
"""
    จงเขียนโปรแกรมแสดงรูปสามเหลื่ยม (ตามโปรแกรมใน Slide 5) แต่ปรับปรุงให้ใช้ Loop เพียง Loop เดียว
"""

# n = 10
# for row in range(n) :
#     for col in range(n) :
#         if row + col < n :
#             print(' ', end="")
#         else :
#             print("#", end=' ')
#     print("#")

n = 10
for row in range(n):
    print(' ' * (n - row), end='')
    print("#" * (row + 1))
