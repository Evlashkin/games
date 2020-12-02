"""
DOCSTRING
This is code for Black Jack game

Rules:
Чтобы сыграть в Блэкджек, следует выполнить следующие шаги:

Создать колоду из 52 карт
Перемешать колоду
Спросить у Игрока его ставку
Убедиться, что ставка Игрока не превышает количество доступных у него фишек
Сдать две карты Дилеру и две карты Игроку
Показать только одну карту из двух карт Дилера, вторая карта остается скрытой
Показать обе карты Игрока
Спросить Игрока, хочет ли он взять ещё одну карту, и если да, то дать ему ещё одну карту
Если сумма карт игрока не превышает 21, то спросить его, хочет ли он снова взять ещё одну карту.
Если Игрок говорит "хватит" (т.е., дополнительных карт не нужно), то перейти к картам Дилера. Дилер всегда берёт
дополнительные карты до тех пор, пока сумма его карт не станет больше или равна 17
Определить победителя, и сохранить новое значение balance у Игрока
Спросить Игрока, хочет ли он сыграть снова
"""
from random import shuffle


suits = ['Червы', 'Бубны', 'Крести', 'Пики']
ranks = ['Двойка', 'Тройка', 'Четверка', 'Пятерка', 'Шестерка', 'Семерка', 'Восьмерка', 'Девятка', 'Десятка', 'Валет',
         'Дама', 'Король', 'Туз']
values = {'Двойка': 2, 'Тройка': 3, 'Четверка': 4, 'Пятерка': 5, 'Шестерка': 6, 'Семерка': 7, 'Восьмерка': 8,
          'Девятка': 9, 'Десятка': 10, 'Валет': 10, 'Дама': 10, 'Король': 10, 'Туз': 11}


class Card:
    """
    Класс карты
    """

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank} {self.suit}'


class Deck:

    """
    Класс колоды
    Позволяет:
    1. Создать колоду
    2. Перемешать колоду
    3. Вытянуть из колоды верхнюю карту
    """

    def __init__(self):
        self.all_deck = []
        for suit in suits:
            for rank in ranks:
                card = Card(suit, rank)
                self.all_deck.append(card)

    def shuffle(self):
        shuffle(self.all_deck)

    def pull(self):

        return self.all_deck.pop()

    def __str__(self):
        return ', '.join(str(item) for item in self.all_deck)


class Player:

    def __init__(self, p_name, balance=500):
        self.p_name = p_name
        self.balance = balance

    def __str__(self):
        return f'Имя: {self.p_name}\nБаланс: {self.balance}'

    def rate(self, p_rate):
        """
        :param p_rate: type - int
        :return: print('Ставка сделана! Ваш баланс {}'.format(self.balance))
        """

        while p_rate > self.balance:
            print(f'Ваша ставка превышает Ваш баланс. Ваш баланс {self.balance}')
            while True:
                try:
                    p_rate = int(input('Сделайте ставку: '))
                    break
                except ValueError:
                    print('Неверный формат ввода! Попробуйте еще раз.')
                    continue
        self.balance -= p_rate
        return print('Ставка сделана! Ваш баланс {}'.format(self.balance))

    def add_money(self, p_rate):
        """
        :param p_rate:  type - int
        :return: self.balance
        """
        self.balance += p_rate
        return self.balance


class Hand:

    def __init__(self):
        self.cards_in_hand = []
        self.values_in_hand = 0
        self.count_ace = 0

    def __str__(self):
        return f'на руках {", ".join(str(item) for item in self.cards_in_hand)} равно {self.values_in_hand} очков'

    def add(self, p_deck):
        """
        :param p_deck: Your deck - instance of class Deck
        :return: ', '.join(str(item) for item in self.cards_in_hand)
        """
        card = p_deck.pull()
        self.cards_in_hand.append(card)
        self.values_in_hand += values[card.rank]
        return ', '.join(str(item) for item in self.cards_in_hand)

    def adjust_for_ace(self):
        for card in self.cards_in_hand:
            if values[card.rank] == 11:
                self.count_ace += 1
        return f'Количество тузов в Вашей руке равно {self.count_ace}'


name = input('Как Вас зовут? : ')
player = Player(name)
while player.balance > 0:
    deck = Deck()
    deck.shuffle()
    print(player)
    rate = 0
    while True:
        try:
            rate = int(input('Сделайте ставку : '))
            break
        except ValueError:
            print('Неверный формат ввода! Попробуйте еще раз.')
            continue

    player.rate(rate)
    diller_hand = Hand()
    player_hand = Hand()
    diller_hand.add(deck)
    diller_hand.add(deck)
    print(f'У диллера на руках {diller_hand.cards_in_hand[0]}')
    player_hand.add(deck)
    player_hand.add(deck)
    print(f'У Вас {player_hand}')
    while player_hand.values_in_hand <= 21:
        answer = input('Вы хотите вытянуть еще одну карту? Y/N :')
        if answer.lower() == 'y':
            player_hand.add(deck)
            print(f'Вы имеете {player_hand}')
        elif answer.lower() == 'n':
            print("Ход переходит к диллеру")
            break
        else:
            print('Неверный формат ввода! Попробуйте еще раз. Введите Y или N')

    while diller_hand.values_in_hand < 17:
        diller_hand.add(deck)
    else:
        print(f'У диллера {diller_hand}')
        print(f'У {player.p_name} {player_hand}')
        if player_hand.values_in_hand < diller_hand.values_in_hand <= 21:
            print(f'Дилер победил! {player.p_name} Ваш баланс {player.balance}')
        elif player_hand.values_in_hand > 21 >= diller_hand.values_in_hand:
            print(f'Дилер победил! {player.p_name} Ваш баланс {player.balance}')
        elif player_hand.values_in_hand == diller_hand.values_in_hand <= 21:
            player.add_money(rate)
            print(f'Ничья! {player.p_name} Ваш баланс {player.balance}')
        elif player_hand.values_in_hand > 21 and diller_hand.values_in_hand > 21:
            player.add_money(rate)
            print(f'Ничья! {player.p_name} Ваш баланс {player.balance}')
        elif diller_hand.values_in_hand > 21 >= player_hand.values_in_hand:
            player.add_money(rate * 2)
            print(f'{player.p_name} победил! Ваш баланс {player.balance}')
        else:
            player.add_money(rate * 2)
            print(f'{player.p_name} победил! Ваш баланс {player.balance}')
    one_more_game = input('Хотите сыграть еще раз? Y/N')
    # Сделать цикл while
    while one_more_game.lower() != 'y' and one_more_game.lower() != 'n':
        print('Неверный формат ввода! Попробуйте еще раз. Введите Y или N')
        one_more_game = input('Хотите сыграть еще раз? Y/N :')
        continue
    else:
        if one_more_game.lower() == 'y':
            continue
        else:
            print("Игра окончена")
            break
else:
    print("Игра окончена!\nВы остались без штанов!")
