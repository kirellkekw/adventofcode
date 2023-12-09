with open("inputs/day9input.txt") as f:
    lines = f.readlines()

# Part 1


def list_to_int(mylist: list):
    for index in range(len(mylist)):
        mylist[index] = int(mylist[index])
    return mylist


for index in range(len(lines)):
    lines[index] = list_to_int(lines[index].strip().split(" "))

q = ["0 3 6 9 12 15", "1 3 6 10 15 21", "10 13 16 21 30 45"]

ex_input1 = list_to_int(q[0].split(" "))
ex_input2 = list_to_int(q[1].split(" "))
ex_input3 = list_to_int(q[2].split(" "))


def find_next_num(sequence: list, roots: list, tree_level: int = 0):
    if tree_level == 0:
        roots += [sequence]

    next_level = [sequence[index+1]-sequence[index]
                  for index in range(len(sequence)-1)]

    if tree_level == 0:
        for num in sequence:
            print(f"{num} ", end="")
        print("")

    print((1+tree_level)*" ", end="")
    for num in next_level:
        print(f"{num}", end=" ")
    print(end="\n")
    for num in next_level:
        if num != 0:
            roots += [next_level]
            return find_next_num(next_level, roots, tree_level+1)

    # print(roots)
    answer = 0
    for list in roots:
        answer += list[-1]

    return answer


total = 0
for line in lines:
    q = find_next_num(line, [])
    print(q)
    total += q

print(total)  # answer of part 1
