from random import choice


def roll(die: str):
    die_a = [3, 3, 3, 3, 3, 6]
    die_b = [2, 2, 2, 5, 5, 5]
    die_c = [1, 4, 4, 4, 4, 4]

    if die == "A":
        return choice(die_a)
    if die == "B":
        return choice(die_b)
    if die == "C":
        return choice(die_c)


def play(die1: str, die2: str, times: int):
    die1_win_count = 0
    die2_win_count = 0
    for i in range(times):
        die1_result = roll(die1)
        die2_result = roll(die2)
        if die1_result > die2_result:
            die1_win_count += 1
        elif die2_result > die1_result:
            die2_win_count += 1
    draw = times - (die1_win_count + die2_win_count)
    return (die1_win_count, die2_win_count, draw)
