with open("day4input.txt") as f:
    content:list[str] = f.readlines()


rawtickets = []
for line in content:
    line = line.strip().split("|")
    line[0] = line[0].split(":")
    rawticket = [sublist for sublist in line[0]] + [line[1]]
    rawtickets.append(rawticket)

class Ticket:
    def __init__(self, rawticket:list[str]):
        self.cardnum = int(rawticket[0][5:].strip())
        self.winnernums = [int(num) for num in rawticket[1].split()]
        self.mynums = [int(num) for num in rawticket[2].split()]
        self.timeswon = -1
        
    def get_value(self):
        if self.timeswon == -1:
            return 0
        return 2**self.timeswon

def checkticket(ticket:Ticket):
    for num in ticket.mynums:
        if num in ticket.winnernums:
            ticket.timeswon += 1


sum = 0
for rawticket in rawtickets:
    ticket = Ticket(rawticket)
    checkticket(ticket)
    print(ticket.cardnum, ticket.timeswon)
    sum += ticket.get_value()

print(sum) # answer of part 1

# Part 2
print("\n\n\n\n\n\n\n\n\n\n\n\n")




tix_powers = {i: 1 for i in range(1, 1+len(rawtickets))}

class Ticket2:
    def __init__(self, rawticket:list[str]):
        self.cardnum = int(rawticket[0][5:].strip())
        self.winnernums = [int(num) for num in rawticket[1].split()]
        self.mynums = [int(num) for num in rawticket[2].split()]
        self.timeswon = 0
        self.copies = 1



tickets:list[Ticket2] = []

for rawticket in rawtickets:
    ticket = Ticket2(rawticket)
    checkticket(ticket)
    tickets.append(ticket)

# all tickets are now initialized

for ticket in tickets:
    current_ticket_index = ticket.cardnum-1
    for i in range(ticket.timeswon):
        tickets[current_ticket_index+i+1].copies += ticket.copies

sum = 0
for ticket in tickets:
    print(ticket.cardnum, ticket.copies)
    sum += ticket.copies

print(sum) # part 2 done