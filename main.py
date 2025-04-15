# surname = "Иванов"
# people_amount = 24
# ticket_price = 2450
# total = people_amount * ticket_price
# print('Экскурсовод -',surname )
# print('Стоимость пакета:', total)
# # Один из бухгалтеров турфирмы пытался написать программу для вычисления экскурсионного пакета услуг, но сделал много ошибок.
# #
# # Исправь ошибки в задании и использовании переменных, допиши программу. Она должна срабатывать как на картинке.
from itertools import count
from operator import length_hint, index

import module

# Стажёр Олег помогал экскурсионному отделу турфирмы. Олег должен был написать программу, вычисляющую полную стоимость поездки школьников в театр.
#
# В театр должна была поехать группа: 2 взрослых и 31 ребёнок. Цена взрослого билета 3699 руб, а детского —1100 руб.
#
# Исправь ошибки в использовании переменных. Программа должна выводить результат как на картинке.

# adults = 2
# children = 31
# adult_price = 3699
# child_price = 1100
# total = adults * adult_price + children * child_price
# print('Полная стоимость:', total)

# В турфирму обратилась семья из 3 человек. Они хотят купить ВСЕ возможные страховки от несчастных случаев в путешествии.
#
# Турфирма предлагает страховки:
# - при потере багажа — 890 руб/за человека,
# - при отмене рейса — 875 руб/за человека,
# - при болезни — 1345 руб/за человека,
# - при потере документов — 2199 руб/за человека.
#
# Рассчитай полную стоимость услуг и выведи результат с пометкой «Стоимость страхования семьи: ». По возможности используй переменные.
#
# luggage = 890
# transport = 875
# health = 1345
# pasport = 2199
# people = 3
# total = (luggage + transport + health + pasport)* people
# print("Стоимость страхования семьи", total)






# percent = 35
# tour = 56720
# percent_tour = (percent*tour)/100
# burning_tour = tour - percent_tour
# print("Стоимость горящего тура:",burning_tour)

# Tuesday = 2100
# Wednesday = 2100
# Thursday = 2100
# Friday = 2850
# Saturday = 2850
# Sunday = 2850
# total = Tuesday + Wednesday + (Thursday*2) + (Friday*2) + (Saturday*2) + Sunday
# print (total)





# price_hotel = input('Введите стоимость одной ночи в отеле:')
# price_hotel = int (price_hotel)
# days = input('Введите количество дней отдыха:')
# total = price_hotel * (int (days))
# print('Стоимость отдыха:', total)


# price = input ('Введите цену билета: ')
# bonus = input ('Введите количество бонусов: ')
# total = int (price) - int (bonus)
# print ('Стоимость билета:', total)



# Здравствуйте
# Вы путешествовали с нами уже ... раз(а)! Хотите снова?
# Наша турфирма проводит распродажу. Тур в ... со скидкой 50%!


# client = input ('Введите имя клиента: ')
# tures = input ('Ввидите количество ранее купленых туров: ')
# kuda_hochesh = input ('Предлогаемый тур: ')
# print ('Здравствуйте', client+'.\nВы путешествовали с нами уже', tures,'раз(а)! Хотите снова?''\nНаша турфирма проводит распродажу. Тур в', kuda_hochesh,'со скидкой 50%!')

# price = input ('Стоимость путёвки')
# cashback = int (price) * 0.05
# print ('Вам начислен кэшбэк в размере', int (cashback))



# Homework

# feedback = input('Оставьте отзыв о путешествии:')
# length = len (feedback)
# print('Спасибо за подробный отзыв! В нём целых', length, 'символов!')



# feedback = 'Корпуcа 2, 7 и 9 - самые уютные! Если выберете этот отель, то останавливайтесь в них'
# building1 = feedback[8]
# building2 = feedback[11]
# building3 = feedback[15]
# print('Клиенты выбирают корпуса:', building1, building2, building3)



# feedback = 'Вид на море - это фишка отеля!'
# feedback_advert = feedback[0:11]
# print('Нашим клиентам нравится:', feedback_advert)


# dishes = input('Введите любимые блюда ресторана "Подсолнух":')
# searching1 = 'шоколадный торт'
# searching2 = 'шашлык'
# result1 = dishes.find(searching1)
# result2 = dishes.find(searching2)
# print(searching1, result1)
# print(searching2, result2)



