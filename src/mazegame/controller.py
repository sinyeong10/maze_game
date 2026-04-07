#!/usr/bin/env python
# coding=utf-8
from mazegame.utils import GameLost, GameWon, GameOverNotificationComplete
from . import view
from .model import MazeModel
from .maze_model import generate_maze

def game_loop(game=MazeModel()):
    while True:
        try:
            view.draw_board(game)

            #@todo keyboard, click 라이브러리 써서 이벤트로 처리하기
            result = input("a, w, s, d 키를 눌러보세요. (종료: q)").strip()
            if result == "a":
                game.move_player(0, -1)
            elif result == "w":
                game.move_player(-1,0)
            elif result == "s":
                game.move_player(1,0)
            elif result == "d":
                game.move_player(0, 1)
            elif result == "q":
                print("종료합니다.")
                break
            else:
                continue
        except GameLost:
            game.game_lost = True
        except GameWon:
            game.game_won = True
        except GameOverNotificationComplete:
            break

def map_size():
    while True:
        try:
            #@todo click, args를 활용하여 문자열이 아니라 인자를 받는 식으로 처리
            result = list(map(int, input("x y인 미로 공간을 정의해주세요 : ").split()))
            if len(result) == 1:
                x = y = result[0]
            elif len(result) == 2:
                x, y = result[0], result[1]
            if x >= 10 and y >= 10:
                break
            else:
                print(f"x : {x}, y : {y}로 입력하셨지만 각각의 값이 10이상이여야 합니다.")
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except:
            print("형식이 맞지 않습니다. ex) 2 2")
    return x, y

def make_map(game):
    try:
        #@todo 전략 패턴 사용하여 미로 생성 알고리즘을 동적으로 처리하기
        game.set_generator(generate_maze)
    except:
        raise ValueError("maze 생성 함수가 잘못됨")
    x, y = map_size()
    game.generate_maze(x,y)

def run(game=MazeModel()):
    GameClass = game.__class__
    try:
        make_map(game)

        while True:
            game_loop(game=game)

            if not view.prompt_play_again():
                break
            game = GameClass()

            make_map(game)
    except KeyboardInterrupt:
        return view.say_goodbye()
    return view.say_goodbye()