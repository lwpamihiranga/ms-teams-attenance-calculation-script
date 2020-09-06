# version: Python 3.8.3
# author: Amith Mihiranga
import csv
from datetime import datetime
import codecs

NAME_COLUMN_NAME = "Full Name"              
ACTION_COLUMN_NAME = "Action"               
TIMESTAMP_COLUMN_NAME = "Timestamp"         
DURATION_COLUMN_NAME = "Duration"           
TIMESTAMP_FORMAT = "%d/%m/%Y, %H:%M:%S"     # 18/08/2020, 18:57:55 --> Date/Month/Year, HH:MM:SS
INPUT_FILE_NAME = "sample.csv"
OUTPUT_FILE_NAME_SUFFIX = "AttendanceResults.csv"
READ_ENCODING_FORMAT = "utf-8"

user_given_file = input("Enter path to the input file, press enter to skip: ")
if(len(user_given_file) != 0):
    INPUT_FILE_NAME = user_given_file
else:
    print("You skipped entering a file path. There should be an input.csv file in the script directory with your data. Otherwise the script will fail!")

# if input file contains null bytes the file need to be read in utf-16 encoding
if '\0' in open(INPUT_FILE_NAME).read():
    READ_ENCODING_FORMAT = 'utf-16'

with codecs.open(INPUT_FILE_NAME, 'rU', READ_ENCODING_FORMAT) as file:
    reader = csv.DictReader(file, delimiter = '\t')
    index = 0
    rowList = []
    nameList = []
    resultList = []
    date = ""
    endtime = ""
    time = input("Enter meeting end time(Default is: 21:15:00): ")
    if(len(time) == 0):
        time = "21:15:00"   # SET 21:15:00 as Default End Time if user does not enter a time
    for row in reader:
        if(index == 0):
            date = row[TIMESTAMP_COLUMN_NAME].split(",")[0]
            name = row[NAME_COLUMN_NAME] 
            nameList.append(name)
        elif(name != row[NAME_COLUMN_NAME]):
            name = row[NAME_COLUMN_NAME]
            nameList.append(name)

        rowList.append(row)
        index += 1
    
    endtime = date + ", " + time
    index = 0
    while index < len(nameList):
        name = nameList[index]

        currentList = []

        for item in rowList:
            if(item[NAME_COLUMN_NAME] == name):
                currentList.append(item)

        if(len(currentList) == 1):
            timestamp = currentList[0][TIMESTAMP_COLUMN_NAME]
            time = datetime.strptime(timestamp, TIMESTAMP_FORMAT)
            end_time = datetime.strptime(endtime, TIMESTAMP_FORMAT)

            duration = end_time - time
            resultList.append({NAME_COLUMN_NAME: name, DURATION_COLUMN_NAME: str(duration)})
        elif(len(currentList) % 2 != 0):
            duration -= duration
            inner_index = 0
            while inner_index < len(currentList):
                if(inner_index == len(currentList) - 1):
                    joined_time = datetime.strptime(currentList[inner_index][TIMESTAMP_COLUMN_NAME], TIMESTAMP_FORMAT)
                    end_time = datetime.strptime(endtime, TIMESTAMP_FORMAT)
                    duration = duration + (end_time - joined_time)
                else:
                    joined_time = datetime.strptime(currentList[inner_index][TIMESTAMP_COLUMN_NAME], TIMESTAMP_FORMAT)
                    left_time = datetime.strptime(currentList[inner_index + 1][TIMESTAMP_COLUMN_NAME], TIMESTAMP_FORMAT)
                    duration = duration + (left_time - joined_time)
                inner_index += 2
            resultList.append({NAME_COLUMN_NAME: name, DURATION_COLUMN_NAME: str(duration)})
        else:
            duration -= duration
            inner_index = 0
            while inner_index < len(currentList):
                joined_time = datetime.strptime(currentList[inner_index][TIMESTAMP_COLUMN_NAME], TIMESTAMP_FORMAT)
                left_time = datetime.strptime(currentList[inner_index + 1][TIMESTAMP_COLUMN_NAME], TIMESTAMP_FORMAT)
                duration += (left_time - joined_time)
                inner_index += 2
            resultList.append({NAME_COLUMN_NAME: name, DURATION_COLUMN_NAME: str(duration)})
        index += 1

# Assumption - Timestamp date part as in 18/08/2020(Day/Month/Year) format
year = date.split("/")[2] + "-"
month = date.split("/")[1] + "-"
day = date.split("/")[0] + "-"
result_filename = year + month + day + OUTPUT_FILE_NAME_SUFFIX  # 2020-08-18-AttendanceResults.csv

input_msg = "Your result file will be stored as " + result_filename + ". If you wish to change the name, please enter a name or press enter to skip: "
user_defined_filename = input(input_msg)
if(len(user_defined_filename) != 0):
    result_filename = user_defined_filename + ".csv"

with open(result_filename, 'w', newline='') as result_csv_file:
    result_csv_columns = [NAME_COLUMN_NAME, DURATION_COLUMN_NAME]
    csvwriter = csv.DictWriter(result_csv_file, result_csv_columns)
    csvwriter.writeheader()
    csvwriter.writerows(resultList)

print("\nResult file generated as ", result_filename)
