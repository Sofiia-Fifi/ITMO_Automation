class A:

    def __init__(self, x=10):
        self.x = x

class B(A):
    
    def __init__(self):
        super().__init__()
        self.y = self.x + 5

b = B()
print(b.y)