# feedback = 'Волшебный Отель с супер ресторанами. Лучший на Кипре. Качественная еда, большое разнообразие. Прекрасный пляж и сервис. Чистые и просторные номера! Все на пять! Японская кухня оставляет приятное впечатление. Всегда, приезжая в Лимассол, заказываем суши и роллы. Мимо витрины со сладким очень сложно пройти не остановившись, хотя бы посмотреть. Тихий район - это круто!'
# searching1 = 'тихий район'
# searching2 = 'вкусно'
# feedback_low = feedback.lower()
# result1 = feedback_low.find(searching1)
# result2 = feedback_low.find(searching2)
# print (searching1, result1)
# print (searching2, result2)


# city = input('Введите город:')
# district = input('Введите район:')
# rating = input('Введите рейтинг:')
# searching = city + '/' + district + '/' + rating
# print('Запрос',  searching,'сформирован')


# id_number = '12451512'
# surname = 'Степашин'
# tour = 'Занзибар'
# client_data = id_number + '/' + surname + '/' + tour
# print('Информация о клиенте:',client_data)



# review = input ('Оцените нас 1-5:')
# dizlike = input ('Что не понравилось:')
# print('Оценка:', review +'-'+ dizlike)


# review = input ('Оцените нас:')
# like = input ('Что понравилось:')
# dizlike = input ('Что не понравилось:')
# dlinna = len (review + like + dizlike)
# discount = dlinna * 0.1
# print('Скидка:', discount)

# price_human = int(input('Цена билета на самолёт:'))
# price_luggage = int(input('Цена провоза багажа:'))
# price_meal = int(input('Цена питания на борту:'))
# total = price_human + price_luggage + price_meal
# print('К оплате:', total)

# necTask = int(input('Количество выполненых заданий:'))
# additionally = int(input('Количество выполненых доп задани'))
# total = necTask * 15 + additionally * 20
# print (total)

# review = input ('Оставте отзыв:')
# lenght = len(review)
# cool = review.find('круто')
# bad = review.find('скучно')
# print('Длинна отзыва:',lenght)
# print('Поиск недостатков', bad)
# print('Поиск достоинств', cool)

# #Программа для печати стажёров, с которыми будет заключён договор
# note = 'Варя, Миша и Стас отлично проявили себя на стажировке'
# offer = note[0:4] + '/' + note[6:10] + '/' + note[13:17]
# print('Выслать предложение о работе:', offer)

# month_salary = int (input('Введите зарплату за месяц:'))
# vacation = int(input('Введите количество дней отпуска:'))
# month = 29.3 #среднее количество дней в месяце
# daily_salary = month_salary/month
# vacation_pay = daily_salary*vacation
# print('Примерные отпускные:', vacation_pay)

# month_salary = int(input ('Введите ежемесечную зарплпту'))
# hours = int(input('Количество часов в выходные'))
# bonus = month_salary * 0.01 * hours
# print('Премия:',bonus)


# weekly_hours = int(input('Количество рабочих часов в неделю:'))
# hour_salary = int(input('Желаемая зарплата за час:'))
# month_salary = hour_salary * weekly_hours * 4
# max_salary = 80000
# print ('Одобрено. Выделить из бюджета:', month_salary)

# favorite_taste = input ('Какой вкус вам больше нравится:')
# if favorite_taste == 'ванильный':
#     print ('рекомендуем чизкейк')
# else:
#     print ('попробуйте орехзовый торт')



# answer = input('Вы первый раз в Сладких историях?')
# answer = answer.lower()
# if answer == 'да':
#     print('Скидка 40% для новичков. Промокод NEW')
# else:
#     print('Торты со скидкой 10%. Промокод CAKE')



# max_price = int(input('Какую сумму вы готовы потратить на сладости?'))
# if max_price <= 500:
#     print('Попробуйте пирожные со сгущенкой!')
# if max_price >= 500 and max_price <= 1000:
#     print('Побалуйте себя тортиком Секрет!')
# if max_price > 1000:
#     print('Угоститесь шоколадным фонданом с голубикой!')



