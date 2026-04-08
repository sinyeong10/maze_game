# 시퀀스 차트 (Sequence Diagrams)
이 문서는 사용자의 입력부터 미로 생성, 그리고 이동 로직이 MVC 패턴과 전략 패턴을 통해 어떻게 흘러가는지 정의합니다.

# 1. 게임 초기화 및 미로 생성 흐름
사용자가 크기를 입력하고 알고리즘을 선택했을 때, 전략 패턴이 적용되어 미로가 생성되는 과정입니다.
<img width="1564" height="1230" alt="image" src="https://github.com/user-attachments/assets/6e0428b4-3040-4e37-ae0d-9a1b8ddec8c3" />

```
sequenceDiagram
    autonumber
    participant U as User
    participant C as controller (function)
    participant M as MazeModel
    participant G as generate_maze (function)
    participant V as view (function)

    %% ======================
    %% 게임 시작
    %% ======================
    U->>C: 게임 실행

    C->>C: make_map(game)

    %% ======================
    %% generator 설정 (고정)
    %% ======================
    Note over C: generate_maze 함수 고정 설정
    C->>M: set_generator(generate_maze)

    %% ======================
    %% 맵 크기 입력
    %% ======================
    C->>U: "x y 입력 요청"
    U-->>C: 크기 입력 (x, y)

    %% ======================
    %% 미로 생성
    %% ======================
    C->>M: generate_maze(x, y)

    M->>G: generator(width, height)
    Note right of G: 미로 생성 알고리즘 실행

    G-->>M: map, start_pos, exit_pos 반환

    %% ======================
    %% 모델 내부 처리
    %% ======================
    M->>M: cur_pos 설정 (start_pos)
    M->>M: 시작 위치 "*" 표시
    M->>M: 출구 위치 "@" 표시

    %% ======================
    %% 화면 출력
    %% ======================
    C->>V: draw_board(game)
    V-->>U: 미로 출력
```

# 2. 사용자 이동 및 승리 판정 흐름
사용자가 방향키를 입력했을 때 MVC 데이터 흐름과 **비즈니스 규칙(벽 충돌)**이 처리되는 과정입니다.
<img width="712" height="1225" alt="image" src="https://github.com/user-attachments/assets/f27ae4f8-aa31-4e2a-b399-6079c2b2a4b0" />


```
sequenceDiagram
    autonumber
    participant U as User
    participant C as controller (game_loop)
    participant M as MazeModel
    participant V as view

    %% ======================
    %% 사용자 입력
    %% ======================
    U->>C: 키 입력 (w, a, s, d)

    C->>C: 입력값 → (dx, dy) 변환

    %% ======================
    %% 이동 요청
    %% ======================
    C->>M: move_player(dx, dy)

    M->>M: is_valid_move(x, y)

    alt 이동 가능 (벽 아님, 범위 내)
        M->>M: remake_map(x, y)
        M->>M: cur_pos 업데이트

        alt 출구 도달
            M-->>C: GameWon 예외 발생
        end

    else 이동 불가 (# 벽 or 범위 밖)
        M-->>C: 아무 동작 없음 (무시)
    end

    %% ======================
    %% 예외 처리
    %% ======================
    alt GameWon 발생
        C->>C: game.game_won = True
    end

    %% ======================
    %% 화면 출력
    %% ======================
    C->>V: draw_board(game)

    V->>V: print_map(map)

    alt game_won == True
        V->>U: "Your Win!!" 출력
        V-->>C: GameOverNotificationComplete 예외 발생
    else 계속 진행
        V-->>U: 현재 맵 출력
    end
```