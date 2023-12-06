with open('day2\day2input.txt') as f:
    content = f.readlines()

red_limit = 12
green_limit = 13
blue_limit = 14


class Day:
    def __init__(self, daystring:str):
        daystring = daystring.split(";")
        daystring[0] = daystring[0].split(":")
        self.day:int = int(daystring[0][0][5:])
        self.sets = [daystring[0][1]]
        self.sets += daystring[1:]
        self.maxred = 0
        self.maxgreen = 0
        self.maxblue = 0

def find_maxrgb(day:Day):
    for set in day.sets:
        set = set.split(",")
        for item in set:
            item = item.split(" ")
            amount = int(item[1])
            color = item[2]
            color = color.strip()
            if color == "red":
                day.maxred = max(day.maxred, amount)
            elif color == "green":
                day.maxgreen = max(day.maxgreen, amount)
            elif color == "blue":
                day.maxblue = max(day.maxblue, amount)
            else:
                print("**" + color + "** is not a valid color")
                return False

def check_item(color:str, amount:int):
    if color == "red":
        return amount <= red_limit
    elif color == "green":
        return amount <= green_limit
    elif color == "blue":
        return amount <= blue_limit
    else:
        print("**" + color + "** is not a valid color")
        return False
    
def check_set(set:str):
    set = set.split(",")
    for item in set:
        item = item.split(" ")
        amount = int(item[1])
        color = item[2]
        color = color.strip()
        is_valid = check_item(color, amount)
        if not is_valid:
            print(f"found invalid item: [{amount} {color}]")
            return False
    return True

def check_day(day:Day):
    for set in day.sets:
        is_valid = check_set(set)
        if not is_valid:
            return False
    return True


# part 1
sum = 0
for line in content:
    day = Day(line)
    print(f"checking day {day.day}")
    print(f"sets: {day.sets}")

    if check_day(day):
       print(f"day {day.day} is valid\n")
       continue 
    else:
        sum += day.day
        print(f"day {day.day} is invalid\n")
print(5050-sum)



# part 2
sum = 0
for line in content:
    day = Day(line)
    print(f"checking day {day.day}")
    
    find_maxrgb(day)
    print(f"r: {day.maxred}, g: {day.maxgreen}, b: {day.maxblue}")
    sum += day.maxred * day.maxgreen * day.maxblue

print(sum)