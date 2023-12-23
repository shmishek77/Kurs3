def date_format(date):
    """возвращает дату в нужном формате"""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"


def from_(item):
    """
    определяем откуда сделан перевод с карты или со счета и возвращаем соответствующую строку
    """
    if "Счет" in item:
        return f"{item[0:5]}**{item[-4:]} ->"
    else:
        return f"{item[:-16]}{item[-16:-12]} {item[-12:-10]}** **** {item[-4:]} ->"


def to(item):
    """
    определяем куда сделан перевод на карту или на счет и возвращаем соответствующую строку
    """
    if "Счет" in item:
        return f"{item[0:5]}**{item[-4:]}"
    else:
        return f"{item[:-16]}{item[-16:-12]} {item[-12:-10]}** **** {item[-4:]}"


def output(sorted_payments, count):
    """выводим на экран нужное количество записей в необходимом виде"""
    counter = 0
    for payment in sorted_payments:
        if counter == count:
            break
        counter += 1
        print(f"{date_format(payment['date'])} {payment['description']}")
        if "from" in payment:
            print(f"{from_(payment['from'])}", end=" ")
        print(f"{to(payment['to'])}")
        print(f"{(payment['operationAmount']['amount'])} {(payment['operationAmount']['currency']['name'])}\n")