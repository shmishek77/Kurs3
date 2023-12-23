import json
correct_data = []
data_sorted = []
x = 0

with open("operations.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(data)
print(type(data))

#print(sorted(data, key=itemgetter('date')))

for date in data:
    if 'date' in date:
#        print(date['date'])
        correct_data.append(date)
    else:
        print('key not found')
    #print(date['date'])
#data_sorted = correct_data.sort['date']
print(correct_data, "\n")
#def get_date(data):
#    return data.get('date')
data_sorted = sorted(correct_data, key=lambda x: x["date"], reverse=True)
print(f"data_sorted: {data_sorted} \n")
#data.sort(key=get_date)
#print(data)
for date_sorted in data_sorted:
     if "from" in date_sorted:
         print(date_sorted['state'])
         print(date_sorted['date'])
         print(date_sorted['from'])
         print(date_sorted['to'],"\n")
     else:
         print(date_sorted['state'])
         print(date_sorted['date'])
         print("not found")
         print(date_sorted['to'], "\n")

for i in data_sorted:
    if "date" in i:
        if i["state"] == "EXECUTED":
            print_1 = (f"{i['date'][8:10]}.{i['date'][5:7]}.{i['date'][0:4]} {i['description']}")
            if 'description' in i:
                if i['description'] == "Открытие вклада":
                    print_2 = (f"{i['to'][0:5]}**{i['to'][-5:-1]}")
                    print_4 = ""
                #print_3 = (f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}\n")
                #continue
            if "from" in i:
                if i['from'][0:10] == "MasterCard":
                    print_2 = (f"{i['from'][0:10]} {i['from'][11:15]} {i['from'][16:18]}** **** {i['from'][-5:-1]} -> ")
                if i['from'][0:7] == "Maestro":
                    print_2 = (f"{i['from'][0:7]} {i['from'][11:15]} {i['from'][16:18]}** **** {i['from'][-5:-1]} -> ")
                if i['from'][0:4] == "Счет":
                    print_2 = (f"{i['from'][0:5]}**{i['from'][-5:-1]} -> ")
                if i['from'][0:12] == "Visa Classic":
                    print_2 = (f"{i['from'][0:12]} {i['from'][-15:-11]} {i['from'][-11:-9]}** **** {i['from'][-5:-1]} -> ")
                if i['from'][0:9] == "Visa Gold":
                    print_2 = (f"{i['from'][0:9]} {i['from'][-15:-11]} {i['from'][-11:-9]}** **** {i['from'][-5:-1]} -> ")
                if i['from'][0:3] == "МИР":
                    print_2 = (f"{i['from'][0:3]} {i['from'][-15:-11]} {i['from'][-11:-9]}** **** {i['from'][-5:-1]} -> ")
                if i['from'][0:13] == "Visa Platinum":
                    print_2 = (f"{i['from'][0:13]} {i['from'][-15:-11]} {i['from'][-11:-9]}** **** {i['from'][-5:-1]} -> ")
            if "to" in i:
                if i['to'][0:10] == "MasterCard":
                    print_4 = (f"{i['to'][0:10]} {i['to'][11:15]} {i['to'][-15:-11]} {i['to'][-11:-9]}** **** {i['to'][-5:-1]}")
                if i['to'][0:7] == "Maestro":
                    print_4 = (f"{i['to'][0:7]} {i['to'][11:15]} {i['to'][-15:-11]} {i['to'][-11:-9]}** **** {i['to'][-5:-1]}")
                if i['to'][0:4] == "Счет":
                    print_4 = (f"{i['to'][0:5]}**{i['to'][-5:-1]}")
                if i['to'][0:12] == "Visa Classic":
                    print_4 = (f"{i['to'][0:12]} {i['to'][-15:-11]} {i['to'][-11:-9]}** **** {i['to'][-5:-1]}")
                if i['to'][0:9] == "Visa Gold":
                    print_4 = (f"{i['to'][0:9]} {i['to'][-15:-11]} {i['to'][-11:-9]}** **** {i['to'][-5:-1]}")
                if i['to'][0:3] == "МИР":
                    print_4 = (f"{i['to'][0:3]} {i['to'][-15:-11]} {i['to'][-11:-9]}** **** {i['to'][-5:-1]}")
                if i['to'][0:13] == "Visa Platinum":
                    print_4 = (f"{i['to'][0:13]} {i['to'][-15:-11]} {i['to'][-11:-9]}** **** {i['to'][-5:-1]}")
            print_3 = (f"{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}\n")
        if i["state"] == "CANCELED":
            continue
    print(print_1)
    print(print_2 + print_4)
    print(print_3)

