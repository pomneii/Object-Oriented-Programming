
# BMI 

# BMI = weight(kg) / height(m) * height(m)

# input and convert to int
weight = int(input("Enter your weight(kg) : "))
height = int(input("Enter your height(cm) : ")) / 100

# output
bmi = weight / (height ** 2)
print("BMI :", bmi)

if 0 <= bmi < 18.5 :
    print("Lower")
elif 18.5 <= bmi <= 22.9 :
    print("Great!")
elif 23.0 <= bmi <= 24.9 :
    print("Over")
elif 25.0 <= bmi <= 29.9 :
    print("Fat")
else :
    print("Obese") 