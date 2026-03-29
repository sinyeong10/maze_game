# 시퀀스 차트 (Sequence Diagrams)
이 문서는 사용자의 입력부터 미로 생성, 그리고 이동 로직이 MVC 패턴과 전략 패턴을 통해 어떻게 흘러가는지 정의합니다.

# 1. 게임 초기화 및 미로 생성 흐름
사용자가 크기를 입력하고 알고리즘을 선택했을 때, 전략 패턴이 적용되어 미로가 생성되는 과정입니다.
<img width="6425" height="3870" alt="image" src="https://github.com/user-attachments/assets/0eeec55c-a8bd-4d1a-8735-2917fd05cfd2" />

```
sequenceDiagram
    autonumber
    participant U as User
    participant C as MazeController
    participant M as MazeModel
    participant G as MazeGenerator (Strategy)
    participant V as MazeView

    U->>C: 게임 시작 (크기, 알고리즘 선택)
    Note over C: 사용자가 선택한 알고리즘 객체 생성<br/>(예: RecursiveBacktracker)
    
    C->>M: set_generator(generator)
    C->>M: generate_maze(W, H)
    
    M->>G: generate(W, H)
    Note right of G: 미로 생성 알고리즘 실행
    G-->>M: 생성된 Grid 배열 반환
    
    M->>M: 외곽 벽 및 출입구(Start/Exit) 설정
    M-->>C: 생성 완료
    
    C->>V: render(grid, player_pos)
    V-->>U: 미로 화면 출력
```

# 2. 사용자 이동 및 승리 판정 흐름
사용자가 방향키를 입력했을 때 MVC 데이터 흐름과 **비즈니스 규칙(벽 충돌)**이 처리되는 과정입니다.
<img width="4742" height="5020" alt="image" src="https://github.com/user-attachments/assets/41ea8402-31da-48e3-a4d5-de422d348106" />


```
sequenceDiagram
    autonumber
    participant U as User
    participant C as MazeController
    participant M as MazeModel
    participant V as MazeView

    U->>C: 키 입력 (W, A, S, D)
    C->>C: 입력 키를 좌표 변화량(dx, dy)으로 변환
    
    C->>M: move_player(dx, dy)
    
    M->>M: is_valid_move(new_x, new_y) 확인
    alt 이동 가능한 길(0)인 경우
        M->>M: player_pos 업데이트
    else 벽(1)인 경우
        M-->>C: 이동 거부 (좌표 유지)
    end
    
    M->>M: is_win() 체크 (현재 좌표 == Exit 좌표?)
    
    M-->>C: 현재 상태 반환 (진행중 or 승리)
    
    C->>V: render(grid, player_pos)
    
    opt 승리 시
        C->>V: show_message("Congratulations! You Escaped!")
    end
    
    V-->>U: 갱신된 화면 출력
```