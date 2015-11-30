__author__ = 'barin.huseyin'

from time import gmtime, strftime


def myTimeGenerator():
    while True:
        yield strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

def getRandomNum(num):
    for i in range(num):
        yield i

def wordList(words):
    for i in words:
        yield i

def main():
    myGen = myTimeGenerator()
    print next(myGen)
    print next(myGen)

    myNumberGen = getRandomNum(10)
    print(next(myNumberGen))
    print(next(myNumberGen))
    print(next(myNumberGen))
    print(next(myNumberGen))

    myWordGen = wordList(("saturn", "uranus", "mars", "venus"))
    print(next(myWordGen))
    print(next(myWordGen))
    print(next(myWordGen))

if __name__ == "__main__": main()