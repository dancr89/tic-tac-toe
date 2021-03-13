def get_current_player(step):
    """

    Current player turn
    :param step: integer about the current iteration
    :return:(player_name, player_sign)
    """

    if step % 2 == 0:
        name = 'Player1'
        sign = 'x'
    else:
        name = 'Player2'
        sign = 'o'

    return name, sign