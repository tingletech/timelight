from __future__ import division
import array
import time
from random import randint
from ola.ClientWrapper import ClientWrapper
from pprint import pprint as pp
import datetime
import itertools
import math

# global variables
wrapper = ClientWrapper()
client = wrapper.Client()


def colorize(minute, frequency=0.03, amplitude=127, center=128):
    value = math.sin(minute * frequency) * amplitude + center
    return int(round(value,1))


def minutes_since_midnight():
    now = datetime.datetime.now()
    midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
    seconds = (now - midnight).seconds
    return seconds // 60


def dmx_send(r, g, b, x, universe=0):
    ''' wrapper for open lighting '''

    def DmxSent(state):
        # callback on send
        wrapper.Stop()

    data = array.array('B', [ r, g, b, x ])
    client.SendDmx(universe, data, DmxSent)
    wrapper.Run()


def adjust_color(minute):
    r = colorize(minute, frequency=0.004363323129985824)
    g = colorize(minute + 480, frequency=0.004363323129985824)
    b = colorize(minute + 960, frequency=0.004363323129985824)
    x = colorize(minute + 960, frequency=0.004363323129985824)
    print(minute, r, g, b, x)
    dmx_send(r, g, b, x)


while True:
    minute = minutes_since_midnight()
    adjust_color(minute)
    time.sleep(60)

def rand(minute):
    return randint(0,255)


for minute in range(0, 1439):
# for minute in itertools.cycle(range(0, 1439, 20)):
    adjust_color(minute)
    time.sleep(0.01)
