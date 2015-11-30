__author__ = 'barin.huseyin'
import time
import datetime
import thread,threading


def trash():
    for i in range(3):
        print ('Tick')
        time.sleep(1)
        print ('Tock')
        time.sleep(1)

    time.sleep(5)

    print "5 seconds were passed"



def washFace():
    print "Wash your face after 2 seconds"
    time.sleep(2)
    print "I washed up"

def wakeUp():

    print "Wake up after 5 seconds"
    time.sleep(5)
    print "I waked up body"


def showDate():
    todayDate = datetime.datetime.now()
    print todayDate
    print datetime
    # specificDate=datetime.datetime(2015,)


def pauseTimerInAGivenPeriod():
    startedTime = datetime.datetime.now()

    myFinalTime = datetime.datetime(2015, 5, 4, 11, 2, 10)



    #okeyto
    while datetime.datetime.now() < myFinalTime:
        print "Current Time:",datetime.datetime.now()
        print "My Final Time",myFinalTime
        print "Started Time",startedTime
        print "Tic"
        time.sleep(30)
        print "Toc"
        time.sleep(30)

    print "finished time", datetime.datetime.now()





def main():
    pauseTimerInAGivenPeriod()

    threadObj=threading.Thread(wakeUp())
    threadObj.start()

    threadObj1=threading.Thread(washFace())
    threadObj1.start()

if __name__ == "__main__": main()