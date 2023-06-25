import random
import time

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
inventary = []


def decode():
    global bal, acs_player, acs, inp, k, day, upordown, nextday, elecnul, elec, inventary
    
    with open('table.txt', 'w') as file:
        num1 = float.hex(float(bal))
        num2 = float.hex(float(acs_player))
        num3 = float.hex(float(acs))
        num4 = float.hex(float(k))
        num5 = float.hex(float(day))
        num6 = float.hex(float(elec))

        file.write(f'{num1}\n{num2}\n{num3}\n{num4}\n{num5}\n{num6}\n{inventary}')

def encode(i):
    global bal, acs_player, acs, inp, k, day, upordown, nextday, elecnul, elec, inventary

    with open('table.txt', 'r') as file:
        alllines = file.readlines()
        string = alllines[i].strip()
        x = float.fromhex(string)
    return x

def encode_inv():
    global bal, acs_player, acs, inp, k, day, upordown, nextday, elecnul, elec, inventary
    
    with open('table.txt', 'r') as file:
        alllines = file.readlines()
        curinv = alllines[-1:]
    return curinv

def newacs(lastacs, upordown):
    global bal, acs_player, acs, inp, k, day, nextday, elecnul, elec, inventary

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

def buyacs():
    global bal, acs_player, acs, inp, k, day, upordown, nextday, elecnul, elec, inventary

    print(f"--- \n Введите кол-во рублей \n Ваш баланс позволяет купить акции на: {bal} рублей \n---")
    if (bal // acs) < 1:
        print("У вас слишком маленький баланс")
        time.sleep(0.5)
        return

    inp = float(input())

    if inp < 0:
        print('Вы не можете купить отрицательное кол-во акций')
        time.sleep(0.5)
        return

    if inp > bal:
        print("У вас слишком маленький баланс")
        time.sleep(0.5)
        return

    time.sleep(0.5)
    print(f"--- \n Покупка выполняется...")
    time.sleep(0.5)
    
    if not "DDOS_Shield" in inventary:
        hackers = random.randint(0, 10000)
        hackers /= 100
        if hackers > inp:
            hackers = inp

        print(f"\n Хакеры взломали биржу и ограбили вас на {hackers} рубля")
        print(f" Купите защиту от DDOS-атак за 1.000.000 в магазине\n")
    print(f" Поздравляем, вы купили акции на {inp - hackers} рублей по цене {round(acs, 2)}!")

    inp -= hackers
    inp /= acs
    bal -= inp * acs
    k += inp

def sellacs():
    global bal, acs_player, acs, inp, k, day, upordown, nextday, elecnul, elec, inventary
    
    print(f"--- \nВведите кол-во рублей на которые вы хотите продать акции")
    print(f"Ваш баланс позволяет продать: {acs_player} рублей \n---")

    # Был баг, в котором нельзя было продать акции
    # if (acs_player // acs) < 1:
    #     print("У вас нет акций")
    #     print("Стоит подождать")
    #     time.sleep(1)
    #     print()
    #     return

    inp = float(input())
    if inp > acs_player:
        print("Вы ввели число большее чем вы можете продать")
        time.sleep(1)
        print()
        return

    if inp < 0:
        print('Вы не можете продать отрицательное кол-во акций')
        time.sleep(0.5)
        print()
        return

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

def newday():
    global bal, acs_player, acs, inp, k, day, upordown, nextday, elecnul, elec, inventary
    
    acs = newacs(acs, upordown)
    nextday = True
    return

def payelec():
    global bal, acs_player, acs, inp, k, day, upordown, nextday, elecnul, elec, inventary

    print('---')
    if bal < elec:
        print('Недостаточно средств')
        return
    time.sleep(0.5)
    print("Переводим деньги...")
    time.sleep(0.5)
    print("Перевод выполнен успешно...")
    bal -= elec
    elec = 0
    nextday = True

def save():
    global bal, acs_player, acs, inp, k, day, upordown, nextday, elecnul, elec, inventary

    print('---')
    print(' Сохраняемся')
    decode()

    time.sleep(0.5)

def loadsave():
    global bal, acs_player, acs, inp, k, day, upordown, nextday, elecnul, elec, inventary
    
    print('---')
    print(' Загружаем сохранение')
    print('---')

    bal = encode(0)
    acs_player = encode(1)
    acs = encode(2)
    k = encode(3)
    day = encode(4)
    elec = encode(5)
    inventary = encode_inv()

    time.sleep(0.5)

def shop():
    global bal, acs_player, acs, inp, k, day, upordown, nextday, elecnul, elec, inventary
    
    items = {
        1: {"name": "аркана на сфа", "price": 2500},
        2: {"name": "телевизор", "price": 10000},
        3: {"name": "ноутбук Apelsin Book", "price": 100000},
        4: {"name": "защита от DDOS-атак", "price": 1000000},
        5: {"name": "бугати", "price": 10000000},
        6: {"name": "квартира в майам... в чебоксарах", "price": 15000000}
    }

    print('---')
    print('МАГАЗИН DИS')
    print('Доступные товары:')
    for item_id, item_info in items.items():
        print(f' {item_id}. {item_info["name"]} - {item_info["price"]} рублей')
    print('---')

    while True:
        goods = int(input('Чтобы выбрать товар, напишите его номер: '))
        if goods not in items:
            print("Такого продукта нет.")
            continue

        if bal < items[goods]["price"]:
            print(f'Недостаточно средств. Требуется {items[goods]["price"]} рублей.')
            continue

        print('---')
        print(f'Вы приобрели {items[goods]["name"]}!')
        bal -= items[goods]["price"]
        inventary.append(items[goods]["name"])
        nextday = True
        break

def main():
    global bal, acs_player, acs, inp, k, day, upordown, nextday, elecnul, elec, inventary

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
        elec += random.uniform(10, 1000)
        day += 1
        nextday = False

    print(f"--- \n Акции Газпрома стоят на данный момент: {round(acs, 2)} \n---", )
    acs_player = round(k * acs, 2)

    print(f" Ваш баланс: {round(bal, 2)} \n Ваш баланс в акциях: {acs_player} \n День: {int(day)} \n Неоплаченный счет в банке: {round(elec, 2)} \n Купленные приколюхи: ", end="")
    print(*inventary)
    print(' \n---')
    print(f" Чтобы приобрести акции нажмите 1 \n Чтобы продать акции нажмите 2 \n Чтобы подождать нажмите 3 \n Чтобы оплатить долг нажмите 4 \n Чтобы сохранить игру нажмите 5 \n Чтобы загрузить сохранение нажмите 6 \n Чтобы зайти в магазин нажмите 7 \n---")
    ans = input()

    if ans == "1":  buyacs()
    if ans == "2":  sellacs()
    if ans == "3":  newday()
    if ans == '4':  payelec()
    if ans == '5':  save()
    if ans == '6':  loadsave()
    if ans == '7':  shop()

logo()

while True:
    main()
    time.sleep(1)
