with open("day6input.txt") as f:
    content = f.readlines()


flag = True

while flag:
    flag = False
    for index in range(len(content)):
        if content[index].find("  ") != -1:
            flag = True
            content[index] = content[index].replace("  ", " ")

for index in range(len(content)):
    content[index] = content[index].replace("\n","").split(" ")

times = content[0][1:]

distances = content[1][1:]


def test_track(time:str, distance:str):
    time = int(time)
    distance = int(distance)

    winning_attempts = 0

    for i in range(0, time):
        if i * (time-i) > distance:
            winning_attempts += 1

    return winning_attempts

sum = 1
for i in range(len(times)):
    sum *= test_track(times[i], distances[i])

print(sum) # part 1

# Part 2
def test_track2(time:str, distance:str):
    time = int(time)
    distance = int(distance)

    winning_attempts = 0
    for i in range(10000000, time-10000000):
        if len(str(i)) * 2 < len(str(time)):
            continue
        if i * (time-i) > distance:
            # no need to check for the rest of the numbers
            print(f"found time and distance: {i}, {time-i}")
            print(time-2*i+1) # +1 since we are counting both start and end
            break

test_track2(60808676,601116315591300) # part 2