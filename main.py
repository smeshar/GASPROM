from functions import *
from termcolor import colored
import plotext as plt
from uuid import getnode as get_user

balance = 1000
player_stocks = 0
stocks_price = 228.14
inp = 0
k = 0
day = 0
next_day = True
elecnul = False
electricity = 0
inventary = []
prices = [stocks_price]

try:
    storymode = ENCODE(6)
except IndexError:
    storymode = True
    
user = get_user()

LOGO()

if storymode:
    START()
    storymode = False

while True:
    if electricity >= 30000:
        print('--- \n'
              ' Ваш долг превысил 30000 рублей')
        time.sleep(5)
        print(' Вы проиграли... Вас выселили')
        print(' Спасибо что поиграли в мою игру, можете попробовать заново!')
        print('---')
        time.sleep(2)
        exit()

    if next_day:
        lastacs = stocks_price
        stocks_price = NEWACS(stocks_price, prices)
        prices.append(stocks_price)
        if not elecnul:
            electricity = ELEC_PLUS(electricity)
        day += 1
        next_day = False

    DRAW_PLOT(prices)
    # EVERYDAY NEWS
    print(f"--- \n"
          f" Акции Газпрома стоят на данный момент: {round(stocks_price, 2)} \n"
          f"---")

    player_stocks = round(k * stocks_price, 2)


    print(
        f" Ваш баланс: {round(balance, 2)} \n"
        f" Ваш баланс в акциях: {player_stocks} \n"
        f" День: {day} \n Неоплаченный счет в банке: {round(electricity, 2)} \n"
        f" Купленные приколюхи: ", end="")



    if (len(inventary) == 1): print(inventary[0])

    else:
        for i in inventary:
            print(i, ", ", end="")

    print(f"\n---\n"
        f" Чтобы приобрести акции нажмите 1 \n"
        f" Чтобы продать акции нажмите 2 \n"
        f" Чтобы подождать нажмите 3 \n"
        f" Чтобы оплатить долг нажмите 4 \n"
        f" Чтобы сохранить игру нажмите 5 \n"
        f" Чтобы загрузить сохранение нажмите 6 \n"
        f" Чтобы зайти в магазин нажмите 7 \n"
        f"---")

    query = input()

    # BUY STOCKS
    if query == "1":
        print(f"--- \n Введите кол-во рублей \n Ваш баланс позволяет купить акции на: {balance} рублей \n---")
        inp = float(input())
        if inp > balance:
            print("У вас слишком маленький баланс")
            time.sleep(0.5)
            continue
        time.sleep(0.5)
        print(f"--- \n Покупка выполняется...")
        time.sleep(0.5)

        hackers = random.randint(0, 300)
        hackers /= 100
        print(f"\n Хакеры взломали биржу и ограбили вас на {hackers} рубля\n"
              f" Купите защиту от DDOS-атак за 1.000.000 в магазине\n"
              f" Поздравляем, вы купили акции на {inp - hackers} рублей по цене {round(stocks_price, 2)}!\n")
        inp -= hackers
        inp /= stocks_price
        balance -= inp * stocks_price
        k += inp

    # SELL STOCKS
    if query == "2":
        print(f"--- \nВведите кол-во рублей на которые вы хотите продать акции")
        print(f"Ваш баланс позволяет продать: {player_stocks} рублей \n---")
        if (player_stocks // stocks_price) < 1:
            print("У вас нет акций")
            print("Стоит подождать")
            time.sleep(1)
            print()
            continue
        inp = float(input())
        if inp > player_stocks:
            print("Вы ввели число большее чем вы можете продать")
            time.sleep(1)
            print()
            continue
        time.sleep(0.5)
        print("--- \n Подготовливаем к продаже...")
        time.sleep(0.5)

        print(" Ищем покупателя...")
        time.sleep(random.triangular(0.5, 4))
        print(f" Поздравляем, вы продали акции на {inp} рублей по цене {round(stocks_price, 2)}!")
        print()
        inp /= stocks_price
        balance += inp * stocks_price
        k -= inp
        next_day = True

    # SKIP DAY
    if query == "3":
        #stocks_price = NEWACS(stocks_price, up_or_down)
        next_day = True
        continue

    # PAY FOR ELECTRICITY
    if query == '4':
        print('---')
        if balance < electricity:
            print('Недостаточно средств')
            continue
        time.sleep(0.5)
        print("Переводим деньги...")
        time.sleep(0.5)
        print("Перевод выполнен успешно...")
        balance -= electricity
        electricity = 0
        next_day = True
        elecnul = True

    # SAVE PROGESS
    if query == '5':
        print('---')
        print(' Сохраняемся')

        DECODE(balance, player_stocks, stocks_price, k, day, electricity, int(storymode), user)

        time.sleep(0.5)

    # LOAD SAVE
    if query == '6':
        print('---\n Загружаем сохранение\n---')

        if user != ENCODE(7):
            print("Неверный пользователь")
            time.sleep(1)
            continue

        balance = ENCODE(0)
        player_stocks = ENCODE(1)
        stocks_price = ENCODE(2)
        k = ENCODE(3)
        day = ENCODE(4)
        electricity = ENCODE(5)
        storymode = ENCODE(6)


        time.sleep(1)

    # SHOP
    if query == '7':
        items = {
            1: {"name": "аркана на сфа", "price": 2500},
            2: {"name": "телевизор", "price": 10000},
            3: {"name": "ноутбук Apelsin Book", "price": 100000},
            4: {"name": "защита от DDOS-атак", "price": 1000000},
            5: {"name": "бугати", "price": 10000000},
            6: {"name": "квартира в майам... в чебоксарах", "price": 15000000}
        }

        print('---\nМагазин DNS\nДоступные товары:')

        for item_id, item_info in items.items():
            print(f' {item_id}. {item_info["name"]} - {item_info["price"]} рублей')

        print(' Чтобы выйти из магазина напишите 7\n---')

        while True:
            goods = int(input('Чтобы выбрать товар, напишите его номер: '))

            if goods == 7: break

            if goods not in items:
                print("Такого продукта нет.")
                continue

            if balance < items[goods]["price"]:
                print(f'Недостаточно средств. Требуется {items[goods]["price"]} рублей.')
                continue

            print(f'---\n Вы приобрели {items[goods]["name"]}!')
            balance -= items[goods]["price"]
            inventary.append(items[goods]["name"])
            next_day = True
            break

        time.sleep(0.5)

    time.sleep(1)
