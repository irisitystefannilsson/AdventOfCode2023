import time


def advent1_1():
    file = open('input01.txt')
    rows = list()
    sum = 0
    for line in file:
        rows.append(line)
        for c in line:
            if c.isdigit():
                first_dig = c
                break
        for c in reversed(line):
            if c.isdigit():
                last_dig = c
                break

        sum += int(first_dig + last_dig)

    print('Sum : ', sum)


def advent1_2():
    file = open('input01.txt')
    rows = list()
    sum = 0
    nums = {'one' : '1', 'two' : '2', 'three' : '3', 'four' : '4', 'five' : '5', 'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9'}
    for line in file:
        rows.append(line)
        pos = 0
        for c in line:
            if c.isdigit():
                first_dig = c
                break
            pos += 1
        for n in nums.keys():
            if line.find(n) < pos and line.find(n) != -1:
                first_dig = nums[n]
                pos = line.find(n)
        pos = len(line) - 1
        for c in reversed(line):
            if c.isdigit():
                last_dig = c
                break
            pos -= 1
        for n in nums.keys():
            if line.rfind(n) > pos:
                last_dig = nums[n]
                pos = line.rfind(n)

        sum += int(first_dig + last_dig)

    print('Sum : ', sum)

    
if __name__ == '__main__':

    start_time = time.time()
    print('Advent 1')
    advent1_1()
    advent1_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
