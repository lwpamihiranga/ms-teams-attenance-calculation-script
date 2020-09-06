# version: Python 3.8.3
# author: Amith Mihiranga
import csv
from datetime import datetime
with open('input.csv', 'r') as file:
    reader = csv.DictReader(file, delimiter = '\t')
    index = 0
    rowList = []
    nameList = []
    resultList = []
    date = ""
    endtime = ""
    time = input("Enter meeting end time(Default is: 21:15:00): ")
    if(len(time) == 0):
        time = "21:15:00"
    # endtime = "18/08/2020, 21:30:00"
    for row in reader:
        if(index == 0):
            date = row["Timestamp"].split(",")[0]
            name = row["Full Name"] 
            nameList.append(name)
        elif(name != row["Full Name"]):
            name = row["Full Name"]
            nameList.append(name)

        rowList.append(row)
        index += 1
    
    endtime = date + ", " + time
    index = 0
    while index < len(nameList):
        name = nameList[index]

        currentList = []

        for item in rowList:
            if(item["Full Name"] == name):
                currentList.append(item)

        if(len(currentList) == 1):
            timestamp = currentList[0]["Timestamp"]
            # time = datetime.strptime(timestamp, "%m/%d/%Y, %I:%M:%S %p")
            time = datetime.strptime(timestamp, "%d/%m/%Y, %H:%M:%S")
            end_time = datetime.strptime(endtime, "%d/%m/%Y, %H:%M:%S")

            duration = end_time - time
            resultList.append({"Full Name": name, "Duration": str(duration)})
        elif(len(currentList) % 2 != 0):
            duration -= duration
            inner_index = 0
            while inner_index < len(currentList):
                if(inner_index == len(currentList) - 1):
                    joined_time = datetime.strptime(currentList[inner_index]["Timestamp"], "%d/%m/%Y, %H:%M:%S")
                    end_time = datetime.strptime(endtime, "%d/%m/%Y, %H:%M:%S")
                    duration = duration + (end_time - joined_time)
                else:
                    joined_time = datetime.strptime(currentList[inner_index]["Timestamp"], "%d/%m/%Y, %H:%M:%S")
                    left_time = datetime.strptime(currentList[inner_index + 1]["Timestamp"], "%d/%m/%Y, %H:%M:%S")
                    duration = duration + (left_time - joined_time)
                inner_index += 2
            resultList.append({"Full Name": name, "Duration": str(duration)})
        else:
            duration -= duration
            inner_index = 0
            while inner_index < len(currentList):
                joined_time = datetime.strptime(currentList[inner_index]["Timestamp"], "%d/%m/%Y, %H:%M:%S")
                left_time = datetime.strptime(currentList[inner_index + 1]["Timestamp"], "%d/%m/%Y, %H:%M:%S")
                duration += (left_time - joined_time)
                inner_index += 2
            resultList.append({"Full Name": name, "Duration": str(duration)})
        index += 1

year = date.split("/")[2] + "-"
month = date.split("/")[1] + "-"
day = date.split("/")[0] + "-"
result_filename = year + month + day + "AttendanceResults.csv"

input_msg = "Your result file will be stored as " + result_filename + ". If you wish to change the name, please enter a name or press enter to skip: "
user_defined_filename = input(input_msg)
if(len(user_defined_filename) != 0):
    result_filename = user_defined_filename + ".csv"

with open(result_filename,'w', newline='') as csvfile:
    csv_columns = ['Full Name','Duration']
    csvwriter = csv.DictWriter(csvfile, csv_columns)
    csvwriter.writeheader()
    csvwriter.writerows(resultList)

print("Result file generated as ", result_filename)