class A:
    def fun(self):
        print('CLASS A')


class B:
    def fun(self, str):
        print(str, 'CLASS B')


objA = A()
objB = B()
objB.fun('VIKING')
objA.fun()
