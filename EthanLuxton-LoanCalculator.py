# Programmer: Ethan Luxton
# Cpt-S 111 - Lab 04
# Lab #2 - Task #5
# Sept. 7th, 2017

p = int(input('Enter the amount you owe: ')) #loan amount
i = float(input('Enter your interest rate: ')) / 100 #interest rate
n = int(input('Enter the number of years you plan to pay off your loan: ')) * 12

monthly_payment = p * (i / 12) / (1 - (1 + i /12) ** - n) #calculates monthly payments

total_amount = (monthly_payment * n) #Calculates total amount owed including interest

total_interest = (total_amount - p)

final_payment = round(monthly_payment, 2)
final_amount = round(total_amount, 2)
final_interest = round(total_interest, 2)

print('Your monthly payment is $',final_payment)
print('The total amount you end up paying is $',final_amount)
print('The total amount of interest you paid is $',final_interest)
