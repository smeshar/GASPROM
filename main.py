import random
import time
import math
import sqlite3
import math

def logo():
    print('---')
    print("  ________                                                        ")
    print(" /  _____/  _____      ______ ______   _______    ____     _____  ")
    print("/   \  ___  \__  \    /  ___/ \____ \  \_  __ \  /  _ \   /     \ ")
    print("\    \_\  \  / __ \_  \___ \  |  |_> >  |  | \/ (  <_> ) |  Y Y  \ ")
    print(" \______  / (____  / /____  > |   __/   |__|     \____/  |__|_|  /")
    print("        \/       \/       \/  |__|                             \/ ")

bal = 1000
acs_player = 0
acs = 228.14
inp = 0
k = 0
day = 0
upordown = 1
nextday = True
elecnul = False
elec = 0

def decode():
    outfile = open("table.txt", "w")

    num1 = float.hex(float(bal))
    num2 = float.hex(float(acs_player))
    num3 = float.hex(float(acs))
    num4 = float.hex(float(k))
    num5 = float.hex(float(day))
    num6 = float.hex(float(elec))

    outfile.write(num1 + '\n' + num2 + '\n' + num3 + '\n' + num4 + '\n' + num5 + '\n' + num6 + '\n')
    outfile.close()

def encode(i):
    infile = open("table.txt", "r")
    alllines = infile.readlines()
    if (i != 5): string = alllines[i][0:-1] 
    else: string = alllines[i]
    x = float(float.fromhex(string))
    infile.close()
    return x

def newacs(lastacs, upordown):
    choice = random.randint(1, 10)
    f = False
    if choice <= 2:
        f = True
    
    if f:
        if upordown:
            currentAcs = random.triangular(50, lastacs, 500)
        else:
            currentAcs = random.triangular(lastacs, 1000, 500)

    else:
        if upordown:
            currentAcs = random.triangular(lastacs, 1000, 500)
        else:
            currentAcs = random.triangular(50, lastacs, 500)

    return currentAcs

logo()

while True:
    if elec >= 30000:
        print('--- \n Ваш долг превысил 30000 рублей')
        time.sleep(5)
        print(' Вы проиграли...')
        print(' Спасибо что поиграли в мою игру, можете попробовать заново!')
        print('---')
        time.sleep(2)
        exit()

    if nextday:
        lastacs = acs
        acs = newacs(acs, upordown)
        if not elecnul:
            elec += random.uniform(10, 1000)
        day += 1
        nextday = False

    print(f"--- \n Акции Газпрома стоят на данный момент: {round(acs, 2)} \n---", )
    acs_player = round(k * acs, 2)

    print(f" Ваш баланс: {round(bal, 2)} \n Ваш баланс в акциях: {acs_player} \n День: {day} \n Неоплаченный счет в банке: {round(elec, 2)} \n---")
    print(
        f" Чтобы приобрести акции нажмите 1 \n Чтобы продать акции нажмите 2 \n Чтобы подождать нажмите 3 \n Чтобы оплатить долг нажмите 4 \n Чтобы сохранить игру нажмите 5 \n Чтобы загрузить сохранение нажмите 6 \n---")
    ans = input()

    if ans == "1":
        print(f"--- \n Введите кол-во рублей \n Ваш баланс позволяет купить акции на: {bal} рублей \n---")
        if (bal // acs) < 1:
            print("У вас слишком маленький баланс")
            continue
        inp = float(input())
        if inp > bal:
            print("У вас слишком маленький баланс")
            time.sleep(0.5)
            continue
        time.sleep(0.5)
        print(f"--- \n Покупка выполняется...")
        time.sleep(0.5)
        print(f" Поздравляем, вы купили акции на {inp} рублей по цене {round(acs, 2)}!")
        inp /= acs
        bal -= inp * acs
        k += inp


    if ans == "2":
        print(f"--- \nВведите кол-во рублей на которые вы хотите продать акции")
        print(f"Ваш баланс позволяет продать: {acs_player} рублей \n---")
        if (acs_player // acs) < 1:
            print("У вас нет акций")
            print("Стоит подождать")
            time.sleep(1)
            print()
            continue
        inp = float(input())
        if inp > acs_player:
            print("Вы ввели число большее чем вы можете продать")
            time.sleep(1)
            print()
            continue
        time.sleep(0.5)
        print("--- \n Подготовливаем к продаже...")
        time.sleep(0.5)
        print(" Ищем покупателя...")
        time.sleep(random.triangular(0.5, 4))
        print(f" Поздравляем, вы продали акции на {inp} рублей по цене {round(acs, 2)}!")
        print()
        inp /= acs
        bal += inp * acs
        k -= inp
        acs = newacs(acs, upordown)


    if ans == "3":
        acs = newacs(acs, upordown)
        nextday = True
        continue

    if ans == '4':
        print('---')
        if bal < elec:
            print('Недостаточно средств')
            continue
        time.sleep(0.5)
        print("Переводим деньги...")
        time.sleep(0.5)
        print("Перевод выполнен успешно...")
        bal -= elec
        elec = 0
        nextday = True
        elecnul = True

    if ans == '5':
        print('---')
        print(' Сохраняемся')

        decode()

        time.sleep(1)

    if ans == '6':
        print('---')
        print(' Загружаем сохранение')
        print('---')

        bal = encode(0)
        acs_player = encode(1)
        acs = encode(2)
        k = encode(3)
        day = encode(4)
        elec = encode(5)

        time.sleep(1)

    

    time.sleep(1)
