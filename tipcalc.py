print("Welcome to the Tip Calculator")
bill= input("What was the total bill? ")
tip_percent= input("What percentage tip would you like to give? 10, 12 or 15? ")
group= input("How many people to split the bill? ")
total_bill= float(bill)*(1+ (float(tip_percent)/100))
share= round(total_bill/int(group), 2)
print(f"Each person should pay: {share} ")