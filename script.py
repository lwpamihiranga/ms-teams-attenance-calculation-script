# Python 3.8.3
import csv

with open('new.csv', 'r') as file:
    # reader = csv.reader(file)
    # reader = csv.reader(file, delimiter = '\t')
    reader = csv.DictReader(file, delimiter = '\t')
    # print(sum(1 for row in reader))
    index = 0
    rowList = []
    for row in reader:
        rowList.append(row)
        # print(row)

    for row in rowList:
        if(index == 0):
            prev_name = rowList[index]['Full Name']
            prev_user_action = rowList[index]['User Action']
            prev_timestamp = rowList[index]['Timestamp']
            index += 1
            continue
        else:
            now_name = rowList[index]['Full Name']
            now_user_action = rowList[index]['User Action']
            now_timestamp = rowList[index]['Timestamp']
        # print(name)
        if(prev_name == now_name):
            print("same")

        print(index, rowList[index])
        index += 1