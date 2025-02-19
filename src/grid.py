import random

class Grid:
    """Representerar spelplanen. Du kan ändra standardstorleken och tecknen för olika rutor. """
    # Storleken sätts i konstruktor, för att enklare kunna testa olika storlekar.
    empty = "."  # Tecken för en tom ruta
    wall = "■"   # Tecken för en ogenomtränglig vägg

    def __init__(self, width=36, height=12):
        """Skapa ett objekt av klassen Grid"""
        self.width = width
        self.height = height
        # Spelplanen lagras i en lista av listor. Vi använder "list comprehension" för att sätta tecknet för "empty" på varje plats på spelplanen.
        self.data = [[self.empty for y in range(self.width)] for z in range(
            self.height)]

    def get(self, x, y):
        """Hämta det som finns på en viss position"""
        return self.data[y][x]

    def set(self, x, y, value):
        """Ändra vad som finns på en viss position"""
        self.data[y][x] = value

    def set_player(self, player):
        self.player = player

    def clear(self, x, y):
        """Ta bort item från position"""
        self.set(x, y, self.empty)

    def __str__(self):
        """Gör så att vi kan skriva ut spelplanen med print(grid)"""
        xs = ""
        for y in range(len(self.data)):
            row = self.data[y]
            for x in range(len(row)):
                if x == self.player.pos_x and y == self.player.pos_y:
                    xs += "@"
                else:
                    xs += str(row[x])
            xs += "\n"
        return xs


    def make_walls(self):
        """Skapa väggar runt hela spelplanen"""
        for i in range(self.height):
            self.set(0, i, self.wall)
            self.set(self.width - 1, i, self.wall)

        for j in range(1, self.width - 1):
            self.set(j, 0, self.wall)
            self.set(j, self.height - 1, self.wall)

        # TODO: H. Använd for-loopar för at skapa flera, sammanhängande väggar på kartan. Se till att det inte skapas några rum som man inte kan komma in i.
        for col in range(3, self.width, int(self.width/3)):
            for row in range(self.height-4, self.height-1):
                self.set(col, row, self.wall)

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
        """ Returnerar koordinater för en tom runta nära centrum."""
        # Rör sig runt mittpunkten för att hitta en lämplig startpunkt.
        position = [int(self.width/2), int(self.height/2)]
        # Första 9 kombinationer av startpositioner.
        offsets = []
        for row in [0, 1, -1]:
            for col in [0, 1, -1]:
                offsets.append([row,col])
        add_coordinates = lambda x, y: [x[0]+y[0], x[1]+y[1]]
        for offset in offsets:
            test_position = add_coordinates(position, offset)
            if self.is_empty(test_position[0], test_position[1]):
                return test_position
        raise Exception("Kunde inte hitta en kombination som fungerar.")
    