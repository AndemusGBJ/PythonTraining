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

#Define credentials

FTP_HOST = "ftp.dlptest.com"
FTP_USER = "dlpuser"
FTP_PASS = "rNrKYTX9g7z3RgJRmxWuGHbeu"


ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS) #Connect to FTP server
print(ftp.getwelcome()) #Check if connection is successful

ftp.dir()           #Directory listing
print(ftp.nlst())   #List files in directory

#I am going to upload files to the FTP server first in a new folder.

#Create a new folder in the directory

ftp.mkd('assignment_week_3')
ftp.cwd('assignment_week_3') #Change directory to the new folder
print(ftp.pwd())

#Let's upload 4 files to the FTP server. Theses have been created in advance
for i in range(1,5):
    with open('file'+str(i)+'.txt','rb') as f:
        ftp.storbinary('STOR file'+str(i)+'.txt', f)

print(ftp.nlst())













