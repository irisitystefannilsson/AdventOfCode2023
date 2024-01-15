import time


ALLCONSTR = list()


class workflow:
    def __init__(self, instr : str):
        self.name, rules = instr.strip('}').split('{')
        self.rules = rules.split(',')

    def apply_rules(self, item : dict()):
        nor = len(self.rules)
        for r in range(nor):
            if r == nor  - 1:
                return self.rules[r]
            cond, dest = self.rules[r].split(':')
            rating, op, val = cond[0], cond[1], cond[2:]
            itval = item[rating]
            if eval(str(itval) + op + val):
                return dest

    def A_condition(self, wf : str):
        retrule = list()
        nor = len(self.rules)
        As = list()
        for r in range(nor):
            if r == nor  - 1:
                dest = self.rules[r]
                if dest == wf:
                    As.append(r)
            else:
                dest = self.rules[r].split(':')[1]
                if dest == wf:
                    As.append(r)
        for r in As:
            retrule.append([])
            if r == nor - 1:
                rating, op, val = 'a', '<', '4001'
            else:
                cond = self.rules[r].split(':')[0]
                rating, op, val = cond[0], cond[1], cond[2:]
            retrule[-1].append([rating, op, val])
            for br in range(r - 1, -1, -1):
                cond = self.rules[br].split(':')[0]
                rating, op, val = cond[0], cond[1], cond[2:]
                if op == '<':
                    op = '>'
                    val = str(int(val) - 1)
                else:
                    op = '<'
                    val = str(int(val) + 1)
                retrule[-1].append([rating, op, val])

        return retrule


def advent19_1():
    #file = open('input19_example.txt')
    file = open('input19.txt')

    workflows = dict()
    for line in file:
        line = line.strip('\n')
        if line == '':
            break
        wf = workflow(line)
        workflows[wf.name] = wf

    parts = list()
    x='x'
    m='m'
    a='a'
    s='s'
    for line in file:
        line = line.strip('\n')
        part = eval(line.replace('=', ':'))
        parts.append(part)

    sum = 0
    for p in parts:
        flow = 'in'
        while flow not in ['A', 'R']:
            flow = workflows[flow].apply_rules(p)

        if flow == 'A':
            sum += (p['x'] + p['m'] + p['a'] + p['s'])

    print('Sum (1):', sum)
    
    
def advent19_2():
    #file = open('input19_example.txt')
    file = open('input19.txt')

    workflows = dict()
    for line in file:
        line = line.strip('\n')
        if line == '':
            break
        wf = workflow(line)
        workflows[wf.name] = wf

    for key, wf in workflows.items():
        constr = wf.A_condition('A')
        for c in constr:
            #print(wf.name, c)
            if len(c) != 0:
                create_constr(workflows, key, c)
        
                
    hvol = 0
    pcubes = []
    num = 0
    for constr in ALLCONSTR:
        hcube = {'x' : (1, 4000), 'm' : (1, 4000), 'a' : (1,4000), 's' : (1, 4000)}
        for r in constr:
            if r[1] == '<':
                hcube[r[0]] = (hcube[r[0]][0], min(hcube[r[0]][1], int(r[2]) - 1))
            else:
                hcube[r[0]] = (max(hcube[r[0]][0], int(r[2]) + 1), hcube[r[0]][1])
        pcubes.append(HCube(hcube['x'], hcube['m'], hcube['a'], hcube['s'], str(num)))
        num += 1
        hvol += pcubes[-1].vol()

    intersect_cubes = list()
    intersect_cubes.append(pcubes)
    while True:
        intersect_cubes.append([])
        for cubel in pcubes:
            for cuber in intersect_cubes[-2]:
                if cubel.name not in cuber.name:
                    isec, icube = cubel.intersect(cuber)
                    if isec:
                        intersect_cubes[-1].append(icube)
        intersect_cubes[-1] = sorted(intersect_cubes[-1], key=lambda e: e.name)
        tempsec = list()
        for c in intersect_cubes[-1]:
            if len(tempsec) > 0 and c.name == tempsec[-1].name:
                continue
            tempsec.append(c)
        intersect_cubes[-1] = tempsec
        
        if len(intersect_cubes[-1]) == 0:
            break

    vol = 0
    for seclev in range(len(intersect_cubes)):
        lvol = 0
        for cube in intersect_cubes[seclev]:
            lvol += cube.vol()
        if seclev % 2 == 0:
            vol += lvol
        else:
            vol -= lvol

        #print(vol)
    print('All possible acc. (2):', hvol) 
        
    
class HCube:
    def __init__(self, b1 : tuple, b2 : tuple, b3 : tuple, b4 : tuple, name : str):
        self.bounds = [b1, b2, b3, b4]
        self.name = name

    def vol(self):
        return (self.bounds[0][1] - self.bounds[0][0] + 1)*(self.bounds[1][1] - self.bounds[1][0] + 1)*(self.bounds[2][1] - self.bounds[2][0] + 1)*(self.bounds[3][1] - self.bounds[3][0] + 1)
    
    def intersect(self, other):
        newname = ''.join(sorted(self.name + other.name))
        for dim in range(0, 4):
            if (self.bounds[dim][0] > other.bounds[dim][1] and self.bounds[dim][1] > other.bounds[dim][1]) or (self.bounds[dim][0] < other.bounds[dim][0] and self.bounds[dim][1] < other.bounds[dim][0]):
                return False, HCube([0, 0], [0, 0], [0, 0], [0, 0], newname)
        cube = []
        for dim in range(0, 4):
            low = max(self.bounds[dim][0], other.bounds[dim][0])
            high = min(self.bounds[dim][1], other.bounds[dim][1])
            cube.append([low, high])
        return True, HCube(cube[0], cube[1], cube[2], cube[3], newname)

    
def create_constr(workflows : list, start : str, chain : list):
    for key, wf in workflows.items():
        constr = wf.A_condition(start)
        for c in constr:
            if len(c) != 0:
                for e in c:
                    chain.append(e)
                if key == 'in':
                    ALLCONSTR.append(chain)
                else:
                    create_constr(workflows, key, chain)

                    
if __name__ == '__main__':

    start_time = time.time()
    print('Advent 19')
    advent19_1()
    advent19_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
