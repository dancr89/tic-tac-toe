from .board import board_matrix, get_options, show
from .status import check_status
from .player import get_current_player



def start():
    """
    This is the engine of the game.
    """
    is_over = False
    step = 0

    print('Welcome and good kuck!')


    while not is_over:
        name, sign = get_current_player(step)
        print('%s is your turn' % name)

        available_options = get_options(board_matrix)

        show(board_matrix)
        print('Pick a choice from available options:', available_options)

        choice = input('Pick your choice: ')
        try:
            choice = int(choice)

            if choice not in available_options:
                raise ValueError()

            is_correct_choice = True
        except ValueError:
            print('Your choice is not an option')
            is_correct_choice = False
            continue

        #play the game
        is_won, is_over = check_status(board_matrix)

        step += 1

    print('Game Over!')