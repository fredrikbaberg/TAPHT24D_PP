class Player:
    marker = "@"

    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

    # Flyttar spelaren. "dx" och "dy" är skillnaden
    def move(self, dx, dy):
        """Flyttar spelaren.\n
        dx = horisontell förflyttning, från vänster till höger\n
        dy = vertikal förflyttning, uppifrån och ned"""
        self.pos_x += dx
        self.pos_y += dy

    def can_move(self, x, y, grid):
        #DONE: returnera True om det inte står något i vägen
        # Spaden gör att spelaren kan hamna utanför planen, kolla gränserna.
        if 0 <= self.pos_x+x < grid.width and 0 <= self.pos_y+y < grid.height:
            # Kollar endast efter väggar.
            if grid.get(self.pos_x+x, self.pos_y+y) != grid.wall:
                return True
        return False



