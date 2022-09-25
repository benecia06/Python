height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")


#Write your code below this line 👇
new_wt= float(weight)
new_ht= float(height)
BMI= (new_wt/(new_ht**2))
print(int(BMI))