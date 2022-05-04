# ---------------------------------------------------------------------Game start ------------------------------------------------------------------------------------------------
def tictactoe(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")


# Function to check if any player has won or the game continues
def winner(player_position, current_player):
    # All possible winning combinations
    solutions = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

    # Loop to check if any winning combination is satisfied
    for n in solutions:
        if all(y in player_position[current_player] for y in n):
            # Return True if any winning combination satisfies
            return True
    # Return False if no combination is satisfied
    return False


# Function to check if the game is drawn
def check_draw(player_pos):
    if len(player_pos['X']) + len(player_pos['O']) == 9:
        return True
    return False


def game(current_player):
    values = [' ' for x in range(9)]

    # Stores the positions occupied by X and O
    player_position = {'X': [], 'O': []}

    # Game Loop for a single game of Tic Tac Toe
    while True:
        tictactoe(values)

        # Try exception block for MOVE input
        try:
            print("Player ", current_player, " turn. Which box? : ")
            move = int(input())
        except ValueError:
            print("This space doesn't exist, please try again")
            continue

        # does the space entered exist
        if move < 1 or move > 9:
            print("This space doesn't exist, please try again")

        # Check if the box is not occupied already
        if values[move - 1] != ' ':
            print("Place already filled. Try again")

        # Updating grid status
        values[move - 1] = current_player

        # Updating player positions
        player_position[current_player].append(move)

        # Function call for checking win
        if winner(player_position, current_player):
            tictactoe(values)
            print("Player ", current_player, " has won the game!!")
            print("\n")
            return current_player

        # Function call for checking draw game
        if check_draw(player_position):
            tictactoe(values)
            print("Game Drawn")
            print("\n")
            return 'D'

        # Switch player moves
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

game("X")