# weight = int (input ('введите ваш вес:'))
# height = int (input ('введите ваш рост:'))
# if (height - weight) > 100:
#     print ('Ваш вес в норме. Может, по куасану?:')
# else:
#     print ('Попробуйте ягодный мусс:')



# age = int (input ('ведите ваш возраст:'))
# if age < 30:
#     print ('возьмите фисташковое мороженое:')
# else:
#     print ('возьмите тёмный шоколад:')



# fruits = input ('Что хотите, фрукты или овощи?')
# if 'фрукты' == fruits:
#     fruty = input ('Какие фрукты хотите, с косточками или без?')
#     if 'без' == fruty:
#         print ('Ананасы')
#     else:
#         print ('Яблоки')
# else:
#     vechtabels = input ('Желайте сезонные овощи?')
#     if 'да' == vechtabels:
#         print ('Броккли')
#     else:
#         print ('Картофель')





# meal = input ('Приём пищи').lower()
# if meal == 'завтрак':
#     print ('Каша')
# else:
#     wish = input ('Вы хотите плотно поесть?').lower()
#     if wish == 'да':
#         print ('Плов')
#     else:
#         print ('Котлета с пюре')



# sales = input('Желаете товары по акции?')
# if sales == 'да':
#     category = input('Введите категорию:')
#     if category == 'сладости':
#         print('Фруктовый мармелад за 200 рублей')
#     else:
#         print('Брусничный морс за 140 рублей')
# else:
#     print('Сообщите, если передумаете!')



# category = input('Категория в разделе "Прямо с грядки":')
# if category == 'зелень':
#     max_price = int (input('Максимальная цена:'))
#     if max_price >= 100:
#         print('Попробуйте салатные миксы')
#     else:
#         print('Попробуйте ассорти из лука и петрушки')
# else:
#     print('Как насчёт батата?')



# answer = input ('Хотите ли узнать о хитах продаж?:').lower()
# if answer == 'да':
#     category = input('Какая категория вас интересует?:').lower()
#     if category == 'продукты':
#         print ('Молоко 1л, Печенье с изюмом, Персики')
#     else:
#         print ('Стиральный порошок, Щётка для обуви')
# else:
#     print ('Дайте знать, если передумаете!')



# price1 = int(input ('Цена первого товара:'))
# price2 = int(input ('Цена первого товара:'))
# price3 = int(input ('Цена первого товара:'))
# if price1 >= price2 and price1 >= price3:
#     print ('Итого к оплате:',price1)
# else:
#     if price2 >= price1 and price2 >= price3:
#         print ('Итого к оплате:',price2)
#     else:
#         print ('Итого к оплате:',price3)

# Или
# print ('К оплате:',max(price1,price2,price3))



# meal = input ('Приём пищи:').lower()
# if meal == 'завтрак':
#     print ('Каша')
# elif meal == 'обед':
#     print ('Суп с тефтелями')
# else:
#     print ('Блины с рыбой')


# category = input('Введите категорию:').lower()
# if category == 'хит продаж':
#     print('Товар недели - виноград Киш-миш')
# elif category == 'веган':
#     print('Попробуйте спаржу с тофу!')
# else:
#     print('Как насчёт свиного шашлычка?')



# price = int (input ('Цена товара:'))
# time = int (input ('Время покупки:'))
# if time >= 20 and time <= 22:
#     print ('К оплате:',price/2)
# elif time >= 8 and time <= 19:
#     print ('К оплате:',price/2)
# elif time <= 0 or time > 24:
#     print ('Введено неправилное время')
# else:
#     print('Магазин не работает')



# yesterday = int(input ('Колличество человек за вчера'))
# b_yesterday = int(input ('Колличество человек за позавчера'))
# if yesterday > b_yesterday:
#     total = (yesterday - b_yesterday) + yesterday
# elif b_yesterday > yesterday:
#     total = yesterday - (b_yesterday - yesterday)
# else:
#     total = yesterday
# print (total)



# code = input ('Введите номер карты')
# while code != '45626':
#     print ('Повезёт в следующий раз!')
#     code = input ('Введите номер карты')
# print ('Вы выйграли')



