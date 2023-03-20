def toFixed(value, digits):
    return "%.*f" % (digits, value)

def comptuition(dcode, credits):
    if dcode == "I":
        tuition = credits * 250
    else:
        if dcode == "O":
            tuition = credits * 550
        else:
            print("enter either 'I' or 'O' for district code.")
    
    return tuition

# Main
print("what's the students last name?")
lname = input()
print("how many credits is " + lname + " taking?")
credits = int(input())
print("is the student in district or out of district? ('I' or 'O')?")
dcode = input()
comptuition(dcode, credits)
tuition = comptuition(dcode, credits)
print("the student " + lname + "owes & " + toFixed(tuition,2) + " in tuition.")
