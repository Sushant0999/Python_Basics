class A:
    def fromA(self):
        print('CLASS A')


class B(A):
    def fromB(self):
        print('CLASS B')


class C(A):
    def fromC(self):
        print('CLASS C')


class D(B, C):
    def fromD(self):
        print('CLASS D')


objD = D()
objD.fromA()
objD.fromB()
objD.fromC()
objD.fromD()
