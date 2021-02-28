
class Board:
    def __init__(self):
        self.spot = self.generate_spot()

    def generate_spot(self):
        return [None, None, None, None, None]
