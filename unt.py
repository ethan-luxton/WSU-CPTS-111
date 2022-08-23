


    
pace = str(input("Enter pace [mm:ss]: "))
distance = float(input("Enter distance [miles]: "))
mm, ss = int(pace.split(":")[0]), int(pace.split(":")[1])

def calculate_time():
    print(pace)
    print(mm)
    print(ss)
    global new_sec
    global full_sec
    global total_time_sec
    global seconds_per_mile
    global hours
    global minutes
    global seconds
    new_sec = mm * 60
    full_sec = ss + new_sec
    total_time_sec = full_sec * distance
    seconds_per_mile = total_time_sec / 60
    hours = int(seconds_per_mile // 60)
    minutes = int((total_time_sec - (hours * 3600))//60)
    seconds = int(total_time_sec - ((hours * 3600) + (minutes * 60)))
    return(seconds, minutes, hours)
calculate_time()

def display_time():
    if seconds < 10:
        print(hours,":",minutes,":0",seconds, sep="")
    else:
        print(hours,":",minutes,":",seconds, sep="")
    return
display_time()
# def main():
#     pace, distance, mm, ss = get_input()
#     hours, minutes, seconds = calculate_time(pace, distance, mm, ss)
#     display_time(pace, distance, mm, ss, seconds, minutes, hours)

# main()
