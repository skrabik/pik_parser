from database import DB
from pik_api import pikAPI
from telegram.message import StaticMethods
from config import BOT_TOKEN
from helpers import create_message
import json
from time import time

db = DB().connect()
api = pikAPI()

query = db.select("SELECT pik_id FROM flat")
parsed_flats = {flat[0] for flat in query}


with open('search_params.json', 'r') as f:
    search_params = json.load(f)

start_time = time()
print(f"Начинается парсинг ...")
flats = api.get_flats(params=search_params)
for el in flats:
    if el['id'] not in parsed_flats:
        parsed_flats.add(el['id'])
        db.insert("INSERT INTO flat (pik_id) VALUES ('{}')".format(el['id']))
        StaticMethods.sendText(BOT_TOKEN, '1030879612', create_message(el))
print(f"Сбор данных завершен за {int(time() - start_time)} секунд")


