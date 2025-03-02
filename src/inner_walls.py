"""Enhetstester för skapande av inre väggar."""

import random


def get_coordinates_for_randomized_wall(width, height, length_of_walls):
    """Returnerar en lista med koordinater där väggar ska finnas.
    Utgår från att ytter väggar redan finns, räcker därför att veta bredd och höjd."""
    wall_lengths = [] # Kommer innehålla: övre, nedre, vänstra, högra väggens längd.
    for side in range(0, 3):
        # Se till att längen inte sticker utanför området
        if side in [0, 1]:
            end = min(length_of_walls-sum(wall_lengths), height-2)
        else:
            end = min(length_of_walls-sum(wall_lengths), width-2)
        wall_lengths.append(random.randint(0, end))
    wall_lengths.append(min(length_of_walls-sum(wall_lengths), width-2))
    walls = []
    # Övre vägg - måste kolla att argument för randint ligger inom intervallet.
    column = random.randint(2, width-2) if (width-2-2) > 0 else 1
    for row in range(1, wall_lengths[0]+1):
        walls.append([column, row])
    # Nedre vägg - måste kolla att argument för randint ligger inom intervallet.
    column = random.randint(2, width-2) if (width-2-2) > 0 else 1
    for row in range(1, wall_lengths[1]+1):
        walls.append([column, height-row-1])
    # Vänster vägg - måste kolla att argument för randint ligger inom intervallet.
    row = random.randint(2, height-2) if (height-2-2) > 0 else 1
    for column in range(1, wall_lengths[2]+1):
        walls.append([column, row])
    # Höger vägg - måste kolla att argument för randint ligger inom intervallet.
    row = random.randint(2, height-2) if (height-2-2) > 0 else 1
    for column in range(1, wall_lengths[3]+1):
        walls.append([width-column-1, row])
    return walls
