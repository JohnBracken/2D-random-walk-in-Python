#The following code describes a 2D random walk
#where the walker can move in one of 4 directions (N, E, S or W)
#equal probability to move in any direction (0.25)



#Numeric Python library
import numpy as np


#Random number library
import random


#Plotting libary
from matplotlib import pyplot as plt


#Number of steps.  Chosen as 100 in this case.
N_steps = 10000


#probability of a step going North (X,Y) = (0, +1), set to between 0 and 0.25.
prob1 = 0.25


#probability of a step going East (X,Y) = (+1,0), set to between 0.25 and 0.5.
prob2 = 0.5


#probability of a step going South (X,Y) = (0,-1), set to between 0.5 and 0.75.
prob3 = 0.75


#probability of a step going west (X,Y) = (-1,0), set to between 0.75 and 1.  This will be the
#last remaining option so an extra variable is not needed.




#Define the random walk function.  N in this case is the total number of steps and
#the probability thresholds for steps in specific directions are also input arguements.
def TwoDRandomWalk(N, p1, p2, p3):


    #Create an array of X and Y positions for a walker.  And initialize the first position
    #to be the origin (zero).  The array will be the same size as the number of steps.
    #A position counter variable is also used, which is initialized to zero as well.

    #Arrays to store X and Y co-ordinate positions of the walker.
    position_X = np.empty(N)
    position_Y = np.empty(N)


    #Initialize starting position of the walker to be at the origin.
    position_X[0] = 0
    position_Y[0] = 0


    #Initialize the position counter to zero for both directions.
    pos_X_counter = 0
    pos_Y_counter = 0


    #Start the random walk.
    for i in range(1,N):


        #Generate a random probability value between 0 and 1.
        test = random.random()


        #Check the value of the probability generated and update the counter by a single N, E, S or W step
        #based on the value.
        if 0 <= test < p1:
            pos_Y_counter += 1

        elif p1 <= test < p2:
            pos_X_counter += 1

        elif p2 <= test < p3:
            pos_Y_counter -= 1

        else:
            pos_X_counter -= 1

        #Fill the current position array indices with the current values of the position counters from the loop.
        position_X[i] = pos_X_counter
        position_Y[i] = pos_Y_counter


    #Return the arrays of X and Y positions after each step in a given walk.
    return position_X, position_Y




#Function to generate histograms for both the final X and Y positions after a given walk is finished.
#For a large group of walkers starting at the origin, the histograms of the final positions should follow
#normal distributions over all walkers.
def Histograms(position_final_X, position_final_Y):


    #Histogram plot of the final horizontal position.
    plt.hist(position_final_X)
    plt.title("Final Horizontal Position Histogram")
    plt.xlabel("Horizontal Position")
    plt.ylabel("Frequency")
    plt.show()

    #Histogram plot of the final vertical position.
    plt.hist(position_final_Y)
    plt.title("Final Vertical Position Histogram")
    plt.xlabel("Vertical Position")
    plt.ylabel("Frequency")
    plt.show()

    return None



#Perform one random walk, generating arrays of X and Y positions.
X_positions, Y_positions = TwoDRandomWalk(N_steps, prob1, prob2, prob3)


#Plot the random walk.  Shows a plot of walker position on an X-Y grid.
plt.plot(X_positions, Y_positions, '-')
plt.xlabel('Horizontal position')
plt.ylabel('Vertical position')
plt.show()






#Now do a simulation of a large number of random walkers.  Set the initial value to 2000.
#All the walkers will start at the origin (X,Y) = (0,0).
walkers = 2000


#Generate arrays of X and Y final positions.
X_position_final = np.empty(walkers)
Y_position_final = np.empty(walkers)


#Create histograms of the final horizontal and vertical positions using data from all the walkers.
for i in range(walkers):

    #Create X and Y position arrays for aeach walker.
    X_positions, Y_positions = TwoDRandomWalk(N_steps, prob1, prob2, prob3)


    #Grab the final (X,Y) position of each walker.
    X_position_final[i] = X_positions[-1]
    Y_position_final[i] = Y_positions[-1]


#Generate and plot the histograms of final positions using the data from all the walkers.
Histograms(X_position_final, Y_position_final)

