height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")


#Write your code below this line 👇
new_wt= float(weight)
new_ht= float(height)
BMI= (new_wt/(new_ht**2))

if BMI<18.5: print(f"Your BMI is {round(BMI)}, you are underweight.")
elif BMI>18.5 and BMI<25: print(f"Your BMI is {round(BMI)}, you have a normal weight.")
elif BMI>25 and BMI<30: print(f"Your BMI is {round(BMI)}, you are slightly overweight.")
elif BMI>30 and BMI<35: print(f"Your BMI is {round(BMI)}, you are obese.")
elif BMI>35: print(f"Your BMI is {round(BMI)}, you are clinically obese.")