# review = input ('Введите отзыв (off-завершить: ')
# while review != 'off':
#     print ('Спазибо за обратную связь')
#     review = input ('Введите отзыв: ')



# price = int (input ('Введите цену товара (0-завершить): '))
# total = 0
# while price != 0:
#     total = price + total
#     price = int (input ('Введите цену товара (0-завершить): '))
# print (price * 0.9,'цена с учётом скидки')



# time = int (input('Введите текущее время в часах:'))
# while time >= 10 and time < 24:
#     print ('Мы открыты')
#     time = int(input('Введите текущее время в часах:'))
# print('Мы закрыты. Часы работы: с 10 до 24.')



# while input('Введите промокод:') != 'life':
#     print ('Этот промокод недействителен')
# print ('Промокод принят')


# text = input ('Введите текст: ')
# while len (text) > 0:
#     print (text [0])
#     text = text [1:]


# price = int (input ('Ведите цену товара'))
# total = 0
# amount = 0
# while price != 0:
#     amount += 1
#     total += price
#     price = int (input('Ведите цену товара'))
# if amount % 2 == 0:
#     total = total/2
#     print ('Акция "Цены пополам"')
# print ('К оплате:',total)



# count = 0
# while count != 3:
#     card = input ('Введите номер карты:')
#     count += 1
#     print ('Вы получили скидку')
# print ('Скидки закончились')



# promo = input ('Введите промокод:')
# count = 1
# while promo != 'fresh' and count < 3:
#     count += 1
#     promo = input('Введите промокод:')
# if promo == 'fresh':
#     print ('Принято с попытки №', count)
# else:
#     print ('Попытки закончились')



# category = input ('Введите категорию:')
# count = 0
# while category != 'end':
#     count += 1
#     category = input('Введите категорию:')
# print ('Всего категорий товаров:', count)



# tree = int (input ('Введите число:'))
# count = 0
# while count < tree:
#     print (' ' * (tree - count - 1) + '*' * (2 * count + 1))
#     count += 1


# talon = int(input ('Введите 0 получить талон, 1 выключить аппарат:'))
# count = 0
# while talon != 1:
#     if talon == 0:
#         count += 1
#         print ('Номер талона -',count )
#     talon = int(input('Введите 0 получить талон, 1 выключить аппарат:'))
# print ('Приходите ещё')




# total = 0
# count = int(input('Количество оценок:'))
# for i in range(count):
#     mark = input('Оценка:')
#     total += mark
# print('Среднее:', total/count)




# for i in range(3):
#     wish = input ('Введите предпочтение:')
#     print ('Предпочтение учтено')
# print ('Система рекомендаций настроена')



# count = input('Колличество участников:')
# for i in range (int(count)):
#     name = input ('Введите имя:')
#     print ('Добро пожаловать,', name)
# print ('Групповой чат создан!')



# login = input('Введите имя:')
# wrong = '=?*^$№@_'
# for i in login:
#     if i in wrong:
#         print ('Неверный символ:', i)


# password = input ('Введите пароль:')
# alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# final = ''
# for i in password:
#     number = (alphabet.find(i) + 1)
#     final += str (number) + ' '
# print (f'Пароль: {password} зашифрован как {final}')



# count = int (input ('Введите колличество рег. аккаунтов:'))
# for i in range(count):
#     login = input ('Введите имя:')
#     age = int(input ('Ведите возраст:'))
#     if age < 14:
#         print ('Ошибка')
#     else:
#         print ('Аккаунт создан:', login)



# game = input('Введите слово:')
# while game != 'off':
#     if game == 'game':
#         for j in range(3):
#             i = int(input('Угадай число!'))
#             if i == 5:
#                 print ('Вы выиграли билет на концерт!')
#                 break
#     game = input('Введите слово:')



# number = input('Введите 1 - рекомендация, off - завершить')
# while number != 'off':
#     if number == '1':
#         preference = input('Ваше настроение:')
#         if preference == 'весёлое':
#             print('Мультфильм Шрек')
#         else:
#             print('Мультфильм Алладин')
#     number = input('Введите 1 - рекомендация, off - завершить')



