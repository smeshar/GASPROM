import time

import connection
from functions import *
import plotext as plt
from colorama import Fore, Back, Style
from colorama import just_fix_windows_console

just_fix_windows_console()

balance = 5000
stocks_price = 228.14
inp = 0
player_stocks = 0
day = 0
next_day = True
inventary = []
prices = []
conn = connection.Conn()
name = ""

LOGO()

print(f""" Чтобы играть вам нужно {Fore.LIGHTRED_EX}зарегистрироваться{Fore.RESET}/{Fore.LIGHTGREEN_EX}войти{Fore.RESET} в аккаунт
 {Fore.LIGHTRED_EX}Зарегистрироваться{Fore.RESET} 1
 {Fore.LIGHTGREEN_EX}Войти в существующий аккаунт{Fore.RESET} 2""")

inp = int(input())
if inp == 1:
    print('---')
    print(
        f' {Fore.LIGHTGREEN_EX}Введите ваш никнейм (может содержать буквы, цифры и специальные символы, максимальная длина 20, аккаунты с непристойными никнеймами будут удалены){Fore.RESET}')
    nick = input()
    print(f' {Fore.LIGHTBLUE_EX}Введите пароль (может содержать буквы, цифры и специальные символы, максимальная длина 20){Fore.RESET}')
    psw = input()
    if conn.register(nick, psw, balance, player_stocks):
        l = conn.login(nick, psw)
        if len(l) == 0:
            inp = input()
        id = l[0]
        name = l[1]
        print(f' {Fore.LIGHTYELLOW_EX}Успешная регистрация!{Fore.RESET}')
    time.sleep(0.5)

elif inp == 2:
    print('---')
    print(
        f' {Fore.LIGHTGREEN_EX}Введите ваш никнейм{Fore.RESET}')
    nick = input()
    print(f' {Fore.LIGHTBLUE_EX}Введите пароль{Fore.RESET}')
    psw = input()
    l = conn.login(nick, psw)
    if len(l) == 0:
        inp = input()
    id = l[0]
    name = l[1]
    balance = l[3]
    player_stocks = l[4]
    print(f' {Fore.LIGHTYELLOW_EX}Успешная авторизация!{Fore.RESET}')

    time.sleep(1)

else:
    inp = input()

