with open("inputs/day8input.txt") as f:
    data = f.readlines()

# Part 1

directions = data[0].strip()
print(directions)

mapstrs = data[2:]

maps = {mapstr[:3]: [mapstr[7:10], mapstr[12:15]] for mapstr in mapstrs}


def go_to_direction(direction: str, base: str):
    if direction == "L":
        return maps[base][0]
    elif direction == "R":
        return maps[base][1]
    else:
        raise ValueError("Invalid direction")


total_steps = 0

is_done = False

base = "AAA"

while not is_done:

    direction = directions[total_steps % len(directions)]
    base = go_to_direction(direction, base)
    total_steps += 1
    print(base, total_steps)
    if base == "ZZZ":
        is_done = True

print(total_steps) # part 1 answer

# Part 2

start_points = []

for key in maps.keys():
    if key[2] == "A":
        start_points.append(key)

total_steps = 0

all_bases_in_z = True

while True:
    all_bases_in_z = True
    for index in range(len(start_points)):
        base = start_points[index]
        direction = directions[total_steps % len(directions)]
        start_points[index] = go_to_direction(direction, base)
        if start_points[index][2] != "Z":
            all_bases_in_z = False
            print(start_points[index], total_steps)
    
    total_steps += 1
    if all_bases_in_z:
        print(total_steps)
        break