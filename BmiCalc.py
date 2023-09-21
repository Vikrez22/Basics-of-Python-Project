height = float(input("enter your height in m:."))
weight = float(input("enter your weight in kg."))

bmi = float(weight / height ** 2)
if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you are normal weight.")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are overweight.")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are normal obese.")
else:
    print(f"Your bmi is {bmi}, you are clinically obese.")