from ftplib import FTP
import os
import time
from random import randint
import sys

SLEEPMIN = 1
SLEEPMAX = 15
MAXRANDOMLOOP = 5
#you can choose number of the files in your repository
#each file needs to be represented by file1, file2.... format
FILECOUNT = 1

#remote host ip address
remoteHost=str(sys.argv[1])
#directory for storing downloaded files
localDownloadDirectory=str(sys.argv[2])
#directory for remote upload
remoteUploadDirectory = str(sys.argv[3])
#directory for ftp local current directory
localRepository = str(sys.argv[4])
#directory for ftp remote directory
remoteRepository = str(sys.argv[5])

ftp= None

#ftp.login()

def connect():
	global ftp
	try:
		ftp.voidcmd("NOOP")
	except:
		ftp=FTP(remoteHost)
		ftp.login()

def close():
	global ftp
	if ftp != None:
		ftp.quit()
		

#Download file from ftp server

def downloadFiles(randLoopCount):

	connect()

	ftp.cwd(remoteRepository)

	os.chdir(localDownloadDirectory)

	for i in range(0,randLoopCount):

		randNum = randint(1,FILECOUNT)

		ftp.retrlines('LIST')

		ftp.retrbinary('RETR file%s'% str(randNum), open('file%s'%randNum,'wb').write)

		time.sleep(randint(SLEEPMIN,SLEEPMAX))

	close()

def uploadFiles(randLoopCount):

	connect()

	ftp.cwd(remoteUploadDirectory)

	os.chdir(localRepository)

	for i in range(0,randLoopCount):

		randNum = randint(1,FILECOUNT)

		ftp.retrlines('LIST')

		ftp.storbinary('STOR file%s'% str(randNum), open('file%s'%randNum,'rb'))

		time.sleep(randint(SLEEPMIN,SLEEPMAX))

	close()

while True:
	randNum = randint(0,1)

	randLoopCount = randint(1,MAXRANDOMLOOP)

	if randNum == 0:
		uploadFiles(randLoopCount)
	elif randNum == 1:
		downloadFiles(randLoopCount)
	

