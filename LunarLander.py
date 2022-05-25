# This program is a game which is about trying to land a space ship on the moom.
# The program aks the user how much of the fuel it should burn to decellerate
# the space ship. The idea of the program is to land on the moon without crashing.
# This is achieved if the landing velocity is less than 10 metres/second.
import sys
h = 1000  # height in metres
vel = 0  # velocity in m/s
f = 1000  # fuel in litres
fl = 0
t = 0   #time at start
fuelleft=0

print('Try to make the spaceship land safely')
print('On each turn, type in the amount of fuel you want to use to slow down the spaceship')
print('Careful though! You only have 1000 litres! Ready, set, go!')

print('How much fuel do you want to use on this turn? Positive numbers only!') #first turn
fl = float(input())

while not 0<=fl<=1000:
    print('enter a positive number between 0 and 1000.')
    fl = float(input())


while h > 0:
        t = t + 1
        vel = 1.6*t - 0.15*fl #0.15 is an artibrary constant. If it is lower, game is harder
        h = h - vel
        f = f-fl

        if h<=0 and vel<=10:
            print('You have successfully landed the lander, contratulations!')
            print('Height is: 0m', 'Velocity is: '+ str(vel)+'m/s', 'Fuel left is: ' + str(f) + 'l',
                  'Time is: ' + str(t) + 's')
        else:
            if f<=0:
                print('Height is: '+ str(h) + 'm,', 'Velocity is: ' + str(vel)+'m/s,', 'Fuel left is: ' + str(f) + 'l,','Time is: ' + str(t)+'s')
                print('There is no more fuel left and you have not landed. You have lost. Please restart the game.')
                sys.exit()
            else:
                print('Height is: ' + str(h)+' m.', 'Velocity is: ' + str(vel)+' m/s', 'Fuel left is:'+str(f)+ 'l.', 'Time is: ' + str(t)+'s')
                if h<=0:
                    print('You have lost. The lander has crashed. Please play again.')
                    sys.exit()
                print('Next go. How much fuel do you want to use?')
                fuelleft = f
                fl = float(input())
                while not 0<=fl<=fuelleft:
                    print('You cant use more fuel than you have left. Please enter between: 0 and ', str(fuelleft))
                    fl =float(input())



if h<=0:
    print('You have finished playing the game, do you want to play again?')
    print('Please enter Y or N:')
    game_replay = input()

    if game_replay == 'Y':
        print('simply run the .py file again')
        sys.exit()
    elif game_replay =='N':
        print('close the game down by closing this window')
        sys.exit()
    else:
        print('Incorrect input. The game will stop. If you want to play again, simply run the game file again.')
