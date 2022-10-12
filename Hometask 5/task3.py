# 3. Создайте программу для игры в "Крестики-нолики". Поле 3x3. Игрок - игрок, без бота.




board = list(map(str, range(1, 10)))


def play_board():
    print('-'*20)
    for i in range(3):
        for j in range(3):
            print(f'{board[j+i*3]:^5}', end=' ')
        print(f"\n{'-'*20}")
    print()
    

    

def place_sign(sign):
    global board
    while True:
        request = input(f'Enter position from 1 to 9 for {sign}: ')
        if request.isdigit() and int(request) in range(1, 10):
            request = int(request)
            pos = board[request-1]
            if pos not in (chr(10060), chr(11093)):
                board[request-1] = chr(10060) if sign == "X" else chr(11093)
                break
            else:
                print(f'Already occupied {chr(129335)}')
        else:
            print(f'incorrect value {chr(128581)}')


def check_win():
    win_comb = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    win = [board[x[0]]
           for x in win_comb if board[x[0]] == board[x[1]] == board[x[2]]]
    return win[0] if win else win


def game():
    play_board()
    counter = 0
    while True:
        place_sign('0') if counter % 2 else place_sign('X')
        play_board()
        if counter > 3:
            if check_win():
                print(f"{check_win()} Win! {chr(129395)}")
                break
        if counter == 8:
            print(f'Draw {chr(129309)} . Would you like replay?')
            break
        counter += 1


game()
