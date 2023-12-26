class A:
    def fromA(self):
        print('CLASS A')

class B(A):
    def fromB(self):
        print('CLASS B')

class C(B):
    def fromC(self):
        print('CLASS C')

objC = C()
objC.fromA()
objC.fromB()
objC.fromC()
