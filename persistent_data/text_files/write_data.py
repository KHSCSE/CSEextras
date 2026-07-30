# where is this program storing the data?
my_data = input("What would you like to store?")
f = open("CSEextras/persistent_data/data.txt", "a")
f.write(my_data)
f.write("\n") # writes a newline after each item
f.close()

# TODO run this program several times
# observe the contents of "data.txt"