# number = input('Введите номер действия:')
# while number != 'off':
#     if number == '1':
#         wish = input('Выберите предпочтение:')
#         if wish == 'спорт':
#             print ('Подкаст Убойный спорт.')
#         else:
#             print ('Новый альбом Канье Уэста')
#     elif number == '2':
#         for i in range(3):
#             music = input ('Отгадайте группу:')
#             if music == 'queen':
#                 print('Вы выиграли билет на концерт!')
#                 break
#     number = input('Введите номер действия:')


# def print_lable(name, amount):
#     for i in range(amount):
#         print ("Английский язык")
#         print ('Имя ученика:',name)
# name = input ('Введите имя ученика:')
# count = int(input('Колличество этикеток:'))
# print_lable(name,count)



# def average_grade(name):
#     grade = int(input('Введите оценку:'))
#     count = 0
#     total = 0
#     while grade != 0:
#         total += grade
#         count += 1
#         grade = int(input('Введите оценку:'))
#     print (name,'- средний балл -',total/count)
# amount = int(input('Введите колличество учеников:'))
# for i in range(amount):
#     name = input ('Введите имя ученика:')
#     average_grade(name)

# def print_lable():
#     print ('Золотое пёрышко')
#     print ('Имя:')
#     print('Школа:')
# people = int(input('Введите число учеников:'))
# for i in range(people):
#     print_lable()
# print ('Готово! Заберите бейджики')



# def setstatus(score):
#     if score >= 0 and score <= 49:
#         print('Скидка 10 процентов')
#     elif score >= 50 and score <= 99:
#         print('Скидка 15 процентов')
#     elif score >= 100:
#         print ('Скидка 20 процентов')
#     else:
#         print ('Ошибка')
#
# a = int(input('Введите колличество баллов:'))
# setstatus(a)



# def setstatus(name,score):
#     if score >= 50 and score <= 99:
#         return f'{name} - диплом 3-й степени'
#     elif score >= 100 and score <= 199:
#         return f'{name} - диплом 2-й степени'
#     elif score >= 200:
#         return f'{name} - диплом 1-й степени'
#     else:
#         return ('Спасиба, уходи')
#
# name = input ('Введите имя:')
# score = int(input('Введите колличество баллов:'))
# result = setstatus (name,score)
# print (result)
# if result == f'{name} - диплом 1-й степени':
#     print ('Сертификат на книги')







# if условие(True/False):
#     если True, то выполняется это действие
# else:
#     если False, то выполняется это действие
# 
# if условие(True/False):
#     если True, то выполняется это действие
# elif условие(True/False):
#     если True, то выполняется это  действие
# else:
#     если False, то выполняется это действие


#def check_test(score):
#     if score >= 80:
#         return True
#     else:
#         return False
# amount = int(input('Введите число участников:'))
# for i in range(amount):
#     name = input('Введите имя:')
#     score = int(input('Введите баллы за тест:'))
#     res = check_test(score)
#     print('Допуск:', res)




# def get_course(wish):
#     if wish.find('спорт') != -1:
#         course = 'волейбол'
#     elif wish.find('наука') != -1:
#         course = 'астрономия'
#     elif wish.find('комиксы') != -1:
#         course = 'скетчинг'
#     else:
#         course = 'история Древнего Рима'
#     return course
#
# amount = int(input('Введите число участников:'))
# for i in range(amount):
#     wish = input ('Введите предпочтение')
#     a = get_course(wish)
#     print (a)
#     if a == 'астрономия':
#         print ('Занятия проходят ночью')





# def check_test(score):
#     if score >= 50:
#         return True
#     else:
#         return False
# amount = int(input('Введите число участников:'))
# for i in range (amount):
#     score= int(input('Введите балл'))
#     result = check_test(score)
#     print (result)




# def is_ok(score):
#     if score >= 100:
#         return True
#     else:
#         return False
# amount = int(input('Введите число участников:'))
# for i in range (amount):
#     score= int(input('Введите балл'))
#     result = is_ok(score)
#     print ('Доступен ли мерч:',result)




# def check_mark ():
#     mark = int(input('Введите оценку:'))
#     count = 0
#     while mark != 0:
#         if mark == 5:
#             count += 1
#         mark = int(input('Введите оценку:'))
#     return count
#
# def set_discount():
#     a = check_mark()
#     if a >=1 and a <= 3:
#         return 3
#     elif a >=4 and a <= 5:
#         return 5
#     elif a > 5:
#         return 10
#     else:
#         return 0
# print ('Скидка на поездку:', set_discount())





