import time


def HASH(word : str):
    val = 0
    for char in word:
        val += ord(char)
        val *= 17
        val = val % 256
    return val
        
def advent15_1():
    #file = open('input15_example.txt')
    file = open('input15.txt')
    sequence = file.readline().strip('\n').split(',')
    #print(sequence)
    sum = 0
    for word in sequence:
        sum += HASH(word)
    print('Sum is (1)', sum)


class Lens:
    def  __init__(self, focal_len : int, label : str):
        self.focal_len = focal_len
        self.label = label


class Box:
    def __init__(self):
        self.lenses = list()

    def remove_lens(self, label):
        found = False
        for idx in range(len(self.lenses)):
            if self.lenses[idx].label == label:
                found = True
                break
        if found:
            self.lenses.pop(idx)

    def add_lens(self, label, focal_len):
        found = False
        for idx in range(len(self.lenses)):
            if self.lenses[idx].label == label:
                found = True
                break
        if found:
            self.lenses[idx].focal_len = focal_len
        else:
            self.lenses.append(Lens(focal_len, label))

    def printme(self):
        for l in self.lenses:
            print('[', l.label, l.focal_len, ']')
    
    def calc_focus_power(self):
        sum = 0
        for l in range(len(self.lenses)):
            sum += (l + 1)*self.lenses[l].focal_len
        return sum
    
            
def advent15_2():
    #file = open('input15_example.txt')
    file = open('input15.txt')
    sequence = file.readline().strip('\n').split(',')
    #print(sequence)
    sum = 0
    boxes = list()
    for box in range(256):
        boxes.append(Box())
    for word in sequence:
        #print(word)
        if word[-1] == '-':
            label = word[:-1]
            box = HASH(label)
            boxes[box].remove_lens(label)
            #print('Box:', box)
            #boxes[box].printme()
        else:
            eq = word.find('=')
            label = word[:eq]
            box = HASH(label)
            foc_len = int(word[eq+1:])
            boxes[box].add_lens(label, foc_len)
            #print('Box:', box)
            #boxes[box].printme()

    focus_power = 0
    for box in range(256):
        focus_power += boxes[box].calc_focus_power()*(box + 1)

    print('Foc. Pow (2):', focus_power)

    
if __name__ == '__main__':

    start_time = time.time()
    print('Advent 15')
    advent15_1()
    advent15_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
