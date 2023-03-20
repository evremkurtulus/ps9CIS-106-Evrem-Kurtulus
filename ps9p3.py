def compmpg(miles, gallons):
    mpg = float(gallons) / miles
    
    return mpg

def gascost(gallons):
    gascost = gallons * 2.5
    
    return gascost

# Main
print("what city did you travel to?")
city = input()
print("how many miles approx traveled?")
miles = int(input())
print("how many gallons of fuel approx used?")
gallons = int(input())
compmpg(miles, gallons)
mpg = compmpg(miles, gallons)
gascost(gallons)
gascost = gascost(gallons)
print("when traveling to " + city + " you will travel " + str(miles) + "miles and the gas will cost $" + str(gascost) + ". your miles per gallon are " + str(mpg))
