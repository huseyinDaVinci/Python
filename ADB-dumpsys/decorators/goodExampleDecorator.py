__author__ = 'barin.huseyin'

#DECORATORS ARE WONDA...
# for benchmarking
def benchmarkDecorator(func):
    # a decorator taking the time when the function is executed
    def wrapper(*args, **kwargs):
        import time
        from time import gmtime, strftime
        t = time.clock()
        print "Time is:", strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()), "Function name:", func.__name__
        res = func(*args, **kwargs)
        return res
    return wrapper


# for counter
def counterDecorator(func):
    #a decorator counting the function execution
    def wrapper(*args, **kwargs):
        wrapper.counter = +1
        wrapper.count = wrapper.count + 1
        res = func(*args, **kwargs)
        print "{0} has been used: {1}x".format(func.__name__, wrapper.count)
        return res
    wrapper.count = 0
    return wrapper


#for logging
def loggerDecorator(func):
    #a decorator logging the function execution
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print "Coming arguments:", args, "\n", kwargs, "Function name:", func.__name__
        return res
    return wrapper


@counterDecorator
@loggerDecorator
@benchmarkDecorator
def sayHello(name,**kwargs):
    print "Hello",name
    print "Path:",kwargs


@counterDecorator
@loggerDecorator
@benchmarkDecorator
def sumTwoNumbers(num1,num2):
    return num1+num2

@counterDecorator
@loggerDecorator
@benchmarkDecorator
def trial():
    print "I am trying are you kola"

def main():
    sayHello("Jane",path="C:\Temp")

    print "---------------------------------------"
    sumTwoNumbers(5,6)

    print "---------------------------------------"
    trial()

if __name__=="__main__":main()