"""Representera spelaren med en klass."""

class Player:
    """Klass som representerar spelaren."""
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
        """Kontrollera om en position är giltig att flytta sig till.

        Args:
            x (int): horisontell position.
            y (int): vertikal position.
            grid (Grid): Instans av Grid som representerar kartan.

        Returns:
            _type_: _description_
        """
        #DONE: returnera True om det inte står något i vägen
        # Spaden skulle kunna göra att spelaren kan hamna utanför kartan, behöver kolla det.
        if 0 <= self.pos_x+x < grid.width and 0 <= self.pos_y+y < grid.height:
            # DONE: C. Man ska inte kunna gå igenom väggar.
            if grid.get(self.pos_x+x, self.pos_y+y) != grid.wall:
                return True
        return False
