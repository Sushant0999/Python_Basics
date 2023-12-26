class A:
    def fromA(self):
        print('CLASS A')


class B:
    def fromB(self):
        print('CLASS B')


class C(A, B):
    def fromC(self):
        print('CLASS C')


objC = C()
objC.fromA()
objC.fromB()
objC.fromC()
