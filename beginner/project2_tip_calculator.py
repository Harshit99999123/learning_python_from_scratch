print("Welcome to the tip calculator! \n")
total_bill_input = input("What is the total bill? ")
tip_input = input("How much tip would you like to give? ")
person_to_split_input = input("How many people to split the bill? ")
total_bill = float(total_bill_input)
tip = float(tip_input)
person_to_split = int(person_to_split_input)
tip_amount = (total_bill * tip) / 100
final_amount = total_bill + tip_amount
each_person_should_pay = final_amount / person_to_split
rounded_final_bill_amount = round(each_person_should_pay, 2)
print(f"Each person should pay {rounded_final_bill_amount}")
