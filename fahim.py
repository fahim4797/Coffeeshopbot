print("Hi, welcome to Coffee House!!!!")
name = input("What's your name, sir?\n")

print("Hello " + name + ", thank you so much for coming in today.\n\n")

menu = "Cold brew, Espresso, Lattes, Cappuccino, Cortado, Drip coffee."

order = input(name + ", what would you like to have? Here's what we are serving:\n" + menu)


#Price adjustment
if order == "Cold brew":
    price = 70
elif order == "Espresso":
    price = 90
elif order == "Cappuccino":
    price = 85
elif order == "Drip coffee":
    price = 75
elif order == "Cortado":
    price = 95
elif order == "Lattes":
    price = 85
else:
    print("Sorry, we are not serving " + order + " here at this moment.")
    exit()
    
    
quantity = input("How many " + order + " do you  want?\n")

total = price * int(quantity)
totalk = str(total)
print("Thanks for the order.")
price = str(price)
print("Here's your order, " + name + ". It will be " + totalk + " taka demanding " + price + " taka for each " + order)
print("You can either pay in cash or using credit card. We accept both visa and mastercard.")
