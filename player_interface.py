import random
from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, grid_size=10):
        self.grid_size = grid_size
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]

    def make_move(self):
        if not self.moves:
            return self.position

        move = random.choice(self.moves)
        
        # Calculate potential new coordinates
        new_x = self.position[0] + move[0]
        new_y = self.position[1] + move[1]

        # Boundary Check: Stay within 0 to grid_size-1
        if 0 <= new_x < self.grid_size and 0 <= new_y < self.grid_size:
            self.position = (new_x, new_y)
            self.path.append(self.position)
            return self.position
        else:
            return self.position

    @abstractmethod
    def level_up(self):
        pass

class Pawn(Player):
    def __init__(self, grid_size=10):
        super().__init__(grid_size)
        # Initial moves: Up, Down, Left, Right
        self.moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    def level_up(self):
        diagonal_moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for move in diagonal_moves:
            if move not in self.moves:
                self.moves.append(move)
        print("\n✨ Level Up! Diagonal moves unlocked. ✨")

if __name__ == "__main__":
    pawn = Pawn(grid_size=10)
    print(f"Starting Position: {pawn.position}")

    print("\n--- Initial Movements ---")
    for i in range(5):
        pos = pawn.make_move()
        print(f"Move {i+1}: {pos}")

    pawn.level_up()

    print("\n--- Post Level-Up Movements ---")
    for i in range(5):
        pos = pawn.make_move()
        print(f"Move {i+6}: {pos}")

    print("-" * 30)
    print(f"Final Position: {pawn.position}")
    print(f"Full Path Recorded: {pawn.path}")
    print("-" * 30)
    print("\n--- Searching for Treasure (9, 9) ---")
    while pawn.position != (9, 9):
        pos = pawn.make_move()
        print(f"Current Position: {pos}")
        if len(pawn.path) > 100: 
            print("Pawn is tired! Game Over.")
            break       
    if pawn.position == (9, 9):
        print("\n🎉 Victory! The Pawn reached the target (9, 9)!")
