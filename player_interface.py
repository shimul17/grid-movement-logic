import random
from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]

    def make_move(self):
        move = random.choice(self.moves)
        # গাণিতিক যোগফল বের করে সরাসরি আপডেট
        self.position = (self.position[0] + move[0], self.position[1] + move[1])
        self.path.append(self.position)
        return self.position

    @abstractmethod
    def level_up(self):
        pass

class Pawn(Player):
    def __init__(self):
        super().__init__()
        # Up, Down, Left, Right
        self.moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    def level_up(self):
        # Diagonal movements
        diagonal_moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        self.moves.extend(diagonal_moves)
        # ১. একটি Pawn অবজেক্ট তৈরি করুন
if __name__ == "__main__":
    pawn = Pawn()
    print(f"Initial Position: {pawn.position}")
    
    pawn.make_move()
    print(f"First Move: {pawn.position}")
    
    pawn.make_move()
    print(f"Second Move: {pawn.position}")
    
    print(f"Full Path: {pawn.path}")