# def imt(weight,height):
#     index = weight/height*height
#     return index
#
# def check_imt(weight,height):
#     index = imt(weight,height)
#     if index <= 18.5:
#         print ('Ваш имт',index,'у вас недостаточный вес')
#     elif index > 18.5 and index <= 25:
#         print ('Ваш имт',index,'у вас вес в норме')
#     else:
#         print ('Ваш имт',index,'у вас избыточный вес')
#
#
# weight = float(input('Введите свой вес'))
# height = float(input('Введите свой рост'))
# check_imt(weight,height)





# def get_result(score):
#     if score >= 85:
#         return '1 место'
#     elif score >= 65 and score < 85:
#         return '2 место'
#     elif score >= 50 and score < 65:
#         return '3 место'
#     else:
#         return 'Повезёт в другой раз!'
# score = int(input('Введите балл:'))
# print('Ваш результат:', get_result(score))


# def get_result(score):
#     if score >= 85:
#         return '1 место'
#     elif score >= 65 and score < 85:
#         return '2 место'
#     elif score >= 50 and score < 65:
#         return '3 место'
#     else:
#         return 'Повезёт в другой раз!'
#
#
# def give_reward(result):
#     if result == '1 место':
#         return 'Поездка в СПБ'
#     elif result == '2 место':
#         return 'Сертификат в книжный магазин'
#     elif result == '3 место':
#         return 'Настольная игра'
#     else:
#         return 'Шиш'
#
#
# score = int(input('Введите балл:'))
# result = get_result(score)
# reward = give_reward(result)
# print('Ваш результат:', result, '-', reward)



# def student_score(amount):
#     score = 0
#     for i in range(amount):
#         mark = int(input('Введите количество баллов'))
#         score += mark
#     print ('Общее колличество баллов',score)
#     return score
#
# def give_reward(amount):
#     score = student_score(amount)
#     if score > 80:
#         return'Наградить дипломом'
#     elif score > 50 and score <= 80:
#         return'Наградить похвальной грамотой'
#     else:
#         return'Выдать грамоту об участии'
#
#
#
#
# student_name = input('Введите имя студента:')
# while student_name != 'стоп':
#     num_subjects = int(input('Введите количество предметов:'))
#     print (give_reward(num_subjects))
#     student_name = input('Введите имя студента:')






# def calc_bmi(weight, height):
#     index = weight / (height ** 2)
#     return index
#
# def print_recommendation(x):
#     if x <= 18.5:
#         print("У вас недостаточный вес, пройдите на консультацию в кабинет 301.")
#     elif 18.5 < x <= 25:
#         print("Ваш вес в норме, пройдите на 3 этаж для продолжения осмотра.")
#     else:
#         print("У вас избыточный вес, пройдите на консультацию в кабинет 410.")
#
# weight = float(input('Введите вес (кг): '))
# height = float(input('Введите рост (м): '))
# x = calc_bmi(weight, height)
# print_recommendation(x)






# def get_result(score):
#     for i in range(3):
#         if score >= 65:
#             return 'Успеваемость в норме.'
#         elif score >= 50 and score < 65:
#             return 'Низкая успеваемость!'
#         else:
#             return 'Не уровень!'
# for i in range(3):
#     score = int(input('Введите балл:'))
#     print('Ваш результат:', get_result(score))





# def ask_question ():
#     question = input ('Что вас интересуют? (стоп - завершить)')
#     if question == 'стоп':
#         print ('Досвидания')
#     elif question == 'лаборатория':
#         laboratory_info()
#     elif question == 'лекторий':
#         lectory_info()
#     else:
#         print ('Пожалуйста уточните')
#         ask_question()
#
# def laboratory_info():
#     print ('Лаборатория в кабинете А 203')
#     ask_question()
#
# def lectory_info():
#     print ('info')
#     ask_question()
#
# ask_question ()



# from random import *
#
# total = int(input('Введите кол-во команд:'))
# x1=randint (1,total)
# x2=randint (1,total)
# print (x1,x2)



