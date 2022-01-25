import random
import time
from playsound import playsound

#delete 6.57 and enter length of audio clip (in seconds) here:
len = 6.57

def timersound():
    start = time.time()
    #default turn length is anywhere between 0 and 10 minutes per turn, "60" converts the random number b/w 0 and 1 into seconds
    time.sleep(10 * 60 * random.random())
    #enter path to sound you'd like to use to signal a rotation
    playsound('/Users/user/audiofile')
    end = time.time()
    #change 6.57 to length of audio file imported
    print('Time Elapsed:', round(((end - start - len)/60),2), 'minutes')
    print('Rotate!')

input('Press Enter to Start timer')

while True:
    timersound()