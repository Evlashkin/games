"""
project 1

Tic Tak Toe
"""
import time


def change_xo():
    global first_player_f
    first_player_f = ''
    global second_player_f
    second_player_f = ''
    while first_player_f != 'X' or first_player_f != 'O':
        first_player_f = input(f'{first_player} выбирает за кого будет играть (X или O): ')
        if first_player_f == 'X':
            print(f'{second_player} Вы играете за "O"')
            second_player_f = 'O'
            break
        elif first_player_f == 'O':
            print(f'{second_player} Вы играете за "X"')
            second_player_f = 'X'
            break
        else:
            print('Введеное значение не соответствует допустимому значению')
    return first_player_f, second_player_f


def turn_controller(num_player, cell_nums, ff, d):
    player_turn = int(input(f'Ходит {num_player}. Введите номер ячейки: '))
    while player_turn not in cell_nums:
        print('Введено некорректное значение. Виберете значение из этго списка:', cell_nums)
        player_turn = int(input(f'Ходит {num_player}. Введите номер ячейки: '))
    cell_nums.remove(player_turn)
    d[player_turn] = ff
    field = "|     |     |     |\n" \
            f"|  {d[7]}  |  {d[8]}  |  {d[9]}  |\n" \
            "|     |     |     |\n" \
            "|-----|-----|-----|\n" \
            "|     |     |     |\n" \
            f"|  {d[4]}  |  {d[5]}  |  {d[6]}  |\n" \
            "|     |     |     |\n" \
            "|-----|-----|-----|\n" \
            "|     |     |     |\n" \
            f"|  {d[1]}  |  {d[2]}  |  {d[3]}  |\n" \
            "|     |     |     |"
    print('\n' * 100)
    print(field)
    if d[1] == d[2] == d[3] == ff or d[4] == d[5] == d[6] == ff or d[7] == d[8] == d[9] == ff or \
            d[1] == d[4] == d[7] == ff or d[2] == d[5] == d[8] == ff or d[3] == d[6] == d[9] == ff or \
            d[1] == d[5] == d[9] == ff or d[3] == d[5] == d[7] == ff:
        print(f'{num_player} победил! Поздравляем  с победой!')
        return 'finish'


def playing_field(ff, sf):
    d = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

    field = "|     |     |     |\n" \
            f"|  {d[7]}  |  {d[8]}  |  {d[9]}  |\n" \
            "|     |     |     |\n" \
            "|-----|-----|-----|\n" \
            "|     |     |     |\n" \
            f"|  {d[4]}  |  {d[5]}  |  {d[6]}  |\n" \
            "|     |     |     |\n" \
            "|-----|-----|-----|\n" \
            "|     |     |     |\n" \
            f"|  {d[1]}  |  {d[2]}  |  {d[3]}  |\n" \
            "|     |     |     |"
    d = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
    print('\n' * 100)
    print("Уважеемые игроки перед вами игровое поле, чтобы заполнить желаемую ячейку крестиком или ноликом (X, O)\n"
          "необходимо ввести номер ячейки. Желаю удачи и пусть победит сильнейший!\n" + field)
    cell_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while len(cell_nums) >= 1:
        f_result = turn_controller(first_player, cell_nums, ff, d)
        if f_result == 'finish':
            break
        if len(cell_nums) == 0:
            continue
        s_result = turn_controller(second_player, cell_nums, sf, d)
        if s_result == 'finish':
            break
    else:
        print("Игра окончена. Ничья")


print('Welcome in Tic Tak Toe')

first_player = input('What is first player name? : ')
second_player = input('What is second player name? : ')

one_more = ''
while one_more == '':
    first_player_f, second_player_f = change_xo()
    time.sleep(3)
    playing_field(first_player_f, second_player_f)
    one_more = input("Нажмите Enter, если хотите сыграть еще раз\nЧтобы выйти любую другую клавишу, а затем Enter")
