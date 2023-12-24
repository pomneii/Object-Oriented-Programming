
# change temperature 
temp = input("Enter temperature(celcious / Fahrenheit) : ")

degrees = int(temp[:-1])

unit = temp[-1]

print(degrees, " = ", unit)

if unit == "C" :
    result = ((degrees * 9) / 5) + 32
if unit == "F" :
    result = ((degrees - 32) * 5) / 9

print(result)