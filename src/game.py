"""Startpunkt för spelet."""
from . import pickups
from .count_pickups import count_pickups
from .exit import Exit
from .find_empty_near_center import get_empty_near_center
from .grid import Grid
from .player import Player
from .printouts import print_inventory, print_result, print_status



score = 0 # pylint: disable=invalid-name
inventory = []

g = Grid(width=36, height=12)
# DONE: A. Spelaren ska börja nära mitten av rummet.
empty_center_position = get_empty_near_center(g)
player = Player(empty_center_position[0], empty_center_position[1])
g.set_player(player)
g.make_walls()
g.make_inner_walls(10) # Skapa inre väggar.
pickups.randomize(g, pickups.pickups)
pickups.randomize(g, [Exit()]) # Lägg till en utgång.


turn_counter = 0 # Håll koll på vilket drag spelaren är på. #pylint: disable=invalid-name
grace_counter = 0 # Håll koll på när det är dags att lägga till nytt Item. #pylint: disable=invalid-name
command = "a" # pylint: disable=invalid-name
# Loopa tills användaren trycker Q eller X.
while not command.casefold() in ["q", "x"]:
    print_inventory(inventory)
    print_status(g, score)

    command = input("Use WASD to move, i for inventory, Q/X to quit. ")
    command = command.casefold()[:1]

    # DONE: B. Förflyttning i alla 4 riktningar (WASD)
    # DONE: C. Man ska inte kunna gå igenom väggar.
    # TODO: N. Jump - om man skriver ett "J" innan något av "WASD", ska spelaren hoppa över en ruta. Man förflyttar sig alltså två steg, men kan förstås bara plocka upp eller interagera med saker där man landar. Hoppar man in i en vägg blir det samma effekt som om man hade gått ett steg på vanligt sätt.
    # Tanke: Behöver dels kolla om det finns ett "J", dels se till att båda rutor är möjliga.
    # Hantera rörelse.
    directions = {"w": (0, -1), "a": (-1,0), "s": (0,1), "d": (1,0)}
    if command in directions:
        dx = directions[command][0]
        dy = directions[command][1]
        pos_x = player.pos_x
        pos_y = player.pos_y
        # Kontrollera om spelaren försöker gå in i en vägg.
        if (0 <= pos_x+dx < g.width and 0 <= pos_y+dy < g.height) and (g.get(player.pos_x+dx, player.pos_y+dy) == g.wall):
            # DONE: J. Spade
            # Kontrollera om det finns någon spade.
            shovels = [e for e in inventory if e.name=='shovel']
            if len(shovels) > 0:
                g.clear(player.pos_x+dx, player.pos_y+dy)
                inventory.remove(shovels[0])
        elif player.can_move(dx, dy, g):
            maybe_item = g.get(player.pos_x+dx, player.pos_y+dy)
            player.move(dx, dy)
            # DONE: G. The floor is lava
            # DONE: Grace period
            if grace_counter > 0:
                grace_counter -= 1
            else:
                score -= 1
            # Item kan läggas i inventory och eventuellt ge poäng.
            if isinstance(maybe_item, pickups.Item):
                # we found something
                # DONE: E. Inventory
                inventory.append(maybe_item)
                score += maybe_item.value
                print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
                g.clear(player.pos_x, player.pos_y)
                grace_counter = 5 # Grace period
            # DONE: M. Exit
            if isinstance(maybe_item, Exit):
                if count_pickups(g, pickups.Item, only_original=True) == 0:
                    print_result(score=score, steps=turn_counter)
                    break
            turn_counter += 1
            # DONE: L. Bördig jord
            if turn_counter % 25 == 0:
                pickups.randomize(g, [pickups.get_random_extra_item()])

    # DONE: F. Nytt kommando: "i", skriver ut innehållet i spelarens inventory.
    elif command == "i":
        print_inventory(inventory)

# Hit kommer vi när while-loopen slutar
print("Thank you for playing!")
