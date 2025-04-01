def who_won(game_board: list):
    player_1_score = 0
    player_2_score = 0

    for i in range(len(game_board)):
        for j in range(len(game_board[i])):
            if game_board[i][j] == 1:
                player_1_score += 1
            elif game_board[i][j] == 2:
                player_2_score += 1

    if player_1_score > player_2_score:
        return 1
    elif player_2_score > player_1_score:
        return 2
    else:
        return 0
