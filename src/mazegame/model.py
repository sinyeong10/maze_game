#!/usr/bin/env python
# coding=utf-8
from .utils import GameLost, GameWon

class MazeModel:
    def __init__(self):       
        self.map = None
        self.player_pos = None
        self.generator = None
        
        self.start_pos = None
        self.cur_pos = None
        self.exit_pos = None

        self.game_lost = False
        self.game_won = False

    def set_generator(self, generator):
        self.generator = generator

    def generate_maze(self, width, height):
        self.map, self.start_pos, self.exit_pos = self.generator(width, height)
        self.cur_pos = self.start_pos
        base_x, base_y = self.cur_pos
        self.map[base_x][base_y] = "*"
        target_x, target_y = self.exit_pos
        self.map[target_x][target_y] = "@"

    def is_win(self):
        raise GameWon()

    def move_player(self, x, y):
        base_x, base_y = self.cur_pos
        if self.is_valid_move(base_x+x,base_y+y):
            self.remake_map(base_x+x,base_y+y)
            if self.cur_pos == self.exit_pos:
                self.is_win()
    
    def is_valid_move(self, x, y):
        if not (0 <= x < len(self.map) and 0 <= y < len(self.map[0])):
            return False
        if self.map[x][y] == "#":
            return False
        return True

    def remake_map(self, x, y):
        base_x, base_y = self.cur_pos
        self.map[base_x][base_y] = " "
        self.map[x][y] = "*"
        self.cur_pos = (x, y)

    def is_win(self):
        raise GameWon()