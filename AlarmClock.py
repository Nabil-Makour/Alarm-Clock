from datetime import datetime, timedelta
import pygame as pg
from pygame import mixer
import random

pg.init()

##creates clock
def problem():
    a = random.randint(3, 12)
    b = random.randint(3, 12)
    print(str(a) + '*' + str(b))
    answer = a * b
    return answer

class Clock:
    def __init__(self):
        self.alarm_sound = r'C:\Users\21mak\OneDrive\Desktop\alarm clock files\Air Raid Siren Sound Effect.mp3'
        mixer.music.load(self.alarm_sound)
        self.time = input('input your time in military time')
        tomorrow = datetime.now() + timedelta(days=1)
        tomorrow_date = tomorrow.strftime('%Y-%m-%d')
        self.time = datetime.strptime(tomorrow_date + ' ' + self.time, '%Y-%m-%d %H:%M')
        self.is_ringing = False

    def toggle(self):
        if not self.is_ringing:
            mixer.music.play(-1)
            print('Alarm started')
            self.is_ringing = True
        else:
            mixer.music.stop()
            self.is_ringing = False


##Creates clock object
clock = Clock()
print(clock.time)
##alarm logic
time = datetime.now()
print(time)

while time < clock.time:
    time = datetime.now()

##alarm rings
clock.toggle()
##turnoff mechanism
correct_answer = problem()
my_answer = input('solve the problem to turn off the alarm')
while my_answer != correct_answer:
    try:
        my_answer = int(my_answer)
        while my_answer != correct_answer:
            my_answer = int(input('Try Again'))
    except ValueError:
        my_answer = int(input("Invalid input. Please enter a number."))


##alarm is off
clock.toggle()
print('you woke up, congrats. Not only did your code work, you are now up when you wanted to be. Go pat yourself on the back')
