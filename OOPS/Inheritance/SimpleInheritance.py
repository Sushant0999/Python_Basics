class A:
    def fromA(self):
        print('CLASS A')


class B(A):
    def fromB(self):
        print('CLASS B')

objB = B()
objB.fromA()
objB.fromB()