while True:
    # if electricity >= 30000:
    #     print('--- \n'
    #           ' Ваш долг превысил 30000 рублей')
    #     time.sleep(5)
    #     print(' Вы проиграли... Вас выселили')
    #     print(' Спасибо что поиграли в мою игру, можете попробовать заново!')
    #     print('---')
    #     time.sleep(2)
    #     exit()

    # if next_day:
    #     lastacs = stocks_price
    #     stocks_price = NEWACS(stocks_price, prices)
    #     prices.append(stocks_price)
    #     # electricity = ELEC_PLUS(electricity)
    #     # day += 1
    #     next_day = False

    stocks_price = conn.get_price()
    conn.update(id, balance, player_stocks)
    conn.get_day()

    DRAW_PLOT(conn.get_prices())
    # EVERYDAY NEWS
    print(f"--- \n"
          f" Криптовалюта Газпром стоит на данный момент: {Fore.LIGHTBLUE_EX}{round(stocks_price, 2)}{Fore.RESET} \n"
          f"---")

    print(
        f" Ваш баланс: {Fore.GREEN}{round(balance, 2)}{Fore.RESET}\n"
        f" Ваш баланс на криптокошельке: {Fore.BLUE}{round(player_stocks * stocks_price, 2)}{Fore.RESET}\n"
        f" Осталось секунд до обновления курса криптовалюты: {Fore.YELLOW}{conn.time_to_reload()}{Fore.RESET}")

    print(f"""---
 Текущие транзакции:""")
    conn.transactions()

    print(f"""---
{Fore.CYAN}Топ игроков:{Fore.RESET}""")
    conn.top_ten()

    # if (len(inventary) == 1): print(items[inventary[0]]["name"])

    # if (len(inventary) != 0):
    #     for i in range(len(inventary)-1):
    #         print(items[inventary[i]]["name"], end=", ")
    #
    #     print(items[inventary[-1]]["name"])

    print(f"---\n"
          f" {Fore.LIGHTGREEN_EX}Приобрести криптовалюту 1{Fore.RESET}\n"
          f" {Fore.LIGHTRED_EX}Продать криптовалюту 2{Fore.RESET}\n"
          f" {Fore.LIGHTYELLOW_EX}Обновить биржу 3{Fore.RESET}\n"
          f"---")

    try:
        query = int(input())
    except:
        print("Неверный ввод")
        time.sleep(1)
        continue

    # BUY STOCKS
    if query == 1:
        print(f"--- \n Введите кол-во рублей \n Ваш баланс позволяет купить криптовалюту Газпром на: {balance} рублей \n---")
        try:
            inp = float(input())
        except:
            print("Неверный ввод")
            time.sleep(1)
            continue

        if inp < 0:
            print("Неверный ввод")
            time.sleep(1)
            continue

        if inp > balance:
            print("Недостаточно средств")
            time.sleep(0.5)
            continue
        time.sleep(0.5)
        print(f"--- \n Покупка выполняется...")
        time.sleep(0.5)

        # hackers = random.randint(0, 500)
        # hackers = (hackers / 100 / 100) * inp

        # if not "защита от DDOS-атак" in inventary:
        #     print(f" Хакеры взломали биржу и ограбили вас на {hackers} рублей.\n"
        #           f" Купите защиту от DDOS-атак за 1.000.000 в магазине")

        print(f" Поздравляем, вы купили криптовалюту на {inp} рублей по цене {round(stocks_price, 2)}!\n")
        BUY_SOUND()
        inp /= stocks_price
        conn.buy_stocks(name, inp)
        balance -= inp * stocks_price
        player_stocks += inp

    # SELL STOCKS
    if query == 2:
        print(f"--- \nВведите кол-во рублей на которые вы хотите продать крипту")
        print(f"Ваш баланс позволяет продать: {round(player_stocks * stocks_price, 2)} рублей \n---")
        try:
            inp = float(input())
        except Exception as e:
            print(f"Неверный ввод, ошибка {e}")
            time.sleep(1)
            continue

        if inp < 0:
            print("Неверный ввод")
            time.sleep(1)
            continue

        if inp > round(player_stocks * stocks_price, 2):
            print("Вы не можете продать так много криптовалюты")
            time.sleep(1)
            print()
            continue
        time.sleep(0.5)
        print("--- \n Подготовливаем к продаже...")
        time.sleep(0.5)

        print(" Ищем покупателя...")
        time.sleep(random.triangular(0.5, 4))
        print(f" Поздравляем, вы продали криптовалюту Газпром на {inp} рублей по цене {round(stocks_price, 2)}!")
        SELL_SOUND()
        print()
        inp /= stocks_price
        conn.sell_stocks(name, inp)
        balance += inp * stocks_price
        player_stocks -= inp
        next_day = True

    # RELOAD STOCKS
    if query == 3:
        continue

    # PAY FOR ELECTRICITY
    # if query == 4:
    #     print('---')
    #     time.sleep(0.5)
    #     print("Переводим деньги...")
    #     time.sleep(0.5)
    #     print("Перевод выполнен успешно...")
    #     PAY_ELEC()
    #     if balance >= electricity:
    #         balance -= electricity
    #         electricity = 0
    #     else:
    #         electricity -= balance
    #         balance = 0
    #     next_day = True

    # SHOP
    if query == 7:
        print('---\nМагазин DИS\nВременно не работает')
        time.sleep(0.5)
        continue
        print('---\nМагазин DИS\nДоступные товары:')

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
            SHOP_SOUND()
            balance -= items[goods]["price"]
            inventary.append(goods)
            next_day = True
            break

        time.sleep(0.5)

    time.sleep(1)
