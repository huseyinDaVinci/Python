__author__ = 'makaveli'
import pysftp
import SftpModule
import os


global files
files=[]



class SftpFile():

    def __init__(self,mac,ip,date):

        self.mac=mac
        self.ip=ip
        self.date=date


    def getFileInfo(self):
        return self.mac+self.ip+self.date

    def getMac(self):
        return self.mac

    def getIp(self):
        return self.ip


    def getDate(self):
        return self.date

def initializeVariables():

    global data
    data = set()
    global dirPath
    dirPath="/mnt/x/"




def search(searchedWord):



    if files is not None:

        for file in files:

            if str(searchedWord) in file.getFileInFo:
                print ("Your file is this:", searchedWord)




def openConnectionWithDefault():
    global srv
    # open the connection here.
    srv = pysftp.Connection(host="10.x.x.x", username="x",
                            password="x!")

def openConnectionWithCertificate(certificate):
    global srv
    srv=pysftp.Connection('hostname', username='me', private_key=certificate)
def openConnectionWithConfig(configInfo):
    configInfo = {'host':'x', 'username':'x', 'password':'x!', 'port':x}
    global srv
    srv=pysftp.Connection(**configInfo)
def putFile(filename):
    pass

def getFile(path,filename):



    srv.get(path+filename, preserve_mtime=True)


def getDirectory(remotePath,localPath):


    destPath=localPath+"/TabletLogs/"



    if os._exists(destPath):  # if path is available do not create anymore
        os.mkdir(destPath)

    srv.get_d(remotePath,destPath,preserve_mtime=True)

def closeConnection():
    # Closes the connection

    if srv is not None:
        srv.close()

def showDirectoryContent():

         # Get the directory and file listing
    data = srv.listdir(dirPath)

    try:
        # Prints out the directories and files, line by line
        for i in data:


            #getFile(dirPath,str(i))
            row=str(i).split("_")
            row[-1]=(row[-1].split("."))[0]
            s= SftpModule.SftpFile(row[0],row[1],row[2])
            files.append(s)
    except Exception as e:
        print ("Error occurs",e.message)

    for j in files:
        print (j.getFileInfo())

def showMenu():
    flag = True

    while (flag):
        choise = raw_input("MAC(1), IP(2), DATE(3)  Exit (-1): ")
        choices=['1','2','3','-1','4']

        if (choise not in choices):
            print ("Please enter a proper option(1,2,3,4 or -1)")
        elif choise=='-1':
            flag = True
        elif choise=='4':
            word=raw_input("Type to search:")
            options[choise](str(word))
        else:

            options[choise]()


    print ("Chosen option",choise)



def showMacs():

    print ("welcome show macs")

    if files is not None:
        for f in files:
            print (f.getMac());

def showIps():
    print ("welcome show ips")
    if files is not None:
        for f in files:
            print (f.getIp());

def showDates():
    print ("welcome show dates")
    if files is not None:

        for f in files:
            print (f.getDate());

def main():

    initializeVariables()

    openConnectionWithDefault()
    showDirectoryContent()
    showMenu()
    getDirectory(dirPath,"/home/makaveli")

    #showDirectoryContent()
    #closeConnection()


    closeConnection()

options={'1':showMacs,'2':showIps,'3':showDates,'4':search}

if __name__ == "__main__": main()
