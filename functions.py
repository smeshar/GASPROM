import random
import time
import math
import plotext as plt
import sys
import winsound

def LOGO():
    print('---')
    print("  ________                                                        ")
    print(" /  _____/  _____      ______ ______   _______    ____     _____  ")
    print("/   \  ___  \__  \    /  ___/ \____ \  \_  __ \  /  _ \   /     \ ")
    print("\    \_\  \  / __ \_  \___ \  |  |_> >  |  | \/ (  <_> ) |  Y Y  \ ")
    print(" \______  / (____  / /____  > |   __/   |__|     \____/  |__|_|  /")
    print("        \/       \/       \/  |__|                             \/ ")
    print("---")

def story():
    print("Нажмите Enter для продолжения: ")
    ans = input()
    return

def QUESTION():
    while True:
        print("Да или нет?")
        ans = input()
        if ans.casefold() != "да":
            print("Нет такого варианта ответа")
        else:
            return

def START():
    print("Добро пожаловать в экономическую игру GASPROM!")
    story()
    print("Эх, как же я устал работать в шестерочке. Работаю по 10 часов в день, а денег не хватает. Пойду посмотрю в telegram, может что-то интересное написали")
    story()
    print("ДАРОВА! ХОЧЕШЬ ЗАРАБОТАТЬ?")
    QUESTION()
    print("ВСЕ ПРОСТО! ВОТ ПРОГРАММА! ПОКУПАЕШЬ АКЦИИ ГАЗПРОМА ПО НИЗКОЙ ЦЕНЕ, ПРОДАЕШЬ ПО ВЫСОКОЙ")
    story()
    print("Варианта у меня нет, за электричество платить надо, ведь если долг превысит 30к рублей, то меня выселят из квартиры")
    story()

def DECODE(balance, player_stocks, stocks_price, k, day, electricity, storymode, user, inventary):
    outfile = open("table.txt", "w")

    num1 = float.hex(float(balance))
    num2 = float.hex(float(player_stocks))
    num3 = float.hex(float(stocks_price))
    num4 = float.hex(float(k))
    num5 = float.hex(float(day))
    num6 = float.hex(float(electricity))
    num7 = float.hex(float(storymode))
    num8 = str(user)

    outfile.write(num1 + '\n' + num2 + '\n' + num3 + '\n' + num4 + '\n' + num5 + '\n' + num6 + '\n' + num7 + '\n' + num8 + '\n')
    for i in inventary:
        outfile.write(str(i))
    outfile.close()


def ENCODE(i):
    infile = open("table.txt", "r")
    alllines = infile.readlines()
    if (i < 7):
        string = alllines[i][0:-1]
    if (i == 7):
        x = alllines[i]
        infile.close()
        return int(x)
    if i == 8:
        string = alllines[i]
        ans = []
        for i in string:
            ans.append(int(i))
        return ans

    x = float(float.fromhex(string))
    infile.close()
    return x


def NEWACS(lastacs, prices):
    choice = random.randint(1, 10)
    f = False
    if choice <= 6:
        f = True

    if f:
        currentAcs = random.triangular(50, lastacs, 500)

    else:
        currentAcs = random.triangular(lastacs, 1000, 500)

    finalAcs = currentAcs

    if len(prices) == 1:
        return (prices[0] + currentAcs) / 2

    if len(prices) >= 2:
        finalAcs = (prices[-1] + prices[-2] + currentAcs) / 3

    return finalAcs

def DRAW_PLOT(prices):
    dates = [i for i in range(1, len(prices) + 1)]
    plt.clear_data()
    plt.theme("clear")
    plt.scatter(dates, prices, marker="x")
    plt.title("GASPROM STOCKS PRICE")
    plt.plot_size(50, 10)
    plt.xfrequency(len(prices))
    plt.show()

def ELEC_PLUS(electricity):
    electricity += random.uniform(1, 500)
    return electricity

def BUY_SOUND():
    winsound.PlaySound('buy2.wav', winsound.SND_FILENAME)

def SELL_SOUND():
    winsound.PlaySound('sell.wav', winsound.SND_FILENAME)

def PAY_ELEC():
    winsound.PlaySound('elec.wav', winsound.SND_FILENAME)

def SAVE_SOUND():
    winsound.PlaySound('save.wav', winsound.SND_FILENAME)

def LOAD_SOUND():
    winsound.PlaySound('load.wav', winsound.SND_FILENAME)

def SHOP_SOUND():
    winsound.PlaySound('shop.wav', winsound.SND_FILENAME)

items = {
    1: {"name": "аркана на сфа", "price": 2500},
    2: {"name": "телевизор", "price": 10000},
    3: {"name": "ноутбук Apelsin Book", "price": 100000},
    4: {"name": "защита от DDOS-атак", "price": 1000000},
    5: {"name": "бугати", "price": 10000000},
    6: {"name": "квартира в майам... в чебоксарах", "price": 15000000}
}