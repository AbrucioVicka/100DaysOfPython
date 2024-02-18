print("Welcome to the Tip Calculator!")
total = float(input("What was the total of the bill?\n $"))
divide = int(input("How many people to split the bill?\n"))
percentage = int(input("What percentage would you like to give?\n"))
split_bill =(total+total*(percentage/100))/divide
print(f"Each person should pay: $ {split_bill:.2f}")