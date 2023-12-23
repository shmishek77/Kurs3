import json
correct_data = []
data_sorted = []

with open("src/operations.json", "r", encoding="utf-8") as f:
    data = json.load(f)

for date in data:
    if 'date' in date:
        correct_data.append(date)

data_sorted = sorted(correct_data, key=lambda x: x["date"], reverse=True)


def last_5(input_data):
    counter = 0
    for i in data_sorted:
        if "date" in i:
            if i["state"] == "EXECUTED":
                counter += 1
                print_1 = f"{i['date'][8:10]}.{i['date'][5:7]}.{i['date'][0:4]} {i['description']}"
                if 'description' in i:
                    if i['description'] == "Открытие вклада":
                        print_2 = "-> "
                if "from" in i:
                    if i['from'][0:10] == "MasterCard":
                        print_2 = f"{i['from'][0:10]} {i['from'][11:15]} {i['from'][16:18]}** **** {i['from'][-5:-1]} -> "
                    if i['from'][0:7] == "Maestro":
                        print_2 = f"{i['from'][0:7]} {i['from'][11:15]} {i['from'][16:18]}** **** {i['from'][-5:-1]} -> "
                    if i['from'][0:4] == "Счет":
                        print_2 = f"{i['from'][0:5]}**{i['from'][-5:-1]} -> "
                    if i['from'][0:12] == "Visa Classic":
                        print_2 = f"{i['from'][0:12]} {i['from'][-15:-11]} {i['from'][-11:-9]}** **** {i['from'][-5:-1]} -> "
                    if i['from'][0:9] == "Visa Gold":
                        print_2 = f"{i['from'][0:9]} {i['from'][-15:-11]} {i['from'][-11:-9]}** **** {i['from'][-5:-1]} -> "
                    if i['from'][0:3] == "МИР":
                        print_2 = f"{i['from'][0:3]} {i['from'][-15:-11]} {i['from'][-11:-9]}** **** {i['from'][-5:-1]} -> "
                    if i['from'][0:13] == "Visa Platinum":
                        print_2 = f"{i['from'][0:13]} {i['from'][-15:-11]} {i['from'][-11:-9]}** **** {i['from'][-5:-1]} -> "
                if "to" in i:
                    if i['to'][0:10] == "MasterCard":
                        print_3 = f"{i['to'][0:10]} {i['to'][11:15]} {i['to'][-15:-11]} {i['to'][-11:-9]}** **** {i['to'][-5:-1]}"
                    if i['to'][0:7] == "Maestro":
                        print_3 = f"{i['to'][0:7]} {i['to'][11:15]} {i['to'][-15:-11]} {i['to'][-11:-9]}** **** {i['to'][-5:-1]}"
                    if i['to'][0:4] == "Счет":
                        print_3 = f"{i['to'][0:5]}**{i['to'][-5:-1]}"
                    if i['to'][0:12] == "Visa Classic":
                        print_3 = f"{i['to'][0:12]} {i['to'][-15:-11]} {i['to'][-11:-9]}** **** {i['to'][-5:-1]}"
                    if i['to'][0:9] == "Visa Gold":
                        print_3 = f"{i['to'][0:9]} {i['to'][-15:-11]} {i['to'][-11:-9]}** **** {i['to'][-5:-1]}"
                    if i['to'][0:3] == "МИР":
                        print_3 = f"{i['to'][0:3]} {i['to'][-15:-11]} {i['to'][-11:-9]}** **** {i['to'][-5:-1]}"
                    if i['to'][0:13] == "Visa Platinum":
                        print_3 = f"{i['to'][0:13]} {i['to'][-15:-11]} {i['to'][-11:-9]}** **** {i['to'][-5:-1]}"
                print_4 = f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}\n"
            if i["state"] == "CANCELED":
                continue
            if counter > 5:
                break

        print(print_1)
        print(print_2 + print_3)
        print(print_4)
