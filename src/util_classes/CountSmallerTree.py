class CountTreeNode:
    def __init__(self, val, left = None, right = None) -> None:
        self.val = val
        self.num_left = 0
        self.left = left
        self.right = right
    
    def insert(self,val,count = 0) -> int:
        if self is None:
            self = CountTreeNode(val)
            return count
        if val < self.val:
            if self.left is None:
                self.num_left += 1 # We need to increment here to keep a count of left children for use by any nodes added to right side later
                self.left = CountTreeNode(val)
                return count
            else:
                self.num_left += 1 # We need to increment here to keep a count of left children for use by any nodes added to right side later
                return self.left.insert(val, count) 
        if val > self.val:
            count += self.num_left + 1
            if self.right is None:
                self.right = CountTreeNode(val)
                return count
            else:
                return self.right.insert(val, count)
        if val == self.val: 
            count += self.num_left
            if self.right is None:
                self.right = CountTreeNode(val)
                return count
            else:
                return self.right.insert(val, count)