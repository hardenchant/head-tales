"""
Toss a coin game.
Win condition - your combination will meet first
"""
import os
import random
import time

winners_table = {
    "TTT": "HTT",
    "TTH": "HTT",
    "THT": "TTH",
    "THH": "TTH",
    "HTT": "HHT",
    "HTH": "HHT",
    "HHT": "THH",
    "HHH": "THH",
}

GAMES_COUNT = 100
TOSS_COUNT = 1000


def break_generator(count: int) -> str:
    return "".join([random.choice(["H", "H", "H", "T"]) for _ in range(count)])


def generate_k_random_toss(count: int) -> str:
    a = time.time()
    # More slow generators
    # res = "".join(["H" if int(i) else "T" for i in bin(random.getrandbits(count))[2:].zfill(count)])
    # res = "".join([random.choice(["H", "T"]) for _ in range(count)])
    res = "".join([bin(b)[2:].zfill(8) for b in os.urandom(count // 8 + 1)])
    res = res.replace('0', 'H').replace('1', 'T')[:count]
    print(time.time() - a)
    return res


def game(predict1: str, predict2: str, generator: generate_k_random_toss = generate_k_random_toss):
    for _ in range(GAMES_COUNT):
        toss_results = generator(TOSS_COUNT)
        res1 = toss_results.find(predict1)
        res2 = toss_results.find(predict2)
        if res1 < res2:
            return 0, toss_results
        elif res1 > res2:
            return 1, toss_results
        return -1, toss_results


def interact():
    computer_choice = generate_k_random_toss(3)

    print(f"{computer_choice} - computer_choice")

    your_choice = input("Enter your choice: ")

    print(game(computer_choice, your_choice))


games = 10000
print(f"Local games count: {games}")
print(f"Games in local game count: {GAMES_COUNT}")
print(f"Toss count: {TOSS_COUNT}")


def check3():
    for choice, win_choice in winners_table.items():
        win_win = 0
        win_cho = 0
        for _ in range(games):
            g_res = game(choice, win_choice)
            if g_res[0] == 0:
                win_cho += 1
            elif g_res[0] == 1:
                win_win += 1
        print(f"{choice}:{win_choice} - {win_cho / games}:{win_win / games}")


def check_k():
    k = 5

    for choice, win_choice in {bin(i)[2:].zfill(k): bin(i)[2:].zfill(k)[-1] + bin(i)[2:].zfill(k)[:-1] for i in
                               range(2 ** k)}.items():
        choice = choice.replace('0', 'H').replace('1', 'T')
        win_choice = win_choice.replace('0', 'H').replace('1', 'T')
        win_win = 0
        win_cho = 0
        for _ in range(games):
            g_res = game(choice, win_choice)
            if g_res[0] == 0:
                win_cho += 1
            elif g_res[0] == 1:
                win_win += 1
        print(f"{choice}:{win_choice} - {win_cho / games}:{win_win / games}")


# check_k()
n = 1000000000
tss = generate_k_random_toss(n)
print(tss.count('T') / n)
print(tss.count('H') / n)
