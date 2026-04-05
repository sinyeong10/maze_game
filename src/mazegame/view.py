#!/usr/bin/env python
# coding=utf-8
import os
import sys
from .utils import GameOverNotificationComplete

def draw_board(game):
    print_map(game.map)
    if game.game_won:
        print("Your Win!!")

    if game.game_lost or game.game_won:
        raise GameOverNotificationComplete

def print_clear():
    #@todo 가시성을 위해 clear말고 "\033[F" 사용하여 처리
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

def print_map(map):
    print_clear()
    for row in map:
        print(*row)

def say_goodbye():
    print_clear()
    print("Game end")

def prompt_play_again():
    while True:
        result = input("retry Game? : 'n' or 'y'")
        if result == "y":
            print_clear()
            return True
        elif result == "n":
            print_clear()
            return False
        else:
            print("need 'n' or 'y'")
