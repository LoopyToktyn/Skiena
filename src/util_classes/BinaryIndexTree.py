class BinaryIndexTree:
    def __init__(self, size) -> None:
        self.bit = [0] * (size + 1)
        self.size = size

    def update(self,index,val) -> None:
        while index < self.size:
           self.bit[index] += val
           index += index & -index

    def query(self, index) -> int:
        res = 0
        while index > 0:
            res += self.bit[index]
            index -= index & -index
        return res
    


        