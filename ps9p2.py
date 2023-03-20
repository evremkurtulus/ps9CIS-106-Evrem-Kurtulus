def compbatavg(numhit, atbats):
    batavg = atbats / numhit
    
    return batavg

# Main
print("what is the players last name?")
lname = input()
print("how many times was the player at bat?")
atbats = int(input())
print("how many hits did the player have?")
numhit = int(input())
compbatavg(numhit, atbats)
batavg = compbatavg(numhit, atbats)
print("the player " + lname + "has a batting avg of " + str(batavg))
