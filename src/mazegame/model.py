class MazeModel:
    def __init__(self):       
        self.grid = None
        self.player_pos = None
        self.start_pos = None
        self.exit_pos = None
        self.generator = None

    def set_generator(self, generator):
        pass

    def generate_maze(self):
        pass

    def move_player(self, x, y):
        pass

    def is_valid_move(self, x, y):
        pass
    
    def is_win(self):
        pass

