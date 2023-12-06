with open("day5input.txt") as f:
    content = f.read()

raw_data = content.split("\n\n")

# Part 1

seeds = raw_data[0][7:].split(" ") # 
for i in seeds:
    seeds[seeds.index(i)] = int(i)

def parse_this(data:str):
    half_parsed = data.split("\n")[1:]
    parsed = []
    for line in half_parsed:
        parsed.append(line.split(" "))
    parsed_to_num = []
    for line in parsed:
        parsed_to_num.append([int(element) for element in line])

    return parsed_to_num

seed_to_soil = parse_this(raw_data[1])
seed_to_soil.sort()


soil_to_fertilizer = parse_this(raw_data[2])
soil_to_fertilizer.sort()

fertilizer_to_water = parse_this(raw_data[3])
fertilizer_to_water.sort()

water_to_light = parse_this(raw_data[4])
water_to_light.sort()

light_to_temperature = parse_this(raw_data[5])
light_to_temperature.sort()

temperature_to_humidity = parse_this(raw_data[6])
temperature_to_humidity.sort()

humidity_to_location = parse_this(raw_data[7])
humidity_to_location.sort()

def find_match(input:int, table:list[list[int]]):
    for line in table:
        if input in range(line[1], line[1]+ line[2]):
            return line[0] + (input - line[1])
    
    return input

def full_rotation(seed:int):
    soil = find_match(seed, seed_to_soil)
    fertilizer = find_match(soil, soil_to_fertilizer)
    water = find_match(fertilizer, fertilizer_to_water)
    light = find_match(water, water_to_light)
    temperature = find_match(light, light_to_temperature)
    humidity = find_match(temperature, temperature_to_humidity)
    location = find_match(humidity, humidity_to_location)

    return location

def reverse_full_rotation(location:int):
    humidity = find_match(location, humidity_to_location)
    temperature = find_match(humidity, temperature_to_humidity)
    light = find_match(temperature, light_to_temperature)
    water = find_match(light, water_to_light)
    fertilizer = find_match(water, fertilizer_to_water)
    soil = find_match(fertilizer, soil_to_fertilizer)
    seed = find_match(soil, seed_to_soil)

    return seed

lowest = None
for seed in seeds:
    q = full_rotation(seed)
    if lowest == None:
        lowest = q
    elif q < lowest:
        lowest = q

print(f"lowest: {lowest}") # part 1


min = None
for i in range(0, len(seeds), 2):
    for j in range(seeds[i], seeds[i] + seeds[i+1]):
        print(f"range {seeds[i]} to {seeds[i] + seeds[i+1]}, current = {j}, min: {min}")
        q = full_rotation(j)
        if min == None:
            min = q
        elif q < min:
            min = q

print(f"min: {min}") # part 2