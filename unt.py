def get_input(pace, distance, mm, ss):
    global pace
    pace = str(input("Enter pace [mm:ss]: "))
    distance = float(input("Enter distance [miles]: "))
    mm, ss = int(pace.split(":")[0]), int(pace.split(":")[1])
    return(pace, distance, mm, ss)
def calculate_time():
    print(pace)
    print(mm)
    print(ss)
    new_sec = mm * 60
    full_sec = ss + new_sec
    print(full_sec)
    print(distance)
    total_time_sec = full_sec * distance
    print(total_time_sec)
    seconds_per_mile = total_time_sec / 60
    hours = int(seconds_per_mile // 60)
    print(seconds_per_mile)
    print(hours)
    minutes = int((total_time_sec - (hours * 3600))//60)
    print(minutes)
    seconds = int(total_time_sec - ((hours * 3600) + (minutes * 60)))
    print(seconds)
    print(pace, full_sec, distance)
    return
calculate_time()

def display_time(pace, distance, mm, ss, seconds, minutes, hours):
    if seconds < 10:
        print(hours,":",minutes,":0",seconds, sep="")
    else:
        print(hours,":",minutes,":",seconds, sep="")
    return()
display_time(pace, distance, mm, ss, seconds, minutes, hours)
def main():
    pace, distance, mm, ss = get_input()
    hours, minutes, seconds = calculate_time(pace, distance, mm, ss)
    display_time(pace, distance, mm, ss, seconds, minutes, hours)

main()
