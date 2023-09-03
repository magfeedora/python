board = list(range(1,10))

def draw(board):
    print("-" * 13)
    for i in range(3):
        print(board[0 + i * 3], board[1 + i * 3], board[2 + i * 3])
        print("-" * 13)

def choose(token):
    check = False
    while not check:
        answer = input("Сделайте свой ход")
        try:
            answer = int(answer)
        except:
            print("Введите число")
            continue
        if(1 <= answer <= 9):
            if(str(board[answer-1]) not in "XO","ХО"):
                board[answer-1] = token
                ckeck = True
            else:
                print("Клетка уже занята")
        else:
            print("Введите число от 1 до 9")

def win(board):
    coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
        return False

def main(board):
    count = 0
    loose = False
    while not loose:
        draw(board)
        if count % 2 == 0:
            choose("X")
        else:
            choose("O")
        count += 1
        if count > 4:
            a = win(board)
            if a:
                print(a, "Выиграл")
                loose = True
                break
        if count == 9:
            print("Ничья")
            break
    draw(board)

main(board)







