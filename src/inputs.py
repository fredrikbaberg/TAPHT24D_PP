def handle_input(command):
    """ Reagera på indata. Antar att command är i lowercase (casefold)"""
    # Rörelser.
    if command in ["w", "a", "s", "d"]:
        pass
    
    if command == "i":
        pass
    pass


def move(move_x, move_y, grid, player):
    """ Försök flytta spelaren. """
    # Kolla om det finns ett item.
    maybe_item = grid.get(player.pos_x + 1, player.pos_y)
    # Flytta spelaren.
    player.move(move_x, move_y)
    # Hantera item.
