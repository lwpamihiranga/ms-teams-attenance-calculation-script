# Python Script to Calculate the Duration a attendee stayed in a Microsoft Teams Meeting

By using this script you can calculate the duration a member stayed in a microsoft teams by using the downloaded attendee list file
in microsoft teams. 

[Click here to watch video demo](https://youtu.be/IVKiwC73FRs)

Need to know how to download the attendee list? [Click here](https://support.microsoft.com/en-ie/office/download-attendance-reports-in-teams-ae7cf170-530c-47d3-84c1-3aedac74d310)

### Limitations and Things You Should Aware of

-  When downloading the attendance list it will give you the times, beginning from the your last joined time. Let's say that you start the meeting at 7pm. Then at 8 you will leave for something and then come back again at 8.05pm. Then when you are dowloading the attendance list at 9pm the minimum starting time in the sheet is 8.05 because your last joined time is 8.05. To resolve that my suggestion is to download two lists and then we can generate the final list. We can modify the script to add a manual starting time, but then if anyone who was there before the meeting left and not joined again after the break their data will be lost. This not related to the script a lot. Since I noticed it I thought it is good to inform

- In the downloaded attendance list there is no final end time. In the list there is only one entry for some member as joined. That is they have joined to the session and has never left till the attendance downloaded time. So basically it says they were in the workshop whole time. To calculate there duration I gave the user to enter a end time for the meeting. I set the default end time as 21.10 because this script is generate to calculate the attendance list of a workshop that happens 19.00 to 21.00. If we enter without entering a end time it will consider the default value for calculations. *Feel free to change the default time to your wish* :wink:

- For the input file you can give the absolute path to the downloaded file. If not you can copy the attendance file to the same folder as the script and give the name correctly.

- The script will name the result file with a meaningful name in same folder where script is in. But it you want you can change the name also when prompt or you can simply skip by pressing enter.

- The *python version* used is **3.8.3**. This should work in **>=8.3** without any error. There are some changes in the csv module that I have used in this script to read the file. But I think it should work in the previous versions as well. If you have a previous python version and any error occurs let me know after testing or feel free to open an issue.

- The timestamps formats are used according to the `"%d/%m/%Y, %H:%M:%S"     # 18/08/2020, 18:57:55 --> Date/Month/Year, HH:MM:SS` format. If there's any change it can be configured easily. You can easily find the format in the top of the script.

- For the issue mentioned in point (1), for now we can generate two lists and copy one list data to the other one manually.