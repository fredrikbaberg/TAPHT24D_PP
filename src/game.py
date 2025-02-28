"""Startpunkt för spelet."""
import random
from .grid import Grid
from .player import Player
from . import pickups
from .printouts import print_inventory, print_status



score = 0 # pylint: disable=invalid-name
inventory = []

g = Grid(width=36, height=12)
# DONE: A. Spelaren ska börja nära mitten av rummet.
empty_center_position = g.get_empty_near_center()
player = Player(empty_center_position[0], empty_center_position[1])
g.set_player(player)
g.make_walls()
pickups.randomize(g, pickups.pickups)


turn_counter = 0 # Håll koll på vilket drag spelaren är på. #pylint: disable=invalid-name
command = "a" # pylint: disable=invalid-name
# Loopa tills användaren trycker Q eller X.
while not command.casefold() in ["q", "x"]:
    print_status(g, score)

    command = input("Use WASD to move, i for inventory, Q/X to quit. ")
    command = command.casefold()[:1]

    # Placerar funktionen här eftersom den inte kommer behövas på fler platser.
    def move_on_input(dx, dy):
        """Move dx, dy on grid, check for item and updates score.
           Assumes movement is valid.

        Args:
            dx (_type_): horizontal movement
            dy (_type_): vertical movement
        """
        # Låt score vara global för att dra bort/lägga till poäng.
        global score #pylint: disable=global-statement
        maybe_item = g.get(player.pos_x + dx, player.pos_y + dy)
        player.move(dx, dy)

        # DONE: G. The floor is lava - för varje steg man går ska man tappa 1 poäng.
        # Avsiktligt val: alltid -1 poäng, även om spelaren försöker gå in i en vägg.
        score -= 1

        if isinstance(maybe_item, pickups.Item):
            # we found something
            # DONE: E. Inventory - alla saker som man plockar upp ska sparas i en lista.
            inventory.append(maybe_item)

            score += maybe_item.value
            print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
            g.clear(player.pos_x, player.pos_y)

        # DONE: L. Bördig jord - efter varje 25:e drag skapas en ny frukt/grönsak någonstans på kartan.
        global turn_counter #pylint: disable=global-statement
        turn_counter += 1
        if turn_counter % 5 == 0:
            pickups.randomize(g, random.sample(pickups.pickups, 1))

    # DONE: B. Förflyttning i alla 4 riktningar (WASD)
    # DONE: C. Man ska inte kunna gå igenom väggar.
    # TODO: N. Jump - om man skriver ett "J" innan något av "WASD",\n
    # ska spelaren hoppa över en ruta. Man förflyttar sig alltså två steg,\n
    # men kan förstås bara plocka upp eller interagera med saker där man landar.\n
    # Hoppar man in i en vägg blir det samma effekt som om man hade gått ett steg på vanligt sätt.
    # Tanke: Behöver dels kolla om det finns ett "J", dels se till att båda rutor är möjliga.
    if command == "w" and player.can_move(0, -1, g):  # move up
        move_on_input(0, -1)
    elif command == "a" and player.can_move(-1, 0, g):  # move left
        move_on_input(-1, 0)
    elif command == "s" and player.can_move(0, 1, g):  # move down
        move_on_input(0, 1)
    elif command == "d" and player.can_move(1, 0, g):  # move right
        move_on_input(1, 0)
    # DONE: F. Nytt kommando: "i", skriver ut innehållet i spelarens inventory.
    elif command == "i":
        print_inventory(inventory)

# Hit kommer vi när while-loopen slutar
print("Thank you for playing!")
