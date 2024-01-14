import time


def advent2_1():
    file = open('input02.txt')
    color_limits = {'red' : 12, 'green' : 13, 'blue' : 14}
    sum = 0
    for line in file:
        possible = True
        line = line.strip('\n')
        id = line.split(':')[0]
        id = int(id[5:])
        sets = line.split(':')[1].split(';')
        for s in sets:
            colors = s.split(',')
            for c in colors:
                #print(c)
                num = c.lstrip(' ').rstrip(' ').split(' ')
                if int(num[0]) > color_limits[num[1]]:
                    possible = False
        
        if possible:
            sum += id
 
    print('Sum : ', sum)


def advent2_2():
    file = open('input02.txt')
    sum = 0
    for line in file:
        color_limits = {'red' : 0, 'green' : 0, 'blue' : 0}
        line = line.strip('\n')
        id = line.split(':')[0]
        id = int(id[5:])
        sets = line.split(':')[1].split(';')
        for s in sets:
            colors = s.split(',')
            for c in colors:
                #print(c)
                num = c.lstrip(' ').rstrip(' ').split(' ')
                color_limits[num[1]] = max(color_limits[num[1]], int(num[0]))

        #print(color_limits)
        sum += color_limits['red']*color_limits['green']*color_limits['blue']
 
    print('Sum : ', sum)

    
if __name__ == '__main__':

    start_time = time.time()
    print('Advent 2')
    advent2_1()
    advent2_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
