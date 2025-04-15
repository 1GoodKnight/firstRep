# def print_football():
#     print('Время игры: два тайма по 45 минут')
#     print('Количество игроков: 11 от одной команды')
#     print('Цель игры — забить как можно больше мячей в ворота соперника')
# def print_hockey():
#     print('Время игры: три периода по 20 минут')
#     print('Количество игроков: 6 от одной команды')
#     print('Цель игры — забросить как можно больше шайб в ворота соперника')
# def print_sprint():
#     print('Время забега: не ограничено')
#     print('Цель — достичь финиша как можно быстрее')
#     print('Интересные факты:')
#     print('-Старейшая дисциплина лёгкой атлетики, существующая со времён первых Олимпийских игр')
#     print('-Абсолютный рекорд (9,63 сек) установлен в 2012 году У. Болтом')


# def get_full_time(experience): #зарплата тренера с учётом повышающего коэффициента
#     salary = 20000
#     if experience >= 3 and experience < 5:
#         k = 1.5
#     elif experience >= 5 and experience < 7:
#         k = 2
#     elif experience >= 7:
#         k = 3
#     else:
#         k = 1
#     salary *= k
#     return salary
# def get_part_time(hours): #зарплата тренера с почасовой оплатой
#     per_hour = 800
#     salary = hours*per_hour
#     return salary


# def get_ticket_price():
#     number = int(input('Введие номер заказа:'))
#     price = 2000
#     if number % 1000 == 0:
#         price = price * 0.8
#     return price
#
# def get_total_price():
#     count = 0
#     total = input('Желаете ли вы купить билет? off-выкл')
#     while total != "off":
#         tiket = get_ticket_price()
#         count += tiket
#         total = input('Желаете ли вы купить билет? off-выкл')
#     print ('К оплате', count)