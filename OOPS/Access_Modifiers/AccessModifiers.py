class A():
    # Protected
    _protectedA = 'PROTECTED FROM A'
    # Private
    __privateA = 'PRIVATE FROM A'
    # Public
    publicA = 'PUBLIC FROM A'


class B(A):
    # Protected
    _protectedB = 'PROTECTED FROM B'
    # Private
    __privateB = 'PRIVATE FROM B'
    # Public
    publicB = 'PUBLIC FROM B'


objA = A()
print(objA.publicA)

# In python only public attributes can be access via objects. Not private nor protected
