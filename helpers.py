def create_message(flat):
    res = ""
    res += "Цена: " + str(flat['price']) + " рублей" + "\n"
    res += "Комиссия: " + str(int((float(flat['price']) / 100)) * float(flat['comission']))  + " рублей" + "\n"
    res += "Адрес: " + flat['address'] + "\n"
    try:
        res += "Метро: " + flat['metro']['name'] + "\n"
        res += "Пешком: " + flat['metro']['walk'] + " мин" + "\n"
    except:
        pass
    res += flat['photos'][0] + "\n"
    res += 'https://pik-arenda.ru/flats/{}'.format(flat['id'])
    return res