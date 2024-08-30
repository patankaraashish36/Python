def timeConversion(s):
    # Write your code here
    if s[:2] == "12" and s[-2:] == "AM":
        s = "00" + s[2:-2]
        return s
    elif s[:2] == "12" and s[-2:] == "PM":
        s = s[:-2]
        return s
    else:
        if int(s[:2]) < 12 and s[-2:] == "PM":
            h = int(s[:2]) + 12
            s = str(h) + s[2:-2]
            return s
        else:
            s = s[:-2]
            return s

print(timeConversion("07:05:45AM"))
    