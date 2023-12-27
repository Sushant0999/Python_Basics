from BaseClass import Abstract


class Child(Abstract):
    # From base class
    def baseFun(self):
        print('FROM CHILD')


objChild = Child()
objChild.baseFun()