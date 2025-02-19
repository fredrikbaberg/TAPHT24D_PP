from .grid import Grid
from .player import Player
from . import pickups
from .printouts import print_inventory, print_status



score = 0
inventory = []

g = Grid()
# DONE: A. Spelaren ska börja nära mitten av rummet.
empty_center_position = g.get_empty_near_center()
player = Player(empty_center_position[0], empty_center_position[1])
g.set_player(player)
g.make_walls()
pickups.randomize(g)



command = "a"
# Loopa tills användaren trycker Q eller X.
while not command.casefold() in ["q", "x"]:
    print_status(g, score)

    command = input("Use WASD to move, i for inventory, Q/X to quit. ")
    command = command.casefold()[:1]

    def move_on_input(dx, dy):
        global score
        maybe_item = g.get(player.pos_x + dx, player.pos_y + dy)
        player.move(dx, dy)

        # DONE: G. The floor is lava - för varje steg man går ska man tappa 1 poäng.
        score -= 1

        if isinstance(maybe_item, pickups.Item):
            # we found something
            # DONE: E. Inventory - alla saker som man plockar upp ska sparas i en lista.
            inventory.append(maybe_item)
            
            score += maybe_item.value
            print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
            g.clear(player.pos_x, player.pos_y)

        # TODO: L. Bördig jord - efter varje 25:e drag skapas en ny frukt/grönsak någonstans på kartan.

    # DONE: B. Förflyttning i alla 4 riktningar (WASD)
    # DONE: C. Man ska inte kunna gå igenom väggar.
    # TODO: N. Jump - om man skriver ett "J" innan något av "WASD", ska spelaren hoppa över en ruta. Man förflyttar sig alltså två steg, men kan förstås bara plocka upp eller interagera med saker där man landar. Hoppar man in i en vägg blir det samma effekt som om man hade gått ett steg på vanligt sätt.
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
