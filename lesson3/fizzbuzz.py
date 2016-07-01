# if, elif, else
# kamen = 1
# nojnicy = 2
# bumaga = 3

# player1 = input('sdelect number from 1 to 3:')
# player2 = input('sdelect number from 1 to 3:')
#
# if player1 == player2:
#     print 'draw'
# elif player1 == 1 and player2 == 3:
#     print 'player2 win'
# elif player1 == 2 and player2 ==1:
#     print 'player2 win'
# elif player1 == 3 and player2 == 2:
#     print 'player2 win'
# elif player1 == 3 and player2 == 1:
#     print 'player1 win'
# elif player1 == 2 and player2 == 3:
#     print 'player1 win'
# elif player1 == 1 and player2 == 2:
#     print 'player1 win'




# if player1 == player2:
#     print 'draw'
#     elif (player1 == 1 and player2 != 3) or (player1 == 2 and player2 == != 1)\
#     or (player1 == 3 and player2 == != 2):
#     print 'player1 win'
# else:
#     print 'player2 win'




number = input('select number:')

if (number % 3 or number % 5) == 0:
    print 'FizzBuzz'
elif number % 3 == 0:
    print 'Fizz'
elif number % 5 == 0:
    print 'Buzz'

