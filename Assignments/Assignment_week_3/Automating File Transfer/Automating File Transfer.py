''' You work at a company that receives daily data files from external partners. These files need to be processed and analyzed, but first, they need to be transferred to the company's internal network.

The goal of this project is to automate the process of transferring the files from an external FTP server to the company's internal network.

Here are the steps you can take to automate this process:

    Use the ftplib library to connect to the external FTP server and list the files in the directory.

    Use the os library to check for the existence of a local directory where the files will be stored.

    Use a for loop to iterate through the files on the FTP server and download them to the local directory using the ftplib.retrbinary() method.

    Use the shutil library to move the files from the local directory to the internal network.

    Use the schedule library to schedule the script to run daily at a specific time.

    You can also set up a log file to keep track of the files that have been transferred and any errors that may have occurred during the transfer process. '''

import ftplib
import os
import shutil
import schedule, time

#Define credentials



def main():
    FTP_HOST = "ftp.dlptest.com"
    FTP_USER = "dlpuser"
    FTP_PASS = "rNrKYTX9g7z3RgJRmxWuGHbeu"
    FTP_PORT = 21
    ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS, FTP_PORT) #Connect to FTP server
    print(ftp.getwelcome()) #Check if connection is successful

    ftp.dir()           #Directory listing
    print(ftp.nlst())   #List files in directory

    #I am going to upload files to the FTP server first in a new folder.

   

    #This will help to upload 4 files to the FTP server if needed. Theses have been created in advance
    # for i in range(1,9):
    #     with open('Automating File Transfer\\files_to_uploaded\\'+'file'+str(i)+'.txt','rb') as f:
    #         ftp.storbinary('STOR file'+str(i)+'.txt', f)

    # print(ftp.nlst())

    #Now let's find the directory where the files will be stored

    directoryName = "FTP_files" 
    if not os.path.exists(directoryName):
        os.mkdir(directoryName)
        print("Directory " , directoryName ,  " Created ")

    #Now let's download the files from the FTP server to the created directory

    for file in ftp.nlst():
        try: 
            with open(os.path.join(directoryName, file), 'wb') as f:
                ftp.retrbinary('RETR ' + file, f.write)
                print("File " , file ,  " downloaded successfully")
        except:
            with open("logFile.txt", "a") as log:
                log.write("File " + file + " did not be downloaded\n")
            print("File " , file ,  " did not be downloaded")  

    
    #Now let's move the files from the local directory to the internal network
    currentDir = os.getcwd()
    sourceDir = "FTP_files"
    sourceDir = os.path.join(currentDir, sourceDir)

    destinationDir = ("Internal Network")
    if not os.path.exists(destinationDir):
        os.mkdir(destinationDir)
        print("Directory " , destinationDir ,  " Created ")

    for file in os.listdir(sourceDir):
        try:
            shutil.move(os.path.join(sourceDir, file), destinationDir)
            print("File " , file ,  " moved successfully")
        except:
            with open("logFile.txt", "a") as log:
                log.write("File " + file + " did not be moved\n")
            print("File " , file ,  " did not be moved")
    
    

# Schedule the script to run daily at 14:30
schedule.every().day.at("14:30").do(main)
# For keeping the script running while waiting for scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)












