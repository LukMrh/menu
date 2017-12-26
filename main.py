print "Welcome to this menu!"

menu = {}

while True:
    new_food = raw_input("Enter your dish name:")
    new_price = raw_input("Please enter your price for '%s' :" % new_food) # %s string formatting
    menu[new_food] = new_price

    again = raw_input("Would you like to start again (y/n)?")
    if again.lower() == "n":
        break


with open("menu.txt", "w+") as menu_file:  # opens and overwrites previous file (w+)
    for food, price in menu.iteritems():
        menu_file.write("%s, %s EUR\n" % (food, menu[food]))  # write text into file with new line  - (\n)

print "Menu '%s' " % menu
print "Goodbye!"

