def toFixed(value, digits):
    return "%.*f" % (digits, value)

def determinegross(hours, payrate):
    if hours > 40:
        overtimehours = hours - 40
        overtimepay = overtimehours * payrate * 0.5
        grosspay = overtimepay + hours * payrate
    else:
        grosspay = hours * payrate
    
    return grosspay

def determinepay(jcode):
    if jcode == "L":
        payrate = 25
    else:
        if jcode == "A":
            payrate = 30
        else:
            if jcode == "J":
                payrate = 50
            else:
                print("enter correct job code")
    
    return jcode

# Main
print("what is your last name?")
lname = input()
print("what is your job code? ('A','L', or 'J')")
jcode = input()
print("how many hours did you work?")
hours = int(input())
determinepay(jcode)
payrate = determinepay(jcode)
determinegross(hours, payrate)
grosspay = determinegross(hours, payrate)
print("your name is " + lname + " and your gross pay is $ " + toFixed(grosspay,2))
