with open('inputs/day3input.txt') as f:
    content = f.readlines()

# Part 1
# chars = ["#", "+", "%", "=", "@", "-", "$", "/", "*", "&"]
#
# enginearray:list[str] = []
#
# for line in content:
#     for char in chars:
#         line = line.strip()
#         line = line.replace(char, "A")
#     enginearray.append(line)
#
#
#
#
# valid_coords = []
# x = 0
# for line in enginearray:
#     y = 0
#     for char in line:
#         if char == "A": # mark the surrounding 8 squares as valid
#             for i in range(-1, 2):
#                 for j in range(-1, 2):
#                     if (x+i, y+j) not in valid_coords:
#                         valid_coords.append((x+i, y+j))
#         y += 1
#     x += 1
#
# # now at least one cell of every number block is marked as valid
# # now we have to find the number blocks that are valid
# # a number block is valid if at least one of its cells is valid
# # we need to add the number blocks to get the answer
#
#
# def find_number_block(line:str, x:int, y:int):
#     registering = True
#     validated = False
#     number_block = ""
#     while registering:
#         if y >= line.__len__():
#             registering = False
#             break
#         if line[y].isdigit():
#             number_block += line[y]
#             if (x, y) in valid_coords:
#                 validated = True
#                 valid_coords.remove((x, y))
#             y += 1
#         else:
#             registering = False
#
#     if validated:
#         print("found number block at", x, y)
#         valid_number_blocks.append(number_block)
#         print(number_block)
#
#     return number_block.__len__()
#
#
# # find the number blocks
# valid_number_blocks = []
# x = 0
# for line in enginearray:
#     y = 0
#     for char in line:
#         if char.isdigit():
#             len = find_number_block(line, x, y)
#             y += len-1
#
#         y += 1
#     x += 1
#
# sum = 0
# for block in valid_number_blocks:
#     sum += int(block)
#
# print("Part 1:", sum)

# Part 2
chars = ["#", "+", "%", "=", "@", "-", "$", "/", "&"]

enginearray: list[str] = []

for line in content:
    for char in chars:
        line = line.strip()
        line = line.replace(char, ".")
    enginearray.append(line)

gears = []

x = 0
for line in enginearray:
    y = 0
    for char in line:
        if char == "*":
            if (x, y) not in gears:
                gears.append((x, y))
        y += 1
    x += 1

# now we have the gears
# we need to find if these gears link 2 number blocks together
# if they do, we need to multiply the number blocks and add them to the answer
# if not, we can ignore them


def find_number_block_in_a_line(line: str, y: int):
    numstr = ""
    while y >= 0 and line[y].isdigit():
        y -= 1
    # either number blocks have ended or we have reached the start of the line, so we need to go back one step
    y += 1
    # now we are at the start of the number block
    # its time to register the number block
    while y < line.__len__() and line[y].isdigit():
        numstr += line[y]
        y += 1

    return int(numstr)


def find_gear_blocks(x: int, y: int):
    num1 = None
    num2 = None
    for i in range(-1, 2):
        for j in range(-1, 2):
            if enginearray[x+i][y+j].isdigit():
                numfound = find_number_block_in_a_line(enginearray[x+i], y+j)
                if num1 == None:
                    num1 = numfound
                else:
                    num2 = numfound

    if num2 != None and num1 != num2:
        print(num1, "*", num2, "=", int(num1) * int(num2))
        return int(num1) * int(num2)
    else:
        print("fail")
        return 0


sum = 0
for gear in gears:
    print("gear at", gear, end=": ")
    a = find_gear_blocks(gear[0], gear[1])
    sum += a
print("Part 2:", sum)
