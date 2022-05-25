# This program is a game which is about trying to land a space ship on the moom.
# The program aks the user how much of the fuel it should burn to decellerate
# the space ship. The idea of the program is to land on the moon without crashing.
# This is achieved if the landing velocity is less than 10 metres/second.
import os
import sys


full_path = os.path.realpath(__file__)
path, file_name = os.path.split(os.path.realpath(__file__))

def game():
    h = 1000  # height in metres
    vel = 0  # velocity in m/s
    f = 1000  # fuel in litres
    fl = -1
    t = 0   #time at start
    fuelleft=0

    print('Welcome to the Lunar Lander game. The objective of the game is to try to make the spaceship land safely.')
    print('On each turn, enter the amount of fuel you want to use to slow down the spaceship')
    print('Careful though! You only have a total of 1000 litres of fuel! Ready, set, go!')
    print('How much fuel do you want to use? Positive numbers only!') #first turn
#first fuel input here
    while not 0<=fl<=1000:
        try:
            fl = float(input('Enter a positive number between 0 and 1000.\n'))
        except ValueError:
            print ("fuel left must be a number, try again")
#whilst spacecraft is still flying (h>0), this code runs
    while h > 0:
            t = t + 1
            vel = 1.6*t - 0.3*fl #0.15 is an artibrary constant. If it is lower, game is harder
            h = h - vel
            f = f-fl

            if h<=0 and 0<=vel<=10: # negative velocity means rocket is moving away from the moon!
                print('You have successfully landed the lander, contratulations!')
                print('Height is: 0m', 'Velocity is: '+ str(vel)+'m/s', 'Fuel left is: ' + str(f) + 'l',
                      'Time is: ' + str(t) + 's')
            elif f<=0 and h>0:
                print('Height is: '+ str(h) + 'm,', 'Velocity is: ' + str(vel)+'m/s,', 'Fuel left is: ' + str(f) + 'l,','Time is: ' + str(t)+'s')
                print('There is no more fuel left and you have not landed. You have lost.')
                restart = input("\nDo you want to restart the game? [y/n] > ")

                if restart == "y":
                    game()
                else:
                    print("\nThe game will be closed...")
                    sys.exit(0)
            else:
                print('Height is: ' + str(h)+' m.', 'Velocity is: ' + str(vel)+' m/s', 'Fuel left is:'+str(f)+ 'l.', 'Time is: ' + str(t)+'s')
                if h<=0:
                    print('\nYou have lost. The lander has crashed.')
                    restart = input("\nDo you want to play again? [y/n] > ")
                    if restart == "y":
                        game()
                    else:
                        print("\nThe programm will me closed...")
                        sys.exit(0)
                #carry on playing till the fuel runs out or spaceship crash lands
                print('Next go. How much fuel do you want to use?')
                fl = float(input())
                while not 0<=fl<=f:
                    print('You cant use more fuel than you have left. Please enter between: 0 and ', str(fuelleft))
                    fl =float(input())

    if h<=0:
        print('You have finished playing the game, do you want to play again?')
        print('Please enter y or n:')
        game_replay = input()

        if game_replay == 'y':
            game()
        elif game_replay =='n':
            print('Game will close')
            sys.exit()
        else:
            print('Incorrect input. The game will stop. If you want to play again, simply run the game file again.')

game()
