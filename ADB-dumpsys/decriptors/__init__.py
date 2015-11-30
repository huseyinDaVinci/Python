__author__ = 'barin.huseyin'


class Widget(object):
    copyright = "Makaveli"


class Circle(Widget):
    PI = 3.1415

    def __init__(self, radius):
        self.radius = radius
        # self.circumstance = self.radius * 2 * self.PI


    @property
    def circumstance(self):
        return self.radius * 2 * self.PI


def main():
    myCircle = Circle(2)
    myCircle.radius = 3
    print myCircle.circumstance



    # print type(myCircle).mro()
    # print myCircle.copyright
    #


if __name__ == "__main__": main()