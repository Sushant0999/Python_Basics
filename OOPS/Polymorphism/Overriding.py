class A:
    def fromA(self, custom_str=None):
        if custom_str:
            print(custom_str, 'CLASS A')
        else:
            print('CLASS A')


objA = A()
objA.fromA(custom_str='VIKING')
objA.fromA()
