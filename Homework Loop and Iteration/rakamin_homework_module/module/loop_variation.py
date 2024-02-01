
class LoopTriangle:
    def __init__(self,height = 5):
        self.height = height
        
    def process(self):
        print("Loop Segitiga")
        for i in range(1, self.height + 1):
            spasi = " " * (self.height - i)
            bintang = "*" * (2 * i - 1)
            print(spasi + bintang)
    
class LoopSquare:
    def __init__(self,size = 5):
        self.size = size
        
    def process(self):
        print("Loop Persegi")
        for i in range(self.size):
            for j in range(self.size):
                print("*", end=" ")
            print()