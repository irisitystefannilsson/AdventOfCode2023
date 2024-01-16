import time


def to_equation(p : list, v : list):
    k = v[1] / v[0]
    m = (p[1] - k*p[0])

    return k, m


def calc_intersect(k0 : float, m0 : float, k1 : float, m1 : float):
    if k0 == k1:
        return float('inf'), float('inf')
    x = (m1 - m0)/(k0 - k1)
    y = k0*x + m0

    return x, y


def within_box(x : float, y : float, box : list):
    if (box[0][0] <= x <= box[0][1]) and (box[1][0] <= y <= box[1][1]):
        return True
    return False


def in_the_future(p : list, v : list, x : float, y : float):
    if x > p[0] and v[0] > 0 and y > p[1] and v[1] > 0:
        return True
    if x > p[0] and v[0] > 0 and y < p[1] and v[1] < 0:
        return True
    if x < p[0] and v[0] < 0 and y > p[1] and v[1] > 0:
        return True
    if x < p[0] and v[0] < 0 and y < p[1] and v[1] < 0:
        return True
    return False

    
def advent24_1():
    #file = open('input24_example.txt'); box = [[7, 27], [7, 27]]
    file = open('input24.txt'); box = [[200000000000000, 400000000000000], [200000000000000, 400000000000000]]

    poss = list()
    vels = list()
    eqs = list()
    for line in file:
        line = line.strip('\n')
        p, v = line.split(' @ ')
        p = [int(e) for e in p.split(', ')]
        v = [int(e) for e in v.split(', ')]
        poss.append(p)
        vels.append(v)
        eqs.append(to_equation(p, v))

    nof_crosses = 0
    for i in range(len(eqs)):
        for j in range(i + 1, len(eqs)):
            k0, m0 = eqs[i][0], eqs[i][1]
            k1, m1 = eqs[j][0], eqs[j][1] 
            x, y= calc_intersect(k0, m0, k1, m1)
            if within_box(x, y, box) and in_the_future(poss[i], vels[i], x, y) and in_the_future(poss[j], vels[j], x, y):
                nof_crosses += 1
    print('Crossing paths in box (1):', nof_crosses)


