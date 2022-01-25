import random
import numpy as np
from matplotlib import pyplot as plt 
import matplotlib.ticker as plticker

print("Press return to roll, type 'stop' to end the game")

rollhistory = []

def diceroll(): 
    dye1 = random.randint(1,6)
    dye2 = random.randint(1,6)
    roll = dye1 + dye2
    print('**', roll, '**')
    rollhistory.append(roll)

while True:
    x = input('Roll:')
    if x == '':
        diceroll()

    elif x == 'stop':
        print('GG EZ')
        
        #HISTOGRAM FORMATTING - DO NOT TOUCH
        fig, main_ax = plt.subplots()
        main_ax.set_xlim(1.5,12.5)
        loc = plticker.MultipleLocator(base=1.0)
        main_ax.xaxis.set_major_locator(loc)
        loc = plticker.MultipleLocator(base=2.0)
        main_ax.yaxis.set_major_locator(loc)
        main_ax.set_xlabel('roll')
        main_ax.set_ylabel('number of rolls')
        main_ax.set_title("It's not the rolls you are just bad")
        labels, counts = np.unique(rollhistory, return_counts=True)
        plt.bar(labels, counts, align='center')
        plt.gca().set_xticks(labels)
        plt.show()
        break

    else:
        print("enter either 'stop' or press return")