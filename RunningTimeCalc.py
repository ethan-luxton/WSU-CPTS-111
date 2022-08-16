# Ethan Luxton
# CptS 111, Fall 2017
# Programming Assignment #3
# 9/22/17
# Running time Calculator
# This program calculates the time it takes for a person to run a set amount of miles

def get_input():
    global pace_str
    pace_str = str(input("Enter your pace: "))
    mm, ss = int(pace_str.split(':')[0]), int(pace_str.split(':')[1])
    global dist
    dist = float(input("Enter the distance you're going to run: "))
    global sec_per_mile
    sec_per_mile = (mm * 60) + ss
    return

def calc_time():
    global total_time
    total_time = sec_per_mile * dist
    return

def display_time():
    s2, test = divmod(total_time, 3600)
    s3, remainder = divmod(test, 60)
    hours = int(s2)
    minutes = int(s3)
    seconds = int(remainder)
    if remainder < 10:
        print("The time needed to run", dist, "miles at a(n)",pace_str,"pace: " ,hours,":",minutes,":0",seconds, sep="")
    else:
        print("The time needed to run",dist,"miles at a(n)",pace_str,"pace: ",hours,":",minutes,":",seconds, sep="")
    return

def main():
    get_input()
    calc_time()
    display_time()
    return

main()
