"""Räkna antal pickups av en viss typ på kartan."""

def count_pickups(grid, instance_type, only_original=False):
    """ Räkna antal pickups av en viss sort på kartan.
    
    Kan sätta only_orignal för att endast ta med ursprungliga pickups."""
    number_pickups = 0
    for col in range(0, grid.width):
        for row in range(0, grid.height):
            maybe_item = grid.get(col, row)
            if isinstance(maybe_item, instance_type):
                if only_original:
                    number_pickups +=1 if maybe_item.original else 0
                else:
                    number_pickups += 1
    return number_pickups
