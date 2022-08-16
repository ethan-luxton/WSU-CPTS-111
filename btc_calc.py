#Ethan Luxton
#BTC Value Calculator
#Programmed on 9/18/17



btc_value = float(input('Enter a Bitcoins current value: '))
btc_inf_rate = float(input('Enter Bitcoins current inflation rate per year: ')) / 10
btc_amount = float(input('Enter the amount you have in Bitcoin from .01 to 99.9: '))
years = int(input('Enter the number of years until next Halving: '))
   

calc1 = (btc_value * btc_amount)
calc2 = (calc1 * btc_inf_rate) * years
    
def btc_display():
    calc2_r = round(calc2, 2)
    print(calc2_r,'Dollars is what you will have by the end of',years,'years.')
    return
    
    
btc_display()
