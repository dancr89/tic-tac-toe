def check_winning_sequance(sequance):
    """


    Winning sequance
    :param sequance:
    :return:
    """

def check_winner(board_matrix):
    """
    Game won.
    :param board_matrix:Board config
    :return:True or False
    """
    is_won = False

    for sequence in board_matrix:
        pass

    sequence = []
    for column_index in range(len(board_matrix)):
        for row_index in range(len(board_matrix)):
            sequence.append(board_matrix[row_index][column_index])


    sequence = []
    for index in range(len(board_matrix)):
        sequence.append(board_matrix[index][index])


    sequence = []
    for index in range(len(board_matrix)):
        first_index = index
        second_index = len(board_matrix) - index - 1
        sequence.append(board_matrix[first_index][second_index])

    return False

def check_status(board_matrix):
    """
    Won or it s over.
    :param board_matrix: Board config
    :return:True or False
    """
    is_won = check_winner(board_matrix)

    if is_won:
        is_over = True
    else:
        is_over = False

        for row in board_matrix:
            if None in row:
                is_over = False
                break

    return is_won, is_over