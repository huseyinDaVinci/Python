

def initializeGlobalParameter():

    global mylist
    mylist=[]

def trialIterators():
    
    
    mylist=[x*x for x in range(4)]   
    
    print mylist
    
    for i in mylist:
        print i
    
    for i in mylist:
        print i
    

def trialGenerators():
    
    mygeneratedList=(x*x for x in range(3))
    
    for i in mygeneratedList:
        print "generator",i
        
    for i in mygeneratedList:
        print "generatorsss",i
    
    print mygeneratedList
    
def __init__():
    print "init",mylist



initializeGlobalParameter()
trialIterators()
trialGenerators()
__init__()

