from enum import Enum
import time
import numpy as np
import functools
import math
import copy

NUMBER_OF_CALLS = 0
LOG_FILE = open('logfile.txt', 'w')
DATA_CACHE = dict()
USED = []
ALLCONSTR = list()
MODULES = dict()

class STATE(Enum):
    OFF = 0
    ON = 1

class PULSE(Enum):
    LOW = 0
    HIGH = 1

PULSES_SENT = dict()
PULSES_SENT[PULSE.LOW] = 0
PULSES_SENT[PULSE.HIGH] = 0

UNRELEASED_PULSES = list()

class Module:
    def __init__(self, name : str, dests : list):
        self.name = name
        self.dests = dests
        self.inputs = list()
        self.saved_signal = list()

    def add_input(self, input_name : str):
        self.inputs.append(input_name)

    def pulse_input(self, sender : str, pulse : PULSE):
        PULSES_SENT[pulse] += 1
        #print(sender, '-', pulse, '->', self.name)
        if self.name == 'cn' and pulse == PULSE.HIGH and len(DATA_CACHE) < 4:
            DATA_CACHE[sender] = NUMBER_OF_CALLS
        #    print('SENDER IS:', sender, 'Button push no.:', NUMBER_OF_CALLS)
        #    raise        
        #time.sleep(2)

    def release_signal(self):
        #print('release', self.name)
        if len(self.saved_signal) != 0:
            signal = self.saved_signal.pop(0)
            for dest in self.dests:
                MODULES[dest].pulse_input(self.name, signal)

    def graph_box(self):
        return self.name + ';'
    
class Broadcaster(Module):
    def __init__(self, name : str, dests : list):
        super().__init__(name, dests)
        self.inputs = ['button']

    def pulse_input(self, sender : str, pulse : PULSE):
        super().pulse_input(sender, pulse)
        self.saved_signal.append(pulse)
        UNRELEASED_PULSES.append(self.name)
        #for dest in self.dests:
        #    MODULES[dest].pulse_input(self.name, pulse)
    
    def graph_box(self):
        return self.name + ' [shape=box];'

class FlipFlop(Module):
    def __init__(self, name : str, dests : list):
        super().__init__(name, dests)
        self.state = STATE.OFF

    def flip_state(self):
        if self.state == STATE.ON:
            self.state = STATE.OFF
        else:
            self.state = STATE.ON
            
    def pulse_input(self, sender : str, pulse : PULSE):
        #print(self.name, self.state, pulse)
        super().pulse_input(sender, pulse)
        if pulse == PULSE.HIGH:
            return
        else:
            if self.state == STATE.OFF:
                self.saved_signal.append(PULSE.HIGH)
                #for dest in self.dests:
                #    MODULES[dest].pulse_input(self.name, PULSE.HIGH)
            else:
                self.saved_signal.append(PULSE.LOW)
                #for dest in self.dests:
                #    MODULES[dest].pulse_input(self.name, PULSE.LOW)
            self.flip_state()
            UNRELEASED_PULSES.append(self.name)
            
    def graph_box(self):
        return self.name + ' [shape=ellipse, color=red];'

class Conjunction(Module):
    def __init__(self, name : str, dests : list):
        super().__init__(name, dests)
        self.input_states = dict()

    def add_input(self, input_name : str):
        super().add_input(input_name)
        self.input_states[input_name] = PULSE.LOW
        
    def pulse_input(self, sender : str, pulse : PULSE):
        super().pulse_input(sender, pulse)
        self.input_states[sender] = pulse
        if all(value == PULSE.HIGH for value in self.input_states.values()):
            self.saved_signal.append(PULSE.LOW)
            #for dest in self.dests:
            #    MODULES[dest].pulse_input(self.name, PULSE.LOW)
        else:
            self.saved_signal.append(PULSE.HIGH)
            #for dest in self.dests:
            #    MODULES[dest].pulse_input(self.name, PULSE.HIGH)
        UNRELEASED_PULSES.append(self.name)

    def graph_box(self):
        return self.name + ' [shape=diamond, color=green];'


def advent20_1():
    #file = open('input20_example2.txt')
    file = open('input20.txt')

    for line in file:
        line = line.strip('\n')
        if 'broadcaster' in line:
            dests = line.split(' -> ')[1]
            dests = dests.split(', ')
            MODULES['broadcaster'] = Broadcaster('broadcaster', dests)
        else:
            modtype = line[0]

            if modtype == '%':
                name, dests = line[1:].split(' -> ')
                dests = dests.split(', ')
                MODULES[name] = FlipFlop(name, dests)
            elif modtype == '&':
                name, dests = line[1:].split(' -> ')
                dests = dests.split(', ')
                MODULES[name] = Conjunction(name, dests)
            else:
                name = line[1:].split(' ->')[0]
                #print(name)
                dests = list()
                MODULES[name] = Module(name, dests)
                
    for key, module in MODULES.items():
        for dest in module.dests:
            MODULES[dest].add_input(key)

    for p in range(1000):
        MODULES['broadcaster'].pulse_input('button', PULSE.LOW)
        while len(UNRELEASED_PULSES) != 0:
            name = UNRELEASED_PULSES.pop(0)
            MODULES[name].release_signal()

    print('Low x High pulses:', PULSES_SENT[PULSE.LOW]*PULSES_SENT[PULSE.HIGH])


def advent20_2():
    #file = open('input20_example2.txt')
    file = open('input20.txt')

    for line in file:
        line = line.strip('\n')
        if 'broadcaster' in line:
            dests = line.split(' -> ')[1]
            dests = dests.split(', ')
            MODULES['broadcaster'] = Broadcaster('broadcaster', dests)
        else:
            modtype = line[0]

            if modtype == '%':
                name, dests = line[1:].split(' -> ')
                dests = dests.split(', ')
                MODULES[name] = FlipFlop(name, dests)
            elif modtype == '&':
                name, dests = line[1:].split(' -> ')
                dests = dests.split(', ')
                MODULES[name] = Conjunction(name, dests)
            else:
                name = line[1:].split(' ->')[0]
                #print(name)
                dests = list()
                MODULES[name] = Module(name, dests)
                
    for key, module in MODULES.items():
        for dest in module.dests:
            MODULES[dest].add_input(key)
    LOG_FILE.write('digraph {\n')
    for key, module in MODULES.items():
        #print(module.name, module.inputs, module.dests)
        for dest in module.dests:
            LOG_FILE.write(module.graph_box() + '\n')
            LOG_FILE.write(module.name + ' -> ' + dest + ';\n')
    LOG_FILE.write('}\n')
    global NUMBER_OF_CALLS
    for p in range(10000):
        NUMBER_OF_CALLS = p + 1
        MODULES['broadcaster'].pulse_input('button', PULSE.LOW)
        while len(UNRELEASED_PULSES) != 0:
            name = UNRELEASED_PULSES.pop(0)
            MODULES[name].release_signal()

    global DATA_CACHE
    button_pushes = 1
    for key, item in DATA_CACHE.items():
        button_pushes *= item

    print('Button pushes needed:', button_pushes)

    
if __name__ == '__main__':

    start_time = time.time()
    print('Advent 20')
    advent20_1()
    advent20_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
