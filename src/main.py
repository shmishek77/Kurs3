from src.functions import *  #импортируем все функции из файла function.py
import json #импортируем json
correct_data = []
executed_payments = []


#получаем список операций из файла operations.json
with open("operations.json", "r", encoding="utf-8") as f:
    data = json.load(f)


#удаляем пустые строки из списка
for date in data:
    if 'date' in date:
        correct_data.append(date)

#удаляем отмененные платежи из списка
for item in correct_data:
    if item["state"] == "EXECUTED":
        executed_payments.append(item)


#сортируем список по дате
sorted_payments = sorted(executed_payments, key=lambda x: x["date"], reverse=True)


#выводим на экран последние пять выполненных платежей
output(sorted_payments, 5)