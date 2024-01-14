import time


def mapping(number : int, mappings : list):
    for mapping in mappings:
        source_range = range(int(mapping[1]), int(mapping[1]) + int(mapping[2]))
        if int(number) in source_range:
            return int(mapping[0]) - (int(mapping[1]) - int(number))

    return number


def check_ranges(ranges : list, msg=''):
    for r in ranges:
        if r[0] > r[1]:
            print('Erroneous range:', r, msg)
            
    
def mapping2(ranges : list, mappings : list):
    old_ranges = ranges.copy()
    ret_ranges = list()
    for mupping in mappings:
        lower, upper = int(mupping[1]), int(mupping[1]) + int(mupping[2]) - 1
        new_ranges = list()
        check_ranges(old_ranges)
        for r in old_ranges:
            if r[0] >= lower and r[1] <= upper:
                l = mapping(r[0], [mupping])
                u = mapping(r[1], [mupping])
                ret_ranges.append([l, u])
            elif r[0] > upper or r[1] < lower:
                new_ranges.append(r)
            elif r[0] >= lower and r[1] >= upper:
                l = mapping(r[0], [mupping])
                u = mapping(upper, [mupping])
                ret_ranges.append([l, u])
                new_ranges.append([upper + 1, r[1]])
            elif r[0] <= lower and r[1] <= upper:
                l = mapping(lower, [mupping])
                u = mapping(r[1], [mupping])
                ret_ranges.append([l, u])
                new_ranges.append([r[0], lower - 1])
            elif r[0] < lower and r[1] > upper:
                l = mapping(lower, [mupping])
                u = mapping(upper, [mupping])
                ret_ranges.append([l, u])
                new_ranges.append([r[0], lower - 1])
                new_ranges.append([upper + 1, r[1]])
            else:
                print('WE SHOULD nOT BE HERE??!!')
                print('lower, upper:', lower, upper)
                print('r:', r)
            old_ranges = new_ranges.copy()

    for r in new_ranges:
        ret_ranges.append(r)
    return ret_ranges
            
                
def calc_seeds(seeds : list):
    ret_seeds = list()
    for num in range(int(len(seeds)/2)):
        start = int(seeds[2*num])
        nofs = int(seeds[2*num + 1])
        ret_seeds.append([start, start + nofs - 1])

    return ret_seeds


def advent5_1():
    #file = open('input05_example.txt')
    file = open('input05.txt')
    seedline = file.readline().strip('\n')
    seeds = seedline.split(': ')[1].split()

    seed_to_soil = list()
    soil_to_fertilizer = list()
    fertilizer_to_water = list()
    water_to_light = list()
    light_to_temperature = list()
    temperature_to_humidity = list()
    humidity_to_location = list()
    for line in file:
        row = line.strip('\n')
        if row.find('seed-to-soil') > -1:
            for num_row in file:
                if num_row.strip('\n') == '':
                    break
                seed_to_soil.append(num_row.strip('\n').split())

        if row.find('soil-to-fertilizer') > -1:
            for num_row in file:
                if num_row.strip('\n') == '':
                    break
                soil_to_fertilizer.append(num_row.strip('\n').split())

        if row.find('fertilizer-to-water') > -1:
            for num_row in file:
                if num_row.strip('\n') == '':
                    break
                fertilizer_to_water.append(num_row.strip('\n').split())

        if row.find('water-to-light') > -1:
            for num_row in file:
                if num_row.strip('\n') == '':
                    break
                water_to_light.append(num_row.strip('\n').split())

        if row.find('light-to-temperature') > -1:
            for num_row in file:
                if num_row.strip('\n') == '':
                    break
                light_to_temperature.append(num_row.strip('\n').split())

        if row.find('temperature-to-humidity') > -1:
            for num_row in file:
                if num_row.strip('\n') == '':
                    break
                temperature_to_humidity.append(num_row.strip('\n').split())

        if row.find('humidity-to-location') > -1:
            for num_row in file:
                if num_row.strip('\n') == '':
                    break
                humidity_to_location.append(num_row.strip('\n').split())

    soils = []
    for seed in seeds:
        soils.append(mapping(seed, seed_to_soil))
    #print('soils')
    fertilizers = []
    for soil in soils:
        fertilizers.append(mapping(soil, soil_to_fertilizer))
    #print('fertilizers')
    waters = []
    for fertilizer in fertilizers:
        waters.append(mapping(fertilizer, fertilizer_to_water))
    #print('waters')
    lights = []
    for water in waters:
        lights.append(mapping(water, water_to_light))
    #print('lights')
    temperatures = []
    for light in lights:
        temperatures.append(mapping(light, light_to_temperature))
    #print('temperatures')
    humiditys = []
    for temperature in temperatures:
        humiditys.append(mapping(temperature, temperature_to_humidity))
    #print('humiditys')
    locations = []
    for humidity in humiditys:
        locations.append(mapping(humidity, humidity_to_location))
    #print('locations')
    print('Min .location (1): ', min(locations))

    
