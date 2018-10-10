#Codecademy Pro
#2018-10-10
#Introduction to Python Project
#script.py

# Initial set-up for our store
lovely_loveseat_description = '''
Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
'''
lovely_loveseat_price = 254.00

stylish_settee_description = '''
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
'''
stylish_settee_price = 180.50

luxurious_lamp_description = '''
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
'''
luxurious_lamp_price = 52.15
sales_tax = 0.088

# Initial set-up for our first customer
customer_one_total = 0
customer_one_itemization =''

# First customer purchases a Lovely Loveseat
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description

# First customer also purchases Luxurious Lamp
customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description

# First customer is ready to check out
customer_one_tax = customer_one_total * sales_tax

customer_one_total += customer_one_tax

print('Customer One Items:')
print(customer_one_itemization)

print('Customer One Total:')
print(customer_one_total)

# Initial set-up for our second customer
customer_two_total = 0
customer_two_itemization =''

# Second customer purchases Stylish Settee
customer_two_total += stylish_settee_price
customer_two_itemization += stylish_settee_description

# Second customer purchases Luxurious Lamp
customer_two_total += luxurious_lamp_price
customer_two_itemization += luxurious_lamp_description

# Second customer is ready to check out
customer_two_tax = customer_two_total * sales_tax

customer_two_total += customer_two_tax

print('Customer Two Items:')
print(customer_two_itemization)

print('Customer Two Total:')
print(customer_two_total)
