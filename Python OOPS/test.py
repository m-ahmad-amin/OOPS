class A:
    def a_m(self):
        print('this is A')


class B:
    def b_m(self):
        print('this is B')


class C(A, B):
    def c_m(self):
        print('this is C')
        print(A)

c = C()
c.c_m()
print(C)