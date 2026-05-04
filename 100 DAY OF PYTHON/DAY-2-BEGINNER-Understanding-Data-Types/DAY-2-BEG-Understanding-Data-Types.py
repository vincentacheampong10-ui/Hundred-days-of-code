print("Welcome to the tip calculator")

bill = float(input("What was the total bill? $:"))

tip = int(input("What percentage tip would you like to give?:"))
people = int(input("How many people are splitting the bill?:"))

bill_with_tip = tip / 100 * bill + bill
final_amount= round(bill_with_tip / people, 2)

print(f"The final amount is ${final_amount}")