def advent24_2():
    #file = open('input24_example.txt');
    file = open('input24.txt');

    poss = list()
    vels = list()
    for line in file:
        line = line.strip('\n')
        p, v = line.split(' @ ')
        p = [int(e) for e in p.split(', ')]
        v = [int(e) for e in v.split(', ')]
        poss.append(p)
        vels.append(v)

    x1, y1, z1, v1x, v1y, v1z = poss[0][0], poss[0][1], poss[0][2], vels[0][0], vels[0][1], vels[0][2]
    x2, y2, z2, v2x, v2y, v2z = poss[1][0], poss[1][1], poss[1][2], vels[1][0], vels[1][1], vels[1][2]
    x3, y3, z3, v3x, v3y, v3z = poss[2][0], poss[2][1], poss[2][2], vels[2][0], vels[2][1], vels[2][2]

    # these were obtained using maxima
    # starting from the equations for intersection with the first 3 hail stones
    # with the thrown stone (9 equations and 9 unknowns (X,Y, Z, Vx, Vy, Vz, t1, t2, t3)
    t1 = (((v3x - v2x)*y2 + (v2x - v3x)*y1 + (v2y - v3y)*x2 + (v3y - v2y)*x1)*z3
          + ((v2x - v3x)*y3 + (v3x - v2x)*y1 + (v3y - v2y)*x3 + (v2y - v3y)*x1)*z2
          + ((v3x - v2x)*y3 + (v2x - v3x)*y2 + (v2y - v3y)*x3 + (v3y - v2y)*x2)*z1
          + ((v3z - v2z)*x2 + (v2z - v3z)*x1)*y3 + ((v2z - v3z)*x3 + (v3z - v2z)*x1)*y2
          + ((v3z - v2z)*x3 + (v2z - v3z)*x2)*y1) \
    /(((v2x - v1x)*v3y + (v1y - v2y)*v3x + v1x*v2y - v1y*v2x)*z3
      + ((v1x - v2x)*v3y + (v2y - v1y)*v3x - v1x*v2y + v1y*v2x)*z2
      + ((v1x - v2x)*v3z + (v2z - v1z)*v3x - v1x*v2z + v1z*v2x)*y3
      + ((v2x - v1x)*v3z + (v1z - v2z)*v3x + v1x*v2z - v1z*v2x)*y2
      + ((v2y - v1y)*v3z + (v1z - v2z)*v3y + v1y*v2z - v1z*v2y)*x3
      + ((v1y - v2y)*v3z + (v2z - v1z)*v3y - v1y*v2z + v1z*v2y)*x2)

    t2 = (((v3x - v1x)*y2 + (v1x - v3x)*y1 + (v1y - v3y)*x2 + (v3y - v1y)*x1)*z3
          + ((v1x - v3x)*y3 + (v3x - v1x)*y1 + (v3y - v1y)*x3 + (v1y - v3y)*x1)*z2
          + ((v3x - v1x)*y3 + (v1x - v3x)*y2 + (v1y - v3y)*x3 + (v3y - v1y)*x2)*z1
          + ((v3z - v1z)*x2 + (v1z - v3z)*x1)*y3 + ((v1z - v3z)*x3 + (v3z - v1z)*x1)*y2
          + ((v3z - v1z)*x3 + (v1z - v3z)*x2)*y1) \
    /(((v2x - v1x)*v3y + (v1y - v2y)*v3x + v1x*v2y - v1y*v2x)*z3
      + ((v1x - v2x)*v3y + (v2y - v1y)*v3x - v1x*v2y + v1y*v2x)*z1
      + ((v1x - v2x)*v3z + (v2z - v1z)*v3x - v1x*v2z + v1z*v2x)*y3
      + ((v2x - v1x)*v3z + (v1z - v2z)*v3x + v1x*v2z - v1z*v2x)*y1
      + ((v2y - v1y)*v3z + (v1z - v2z)*v3y + v1y*v2z - v1z*v2y)*x3
      + ((v1y - v2y)*v3z + (v2z - v1z)*v3y - v1y*v2z + v1z*v2y)*x1)
    
    t3 = (((v2x - v1x)*y2 + (v1x - v2x)*y1 + (v1y - v2y)*x2 + (v2y - v1y)*x1)*z3
          + ((v1x - v2x)*y3 + (v2x - v1x)*y1 + (v2y - v1y)*x3 + (v1y - v2y)*x1)*z2
          + ((v2x - v1x)*y3 + (v1x - v2x)*y2 + (v1y - v2y)*x3 + (v2y - v1y)*x2)*z1
          + ((v2z - v1z)*x2 + (v1z - v2z)*x1)*y3 + ((v1z - v2z)*x3 + (v2z - v1z)*x1)*y2
          + ((v2z - v1z)*x3 + (v1z - v2z)*x2)*y1) \
    /(((v2x - v1x)*v3y + (v1y - v2y)*v3x + v1x*v2y - v1y*v2x)*z2
      + ((v1x - v2x)*v3y + (v2y - v1y)*v3x - v1x*v2y + v1y*v2x)*z1
      + ((v1x - v2x)*v3z + (v2z - v1z)*v3x - v1x*v2z + v1z*v2x)*y2
      + ((v2x - v1x)*v3z + (v1z - v2z)*v3x + v1x*v2z - v1z*v2x)*y1
      + ((v2y - v1y)*v3z + (v1z - v2z)*v3y + v1y*v2z - v1z*v2y)*x2
      + ((v1y - v2y)*v3z + (v2z - v1z)*v3y - v1y*v2z + v1z*v2y)*x1)

    print('Collision times:', int(t1), int(t2), int(t3))

    X = -(t1*((- x2) - t2*v2x) + t2*x1 + t1*t2*v1x) / (t1 - t2)
    Vx =  ((- x2) + x1 - t2*v2x + t1*v1x ) / (t1 - t2)

    Y = -(t1*((- y2) - t2*v2y) + t2*y1 + t1*t2*v1y) / (t1 - t2)
    Vy = ((- y2) + y1 - t2*v2y + t1*v1y) / (t1 - t2)

    Z = -(t1*((- z2) - t2*v2z) + t2*z1 + t1*t2*v1z) / (t1 - t2)
    Vz = ((- z2) + z1 - t2*v2z + t1*v1z) / (t1 - t2)
    print('Coords & velocity:', int(X), int(Y), int(Z), int(Vx), int(Vy), int(Vz))

    print('Sum of coords (2):', int(X + Y + Z))

    
if __name__ == '__main__':
    start_time = time.time()
    print('Advent 24')
    advent24_1()
    advent24_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
