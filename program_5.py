# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost. 
hotDog = 3.50
chiliDog = 4.50
cheese = 0.50
peppers = 0.75
grilledOnions = 1.00

hotDogAmount = int(input('How many Hot Dogs do you want: '))
chiliDogAmount = int(input('How many Chili Dogs do you want: '))
cheeseAmount  = int(input('How many servings of Cheese do you want: '))
peppersAmount = int(input('How many ser ings of Pepers do you want: '))
grilledOnionsAmount = int(input('How many servings of Grilled Onions do you want: '))

subtotal = (hotDog*hotDogAmount) + (chiliDog*chiliDogAmount) + (cheese*cheeseAmount) + (peppers*peppersAmount) +(grilledOnions*grilledOnionsAmount)
print(('subtotal=$'),subtotal)
tax = (subtotal*.07)
print(('tax=$'),tax)
total = tax + subtotal
print(('total=$'),round(total, 2))
