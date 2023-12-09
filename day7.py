with open("inputs/day7input.txt") as f:
    data = f.readlines()

# 1000 players in game


class Player:
    def __init__(self, hand, bet):
        self.hand = hand
        self.bet = bet
        self.tier = find_hand_tier(hand)
        self.rank: int
        self.hand_point = 0
        self.won_money: int


def get_list_name(lst):
    # Iterate over the global variables and their values
    for name, value in globals().items():
        if value is lst:
            return name
    return None  # Return None if the list name is not found


def parse_line(line: str):
    line = line.split(" ")
    return line[0], int(line[1])


def find_hand_tier(hand: str):

    nums = []
    for char in hand:
        nums.append(hand.count(char))

    if 5 in nums:
        return "five_of_a_kind"
    elif 4 in nums:
        return "four_of_a_kind"
    elif 3 in nums and 2 in nums:
        return "full_house"
    elif 3 in nums:
        return "three_of_a_kind"
    elif nums.count(2) == 4:
        return "two_pair"
    elif nums.count(2) == 2:
        return "one_pair"
    else:
        return "high_card"


# Sort players by tier
five_of_a_kind: list[Player] = []
four_of_a_kind: list[Player] = []
full_house: list[Player] = []
three_of_a_kind: list[Player] = []
two_pair: list[Player] = []
one_pair: list[Player] = []
high_card: list[Player] = []

card_powers = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J",
               "Q", "K", "A"]  # 2 is lowest, A is highest


def sort_players_by_tier(player: Player):
    if player.tier == "five_of_a_kind":
        five_of_a_kind.append(player)
    elif player.tier == "four_of_a_kind":
        four_of_a_kind.append(player)
    elif player.tier == "full_house":
        full_house.append(player)
    elif player.tier == "three_of_a_kind":
        three_of_a_kind.append(player)
    elif player.tier == "two_pair":
        two_pair.append(player)
    elif player.tier == "one_pair":
        one_pair.append(player)
    elif player.tier == "high_card":
        high_card.append(player)


def calculate_hand_point(hand: str):
    hand_point = 0
    for index in range(len(hand)):
        current_card = hand[index]
        hand_point += (card_powers.index(current_card)+1) * \
            ((len(hand)-index) ** 20)

    return hand_point


players: list[Player] = []

for line in data:
    hand, bet = parse_line(line)
    myplayer = Player(hand, bet)
    sort_players_by_tier(myplayer)

for player in four_of_a_kind:
    player.hand_point = calculate_hand_point(player.hand)

for player in full_house:
    player.hand_point = calculate_hand_point(player.hand)

for player in three_of_a_kind:
    player.hand_point = calculate_hand_point(player.hand)

for player in two_pair:
    player.hand_point = calculate_hand_point(player.hand)

for player in one_pair:
    player.hand_point = calculate_hand_point(player.hand)

for player in high_card:
    player.hand_point = calculate_hand_point(player.hand)

# Sort players by hand point
five_of_a_kind.sort(key=lambda x: x.hand_point, reverse=True)
four_of_a_kind.sort(key=lambda x: x.hand_point, reverse=True)
full_house.sort(key=lambda x: x.hand_point, reverse=True)
three_of_a_kind.sort(key=lambda x: x.hand_point, reverse=True)
two_pair.sort(key=lambda x: x.hand_point, reverse=True)
one_pair.sort(key=lambda x: x.hand_point, reverse=True)
high_card.sort(key=lambda x: x.hand_point, reverse=True)

current_rank = 1
total_money = 0


for player in five_of_a_kind:
    player.rank = current_rank
    current_rank += 1
    player.won_money = player.bet * (1001 - player.rank)
    total_money += player.won_money
    print(f"{player.rank} {player.hand} {player.bet} {player.won_money}")


for player in four_of_a_kind:
    player.rank = current_rank
    current_rank += 1
    player.won_money = player.bet * (1001 - player.rank)
    total_money += player.won_money
    print(f"{player.rank} {player.hand} {player.bet} {player.won_money}")

for player in full_house:
    player.rank = current_rank
    current_rank += 1
    player.won_money = player.bet * (1001 - player.rank)
    total_money += player.won_money
    print(f"{player.rank} {player.hand} {player.bet} {player.won_money}")

for player in three_of_a_kind:
    player.rank = current_rank
    current_rank += 1
    player.won_money = player.bet * (1001 - player.rank)
    total_money += player.won_money
    print(f"{player.rank} {player.hand} {player.bet} {player.won_money}")

for player in two_pair:
    player.rank = current_rank
    current_rank += 1
    player.won_money = player.bet * (1001 - player.rank)
    total_money += player.won_money
    print(f"{player.rank} {player.hand} {player.bet} {player.won_money}")

for player in one_pair:
    player.rank = current_rank
    current_rank += 1
    player.won_money = player.bet * (1001 - player.rank)
    total_money += player.won_money
    print(f"{player.rank} {player.hand} {player.bet} {player.won_money}")

for player in high_card:
    player.rank = current_rank
    current_rank += 1
    player.won_money = player.bet * (1001 - player.rank)
    total_money += player.won_money
    print(f"{player.rank} {player.hand} {player.bet} {player.won_money}")

print(total_money)  # answer of part 1
