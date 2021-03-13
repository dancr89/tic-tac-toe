board_matrix = [
    [None, None, None],
    [None, None, None],
    [None, None, None],
]


def get_options(board):
    """

    checks available options
    :param board:bord configuration
    :return:array of available options
    """
    options = []

    for row_index, row_data in enumerate(board):
        for column_index, column_data in enumerate(row_data):
            if column_data is None:
                options.append(row_index * len(board) + column_index + 1)

    return options

def show(board):
    """

    :param board: bord config
    :return:
    """

    print('+---+----+---+')

    for row_index, row_data in enumerate(board):
        row_signs = []
        for column_index, column_data in enumerate(row_data):
            if column_data is None:
                row_signs.append(row_index * len(board) + column_index + 1)
            else:
                row_signs.append(column_data)

        row_signs = str(row_signs)
        row_signs = row_signs.replace('[', '|').replace(']', '|').replace(',', '|').replace("'", '|')
        print(row_signs)
        print('+---+---+---+')

def set_choice(board, choice, sign):
    new_board = board.copu()

    for row_index, row_data in enumerate(board):
        for column_index, column_data in enumerate(row_data):
            if (row_index * len(board) + column_index + 1) == choice:
                new_board[row_index][column_index] = sign

    return new_board