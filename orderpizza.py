# Created by: Aden Rao
# Created on: March 14, 2019
# This program will tell you to choose between two sizes of pizza large or extra large then you type it in. Then it will ask you how many toppings you want and once you type in between 1 and 4 it will print the subtotal, taxes and the total cost.

# Variable for the pizza size that the user inputs and this also asks the user to enter large or extra large
pizza_size = input( ''' 
What size pizza would you like?
Type "large" for a Large Pizza.
Type "extra large" for an Extra Large Pizza.
''')

# If statement for the large or extra large pizza size. This also asks the user to input between a number between 1 and 4 for their toppings
if pizza_size == 'large' or pizza_size == 'extra large':
	toppings = int(input( 'Enter how many toppings you would like between 1 and 4: '))
	if pizza_size == 'large':
		if toppings == 1:
			subtotal = 6 + 1 
			print( 'Subtotal: ${}'.format(round(subtotal, 2)))
			tax = subtotal * 0.13
			print( 'Tax: ${}'.format(round(tax, 2)))
			total = subtotal + tax 
			print( 'Total: ${}'.format(round(total, 2)))
		elif toppings == 2:
			subtotal = 6 + 1.75 
			print( 'Subtotal: ${}'.format(round(subtotal, 2)))
			tax = subtotal * 0.13
			print( 'Tax: ${}'.format(round(tax, 2)))
			total = subtotal + tax 
			print( 'Total: ${}'.format(round(total, 2)))
		elif toppings == 3:
			subtotal = 6 + 2.50 
			print( 'Subtotal: ${}'.format(round(subtotal, 2)))
			tax = subtotal * 0.13
			print( 'Tax: ${}'.format(round(tax, 2)))
			total = subtotal + tax 
			print( 'Total: ${}'.format(round(total), 2)	)
		elif toppings == 4:
			subtotal = 6 + 3.35 
			print( 'Subtotal: ${}'.format(round(subtotal, 2)))
			tax = subtotal * 0.13
			print( 'Tax: ${}'.format(round(tax, 2)))
			total = subtotal + tax 
			print( 'Total: ${}'.format(round(total, 2)))
		else:
			# Tell the user that they have inputed an invalid amount of toppings if they enter a number that's not 1,2,3 or 4
			print('Invalid # of toppings. Please restart and choose a value between 1 and 4.')
	# The part of the if statement for the cost of the extra large pizza
	elif pizza_size == 'extra large':
		if toppings == 1:
			subtotal = 10 + 1 
			print( 'Subtotal: ${}'.format(round(subtotal, 2)))
			tax = subtotal * 0.13
			print( 'Tax: ${}'.format(round(tax, 2)))
			total = subtotal + tax 
			print( 'Total: ${}'.format(round(total, 2)))
		elif toppings == 2:
			subtotal = 10 + 1.75 
			print( 'Subtotal: ${}'.format(round(subtotal, 2)))
			tax = subtotal * 0.13
			print( 'Tax: ${}'.format(round(tax, 2)))
			total = subtotal + tax 
			print( 'Total: ${}'.format(round(total, 2)))
		elif toppings == 3:
			subtotal = 10 + 2.50 
			print( 'Subtotal: ${}'.format(round(subtotal, 2)))
			tax = subtotal * 0.13
			print( 'Tax: ${}'.format(round(tax, 2)))
			total = subtotal + tax 
			print( 'Total: ${}'.format(round(total), 2)	)
		elif toppings == 4:
			subtotal = 10 + 3.35 
			print( 'Subtotal: ${}'.format(round(subtotal, 2)))
			tax = subtotal * 0.13
			print( 'Tax: ${}'.format(round(tax, 2)))
			total = subtotal + tax 
			print( 'Total: ${}'.format(round(total, 2)))
		else:
			# Tell the user that they have inputed an invalid amount of toppings if they enter a number that's not 1,2,3 or 4
			print('Invalid # of toppings. Please restart and choose a value between 1 and 4.')
	else:
		#If they enter a size that is not larg or extra large.
	    print( 'Invalid size. Please restart and type "large" or "extra large".')
else: 
	print( 'Invalid size. Please restart and type "large" or "extra large".')


input('Thank you for ordering a pizza!')
