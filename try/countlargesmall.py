
def check_str(str) :
    result = {"Upper" : 0, "Lower" : 0}
    for i in str :
        if i.isupper() :
            result["Upper"] += 1
        elif i.islower() :
            result["Lower"] += 1
        else :
            pass
    return result

m = check_str("AfalfFKALFJamaf")
print(m)