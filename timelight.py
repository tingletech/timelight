import array
import time
from random import randint
from ola.ClientWrapper import ClientWrapper
from pprint import pprint as pp

def DmxSent(state):
    wrapper.Stop()

universe = 0
wrapper = ClientWrapper()
client = wrapper.Client()
while True:
    data = array.array('B', [randint(0,255), randint(0,255), randint(0,100), randint(0,80)])
    #data = array.array('B', [randint(0,255), randint(0,255), randint(0,255), randint(0,100)])
    pp(data)
    client.SendDmx(universe, data, DmxSent)
    wrapper.Run()
    time.sleep(5)
