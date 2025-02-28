"""Klass som representerar spelplanen."""
import random

# Liten hjälpfunktion för att lägga ihop två koordinater.
add_coordinates = lambda x, y: [x[0]+y[0], x[1]+y[1]] #pylint: disable=unnecessary-lambda-assignment


class Grid:
    """Representerar spelplanen. Du kan ändra standardstorleken och tecknen för olika rutor. """
    # Storleken sätts i konstruktor, för att enklare kunna testa olika storlekar.
    empty = "."  # Tecken för en tom ruta
    wall = "■"   # Tecken för en ogenomtränglig vägg

    def __init__(self, width=36, height=12):
        """Skapa ett objekt av klassen Grid"""
        self.width = width
        self.height = height
        # Spelplanen lagras i en lista av listor. Vi använder\n
        # "list comprehension" för att sätta tecknet för "empty" på varje plats på spelplanen.
        self.data = [[self.empty for y in range(self.width)] for z in range(
            self.height)]
        self.player = None # Pylint klagar om player inte definieras i konstruktorn.

    def get(self, x, y):
        """Hämta det som finns på en viss position"""
        return self.data[y][x]

    def set(self, x, y, value):
        """Ändra vad som finns på en viss position"""
        self.data[y][x] = value

    def set_player(self, player):
        """Sätt värde på player"""
        self.player = player

    def clear(self, x, y):
        """Ta bort item från position"""
        self.set(x, y, self.empty)

    def __str__(self):
        """Gör så att vi kan skriva ut spelplanen med print(grid)"""
        xs = ""
         # pylint: disable=consider-using-enumerate
        for y in range(len(self.data)):
            row = self.data[y]
            for x in range(len(row)):
                # Kollar om player har något värde först, för att undvika AttributeError.
                if self.player is not None and x == self.player.pos_x and y == self.player.pos_y:
                    xs += "@"
                else:
                    xs += str(row[x])
            xs += "\n"
        # pylint: enable=consider-using-enumerate
        return xs


    def make_walls(self):
        """Skapa väggar runt hela spelplanen"""
        for i in range(self.height):
            self.set(0, i, self.wall)
            self.set(self.width - 1, i, self.wall)

        for j in range(1, self.width - 1):
            self.set(j, 0, self.wall)
            self.set(j, self.height - 1, self.wall)

    # TODO: H. Använd for-loopar för att skapa flera, sammanhängande väggar på kartan.
    # Se till att det inte skapas några rum som man inte kan komma in i. Gör detta i filen grid.py.
    def make_inner_walls(self, length_of_walls=10):
        """Skapa inre väggar.

        Kommer slumpa en vägg per sida. Summan av väggarnas längder ges som argument, 
        men varje väggs längd slumpas. Obs: Om två väggar överlappar blir längden kortare.
        """
        wall_lengths = [] # Kommer innehålla: övre, nedre, vänstra, högra väggens längd.
        for _ in range(0, 3):
            wall_lengths.append(random.randint(0, length_of_walls-sum(wall_lengths)))
        wall_lengths.append(length_of_walls-sum(wall_lengths))
        # För vänster och höger sida skulle slicing kunna användas direkt på grid.data, förutsatt
        # att den förblir publik. Håller mig till set för att ha samma struktur på alla sidor.
        # Övre vägg
        column = random.randint(2, self.width-2)
        for row in range(1, wall_lengths[0]+1):
            self.set(column, row, self.wall)
        # Nedre vägg
        column = random.randint(2, self.width-2)
        for row in range(1, wall_lengths[1]+1):
            self.set(column, self.height-row-1, self.wall)
        # Vänster vägg.
        row = random.randint(2, self.height-2)
        for column in range(1, wall_lengths[2]+1):
            self.set(column, row, self.wall)
        # Höger vägg
        row = random.randint(2, self.height-2)
        for column in range(1, wall_lengths[3]+1):
            self.set(self.width-column-1, row, self.wall)
        # # Nästade for-loopar kan ge återkommande mönster men inte mycket variation.
        # # for col in range(3, self.width, int(self.width/3)):
        # #     for row in range(self.height-4, self.height-1):
        # #         self.set(col, row, self.wall)

    # Används i filen pickups.py
    def get_random_x(self):
        """Slumpa en x-position på spelplanen"""
        return random.randint(0, self.width-1)

    def get_random_y(self):
        """Slumpa en y-position på spelplanen"""
        return random.randint(0, self.height-1)


    def is_empty(self, x, y):
        """Returnerar True om det inte finns något på aktuell ruta"""
        return self.get(x, y) == self.empty


    def get_empty_near_center(self):
        """Returnerar koordinater för en tom ruta nära centrum.
        Lyfter Exception om ingen av de första 9 rutorna fungerar.
        """
        # Ungefärlig mittpunkt.
        position = [int(self.width/2), int(self.height/2)]
        # Ta fram första 9 kombinationerna av startpositioner.
        offsets = []
        for row in [0, 1, -1]:
            for col in [0, 1, -1]:
                offsets.append([row,col])
        for offset in offsets:
            test_position = add_coordinates(position, offset)
            if self.is_empty(test_position[0], test_position[1]):
                return test_position
        # Hittade inget mer specifikt felmeddelande som passar, så använder Exception.
        raise Exception("Kunde inte hitta en kombination som fungerar.") #pylint: disable=broad-exception-raised

def check_no_isolated_rooms(grid):
    """Kolla att det går att nå alla rum.

    Använder bredd-först-sökning."""
    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    visited = []
    start = None
    # Hitta en punkt att börja från.
    for col in range(0, grid.width):
        for row in range(0, grid.height):
            if grid.is_empty(col, row):
                start = (row, col)
                break
        if start:
            break
    # Lägg till startpunkten och alla grannar i en kö för att kollas.
    queue = [start]
    while queue:
        to_check = queue.pop() # Hämta en punkt som ska besökas.
        visited.append(to_check)
        for direction in directions: # Försök lägga till grannar.
            new = tuple(add_coordinates(to_check, direction))
            # Kontrollera att koordinaten går att nå.
            if 0 <= new[0] < grid.width and 0 <= new[1] < grid.height:
                if grid.is_empty(new[0], new[1]) and new not in visited:
                    queue.append(new)
    # Skapa en lista med alla koordinater som borde kunna besökas
    should_have_been_visited = []
    for col in range(0, grid.width):
        for row in range(0, grid.height):
            if grid.is_empty(col, row):
                should_have_been_visited.append((col, row))
    # Ta bort kopior genom att göra om till set och tillbaka till tuple.
    visited = tuple(set(visited))
    should_have_been_visited = tuple(set(should_have_been_visited))
    return should_have_been_visited == visited
