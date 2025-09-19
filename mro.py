class A:
    def __init__(self):
        print('A')
        super().__init__()

class B:
    def __init__(self):
        print('B')
        super().__init__()

class E(A, B):
    def __init__(self):
        print('E')
        super().__init__()

class C:
    def __init__(self):
        print('C')
        super().__init__()

class D:
    def __init__(self):
        print('D')
        super().__init__()

class F(C, D):
    def __init__(self):
        print('F')
        super().__init__()

class G(E, F):
    def __init__(self):
        print('G')
        super().__init__()

g = G()