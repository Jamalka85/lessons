# restaurant bill: menu, total amount, service

food = raw_input('Bludo')
price = input('Price')
quantity = input('Quantity')
service = 15

total = price * quantity + ((price * quantity) * service/100)

if food in menu:
    print 'Bludo %s, Price: %s Quantity: %s  total: %s' % (food, price, quantity, total)
