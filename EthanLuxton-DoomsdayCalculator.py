# Programmer: Ethan Luxton
# Cpt-S 111 - Lab 04
# Lab #2 - Task #6
# Sept. 7th, 2017

dmsd_year = int(input('Enter the last two digits of the year: ')) #Ex: 05 or 17
dmsd_anchor = int(input('Enter the anchor day as an integer: ')) #Ex: 1 or 2

doomsday = (((dmsd_year // 12) + (dmsd_year % 12) + (dmsd_year % 12) // 4) % 7 + dmsd_anchor) % 7

print('Doomsday =', doomsday)
