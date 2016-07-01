
menu = [
    {
        'name' : 'ceaser',
        'price' : 180,
        'mass' : 300,

    },
    {
        'name' : 'steak',
        'price' : 350,
        'mass' : 600,

    },
]
select = raw_input('food')
quantity = input ('quantity')
service = 15
discount = 10
balance = 200

#esli est skidka ispolzovat ee
#new peremennye (sidka, balance)

for m in menu:
    if  select == m ['name']:
        subtotal = m ['price'] * quantity
        total = subtotal - (subtotal * discount/100) + (subtotal * service/100) - balance
        print total
