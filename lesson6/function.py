# def get_name(name):
#     return 'name'
#
# def get_number(number):
#     return number ** 2
# print get_number(5)

# def get_login(name, surname):
#     return  name[0]+surname
# print get_login('jama', 'crutch')



     #
# def get_bill(discount, price, quantity, service):
#     amount = price * quantity
#     service = amount * service/100
#     discount = (amount + service) * discount/100
#     total = (amount + service) - discount
#     return total
# print get_bill(10, 100, 2, 15)



    #
# def get_bill(discount, price, quantity, service):
#     amount = price * quantity
#     service = amount * service/100
#     discount = (amount + service) * discount/100
#     total = (amount + service) - discount
#     return {
#         'total' : total,
#         'discount': discount,
#         'service' : service,
#         'amount' : amount
#     }
# bill = get_bill(10, 100, 2, 15)
#
# print bill['discount']

# company
def get_team(name, surname, gender, age, title, salary, experience):
    return {
    'name': 'Oleg',
    'surname' : 'Kim',
    'gender': 'male',
    'age' : 26,
    'title' : 'manager',
    'salary' : '6000',
    'experience' : '3'
    },

    {
    'name': 'Masha',
    'surname' : 'Kant',
    'gender': 'female',
    'age' : 22,
    'title' : 'weitress',
    'salary' : '4000',
    'experience' : '1'
    },

    {
    'name': 'Jason',
    'surname' : 'Miller',
    'gender': 'male',
    'age' : 25,
    'title' : 'barmen',
    'salary' : '5000',
    'experience' : '2'
    },

    {
    'name': 'Mark',
    'surname' : 'Fish',
    'gender': 'male',
    'age' : 28,
    'title' : 'security',
    'salary' : '4000',
    'experience' : '3'
    }
    print get_team['age']