# from random import *
#
# win_number = 1
# current_number = randint(1, 2)
# print('Номер лотерейного билета:',current_number)
# if current_number == win_number:
#     print('Вы выиграли ужин в ресторане!')
# else:
#     print('Повезёт в другой раз!')



# from random import *
# count1 = 0
# count2 = 0
# total = input('Получить номер?:')
# while total != 'off':
#     number = randint(1,2)
#     print ('Ваш номер',number)
#     if number == 1:
#         count1 += 1
#     else:
#         count2 += 1
#     print ('Участников в первом забеге:',count1,',''участников во втором забеге:',count2)
#     total = input('Получить номер?:')



# from random import *
# word= 'ABCDEFGH'
# x1=randint (0,7)
# x2=randint (1,8)
# print (word[x1]+str(x2))


# from random import *
# team1=int(input('Введите кол-во участников:'))
# team2=int(input('Введите кол-во участников:'))
# swimmer1=randint (1,team1)
# swimmer2=randint (1,team2)
# print ('Пловец',swimmer1,'-пловец',swimmer2)

# Каждый месяц Go Ahead проводит турнир по быстрым шахматам. Каждому игроку отводится 30 минут на все ходы в партии.
#
# При запуске программы запускается подсчёт времени. После каждого хода выводится сообщение: «Осталось _ минут из 30». Таймер прерывается в двух случаях:
# 1) Закончилось время.
# 2) Введено «off» (игрок сдаётся).
#
# Исправь ошибки в программе.

# from time import time
# move = ''
# rest = 30
# begining = time()
# while rest > 0 and move != 'off':
#     move = input('Ваш ход (off - сдаться):')
#     end = time()
#     rest = 30 - (end - begining)/60
#     print('Осталось', int(rest), 'минут из 30')




# Запрограммируй обратный отсчёт!
# Многие спортсмены жаловались, что судья слишком тихо отсчитывает секунды,
# оставшиеся до старта («Три!.. Два!.. Один!..»). Фирма Go Ahead купила табло для наглядного отображения оставшегося времени.
#
# Запрограммируй табло так, чтобы оно по порядку печатало, сколько секунд осталось


# from time import sleep
# seconds = int(input('Введите кол-во секунд:'))
# for i in range (seconds):
#     print (seconds)
#     seconds -= 1
#     sleep(1)
# print ('Марш!')




# import module
# answer= (input('\n1-футбол\n2-хоккей\n3-бег на 100 метров\noff-завершить\n'))
# while answer != 'off':
#     if answer == "1":
#         module.print_football()
#     elif answer == '2':
#         module.print_hockey()
#     elif answer == '3':
#         module.print_sprint()
#     else:
#         print('Ошибка')
#     answer = (input('\n1-футбол\n2-хоккей\n3-бег на 100 метров\noff-завершить\n'))



# surname = input('Введите фамилию:')
# grafic = input('\nКакой график удобнее?\n1-полный\n2-почасовой\n')
# if grafic == '1':
#     experience = int(input('Введите стаж:'))
#     salary = module.get_full_time(experience)
# elif grafic == '2':
#     hours = int(input('Введите кол-во часов работы:'))
#     salary = module.get_part_time(hours)
# print (surname,salary)


# import module
# foot_ball = input('Хотите посетить чемпионат по футболу?')
# if foot_ball == 'да':
#     module.get_total_price()
# else:
#     print ('А надо бы')


# import turtle as t
# scr = t.Screen()
# t1 = t.Turtle()
# t1.color('green')
# for i in range(4):
#     t1.forward(100)
#     t1.left(90)
# t1.color('yellow')
# for i in range(3):
#     t1.forward(100)
#     t1.left(120)
# scr.mainloop()


# import turtle as t
# scr = t.Screen()
# t1 = t.Turtle()
# t1.color('green')
# for i in range(1000):
#     t1.forward(i)
#     t1.left(59)
#
# scr.mainloop()


# import turtle as t
# scr = t.Screen()
# t1 = t.Turtle()
# t1.color('green')
# for i in range(4):
#     t1.forward(100)
#     t1.left(90)
# t1.color('yellow')
# for i in range(3):
#     t1.forward(100)
#     t1.left(120)
# scr.mainloop()