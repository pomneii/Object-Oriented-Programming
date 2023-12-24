
hour_in, minute_in, hour_out, minute_out = [int(e) for e in input().split()]

if (((hour_in == hour_out) and minute_in > minute_out) or (hour_in > hour_out)) or (hour_out == 23 and minute_out > 0) or (hour_in < 7) or minute_in > 59 or minute_out > 59 :
    print("Error")
else :
    if (hour_in == hour_out) and (minute_out - minute_in) <= 15 :
        print(0)
    elif (hour_in == hour_out) and (minute_out - minute_in) > 15 :
        print(10)
    elif (hour_out - hour_in) == 1 :
        if (60 - minute_in) + minute_out <= 15 :
            print(0)
        else :
            print(10)
    elif (hour_out - hour_in) < 4 :
        if minute_in >= minute_out :
            print((hour_out - hour_in) * 10)
        else :
            print(((hour_out - hour_in) * 10) + 20)
    elif 4 <= (hour_out - hour_in) <= 6 :
        if minute_in >= minute_out :
            print((hour_out - hour_in-3) * 20+30)
        else :
            if (hour_out - hour_in ) -2 > 3 :
                print(200)
            else :
                print((((hour_out - hour_in) -2) * 20)+30)
    elif (hour_out - hour_in) > 6 :
        print(200)
    
    