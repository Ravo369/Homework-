price_all = 0
ticket_number = int(input("Введите количество билетов"))
for i in range(ticket_number):
    i += 1
    age = int(input(f'Введите возраст для билета № {i}'))
    if age <18:
        price_all += 0
        print ('Билет бесплатный')
    elif age >=18 and age <=25:
        price_all += 990
        print('Билет за 990 руб')
    else:
        price_all += 1390
        print('Билет за 1390 руб')
print("Всего билетов на сумму", price_all, "руб")
if ticket_number >= 3:
    print("Для вас скидка 10%")
    price_all = price_all - price_all/10
print("Итого к оплате",price_all, "руб" )