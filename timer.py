import time
milli = 0
seconds = 0
minutes = 0
hours = 0
while hours < 1000:
    print("Hours:", hours,"Minutes:", minutes,"Seconds:", seconds,"Milliseconds:", milli)
    time.sleep(0.001)
    milli += 1
    if milli == 1000:
        milli = 0
        seconds += 1
        if seconds == 60:
            seconds = 0
            minutes += 1
            if minutes == 60:
                minutes = 0
                hours += 1