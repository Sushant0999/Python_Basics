class A:
    def fromA(self):
        print('CLASS A')


class B(A):
    def fromB(self):
        print('CLASS B')


class C(A):
    def fromC(self):
        print('CLASS C')


objB = B()
objC = C()

print('OBJ B')
objB.fromB()
objB.fromA()


print('OBJ C')
objC.fromA()
objC.fromC()