from datetime import datetime, timedelta
from tkinter import filedialog

import pygame as pg
from pygame import mixer
import random
from tkinter import *
from tkinter import filedialog

pg.init()


##creates clock

class Clock:
    def openFile(self):
        filepath = filedialog.askopenfilename()
        self.alarm_sound = filepath

    def __init__(self):
        self.answer = None
        Button(command=self.openFile())
        mixer.music.load(self.alarm_sound)
        self.time = input('input your time in military time')
        tomorrow = datetime.now() + timedelta(days=1)
        tomorrow_date = tomorrow.strftime('%Y-%m-%d')
        self.time = datetime.strptime(tomorrow_date + ' ' + self.time, '%Y-%m-%d %H:%M')
        self.is_ringing = False

    def problem(self):
        a = random.randint(3, 12)
        b = random.randint(3, 12)
        print(str(a) + '*' + str(b))
        self.answer = str(a * b)
        return self.answer

    def toggle(self):
        if not self.is_ringing:
            mixer.music.play(-1)
            print('Alarm started')

            self.is_ringing = True
        else:
            correct_answer = self.problem()
            my_answer = str(input('solve the problem to turn off the alarm'))
            while my_answer != correct_answer:
                my_answer = str(input('Try Again'))
            mixer.music.stop()
            self.is_ringing = False


# Creates clock object
clock = Clock()
print(clock.time)

time = datetime.now()
# when setting alarms past midnight this prevents it from playing the day after you'd like to wake up
if (clock.time - timedelta(days=1)) > time:
    clock.time = clock.time - timedelta(days=1)

print(time)
print(clock.time)
while time < clock.time:
    time = datetime.now()


# alarm rings
clock.toggle()
# alarm is off
clock.toggle()
print('you woke up, congrats. Not only did your code work, you are now up when you wanted to be.Go pat yourself on the back.')