def advent5_2():
    #file = open('input05_example.txt')
    file = open('input05.txt')
    seedline = file.readline().strip('\n')
    seeds = calc_seeds(seedline.split(': ')[1].split())
    #print(seeds)

    seed_to_soil = list()
    soil_to_fertilizer = list()
    fertilizer_to_water = list()
    water_to_light = list()
    light_to_temperature = list()
    temperature_to_humidity = list()
    humidity_to_location = list()
    for line in file:
        row = line.strip('\n')
        if row.find('seed-to-soil') > -1:
            for num_row in file:
                if num_row.strip('\n') == '':
                    break
                seed_to_soil.append(num_row.strip('\n').split())

        if row.find('soil-to-fertilizer') > -1:
            for num_row in file:
                if num_row.strip('\n') == '':
                    break
                soil_to_fertilizer.append(num_row.strip('\n').split())

        if row.find('fertilizer-to-water') > -1:
            for num_row in file:
                if num_row.strip('\n') == '':
                    break
                fertilizer_to_water.append(num_row.strip('\n').split())

        if row.find('water-to-light') > -1:
            for num_row in file:
                if num_row.strip('\n') == '':
                    break
                water_to_light.append(num_row.strip('\n').split())

        if row.find('light-to-temperature') > -1:
            for num_row in file:
                if num_row.strip('\n') == '':
                    break
                light_to_temperature.append(num_row.strip('\n').split())

        if row.find('temperature-to-humidity') > -1:
            for num_row in file:
                if num_row.strip('\n') == '':
                    break
                temperature_to_humidity.append(num_row.strip('\n').split())

        if row.find('humidity-to-location') > -1:
            for num_row in file:
                if num_row.strip('\n') == '':
                    break
                humidity_to_location.append(num_row.strip('\n').split())

    soils = mapping2(seeds, seed_to_soil)
    check_ranges(soils, ' in soils')
    #print(soils)
    fertilizers = mapping2(soils, soil_to_fertilizer)
    check_ranges(fertilizers, ' in fertilizers')
    #print(fertilizers)
    waters = mapping2(fertilizers, fertilizer_to_water)
    check_ranges(waters, ' in waters')
    #print(waters)
    lights = mapping2(waters, water_to_light)
    check_ranges(lights, ' in lights')
    #print(lights)
    temperatures = mapping2(lights, light_to_temperature)
    check_ranges(temperatures, ' in temperatures')
    #print(temperatures)
    humiditys = mapping2(temperatures, temperature_to_humidity)
    check_ranges(humiditys, ' in humiditys')
    locations = mapping2(humiditys, humidity_to_location)
    check_ranges(locations, ' in locations')
    #print(locations)
    min_loc = 2**32
    for loc in locations:
        min_loc = min(min_loc, loc[0])

    print('Min. loc. (2):', min_loc)
    
    
if __name__ == '__main__':
    # 95461669 answer for first seed interval
    # 910845529
    
    start_time = time.time()
    print('Advent 5')
    advent5_1()
    advent5_2()
    end_time_1 = time.time()
    print("time elapsed: {:.2f}s".format(end_time_1 - start_time))
