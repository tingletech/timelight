from __future__ import division
import array
import time
from random import randint
from ola.ClientWrapper import ClientWrapper
from pprint import pprint as pp
import datetime
import itertools

# global variables
wrapper = ClientWrapper()
client = wrapper.Client()


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


# while True:
    # data = array.array('B', [randint(0,255), randint(0,255), randint(0,100), randint(0,80)])
    # print('hello')
    #data = array.array('B', [randint(0,255), randint(0,255), randint(0,255), randint(0,100)])
    # dmx_send(data)
    # time.sleep(5)

def rand(minute):
    return randint(0,255)

for minute in itertools.cycle(range(0, 1439)):
    print(minute)
    r = rand(minute)
    g = rand(minute)
    b = rand(minute)
    x = rand(minute)
    dmx_send(r, g, b, x)
    time.sleep(0.25)
