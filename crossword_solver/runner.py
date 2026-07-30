data = [] # this will be a 2D list of data
# for example:



f = open("insmall.txt")
# TODO read the text file into a 2D list


f.close()

print(data) # comment this out after you see that it works



# TODO complete the function to display the 2D list
def show(data):
    pass


show(data)







# given a 2D list and row & column numbers
# return how many "CSE" surround that spot vertically or horizontally
def look_udlr(data, r,c):
    found = 0
    # TODO

    return found    


# given a 2D list and row and column numbers
# return how many "CSE" surround that spot diagonally
def look_diag(data, r, c):
    found = 0
    # TODO
    
    return found








# the main algorithm:
# loop through, if you find a "C", look around for "S" and "E"
ans = 0
# TODO


print(ans)
# TODO when your algorithm is working, try the 'big' input file