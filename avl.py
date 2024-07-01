
class AVL:
    """Self-balancing AVL trees to guarantee O(log n) search, insert, remove"""
    def __init__(self, item=None, key=None):
        self.item = item
        self.key = key
        self.height = 0
        self.left = None
        self.right = None

    def __iter__(self):
        def gen():
            if self.left:
                yield from self.left
            yield self.item
            if self.right:
                yield from self.right
        return gen()
    
    def get_range(self, lo, hi):
        if lo <= self.key and self.left:
            yield from self.left.get_range(lo, hi)
        if lo <= self.key <= hi:
            yield self.item
        if self.key <= hi and self.right:
            yield from self.right.get_range(lo, hi)
    
    @property
    def balance(self):
        if self.left is None and self.right is None:
            return 0
        elif self.left is None:
            return self.right.height
        elif self.right is None:
            return -self.left.height
        else:
            return self.right.height - self.left.height
    
    def new_height(self):
        if self.left is None and self.right is None:
            self.height = 0
        elif self.left is None:
            self.height = 1 + self.right.height
        elif self.right is None:
            self.height = 1 + self.left.height
        else:
            self.height = 1 + max(self.left.height, self.right.height)

    def copy(self):
        copy = AVL(self.item, self.key)
        copy.left = self.left
        copy.right = self.right
        return copy

    def assume(self, new):
        self.item = new.item
        self.key = new.key
        
    def rotate_right(self):
        self.right = self.copy()
        self.right.left = self.left.right
        self.assume(self.left)
        self.left = self.left.left
        self.right.new_height()
        self.new_height()

    def rotate_left(self):
        self.left = self.copy()
        self.left.right = self.right.left
        self.assume(self.right)
        self.right = self.right.right
        self.left.new_height()
        self.new_height()

    def rebalance(self):
        if self.balance > 1:
            if self.right.balance >= 0:
                self.rotate_left()
            else:
                self.right.rotate_right()
                self.rotate_left()
        elif self.balance < -1:
            if self.left.balance <= 0:
                self.rotate_right()
            else:
                self.left.rotate_left()
                self.rotate_right()
        else:
            self.new_height()

    def find(self, target):
        if self.key < target:
            if self.right:
                return self.right.find(target)
        elif self.key > target:
            if self.left:
                return self.left.find(target)
        else:
            return self.item
    
    def insert(self, new_item, new_key):
        if self.item is None:
            self.item = new_item
            self.key = new_key
            return
        
        if new_key < self.key:
            if self.left is None:
                self.left = AVL(new_item, new_key)
            else:
                self.left.insert(new_item, new_key)
        else:
            if self.right is None:
                self.right = AVL(new_item, new_key)
            else:
                self.right.insert(new_item, new_key)
        
        self.rebalance()
   
    def cut_max(self, parent):
        if self.right is None:
            parent.right = self.left
            return self
        else:
            result = self.right.cut_max(self)
            self.rebalance()
            return result
    
    def remove(self, target, parent=None, prop=None):
        if target < self.key:
            if self.left:
                self.left.remove(target, self, prop)
                self.rebalance()
        elif target > self.key:
            if self.right:
                self.right.remove(target, self, prop)
                self.rebalance()
        elif prop is not None and not prop(self.item):
            if self.left:
                self.left.remove(target, self, prop)
                self.rebalance()
            if self.right:
                self.right.remove(target, self, prop)
                self.rebalance()
        else:
            if self.left and self.right:
                if self.left.right:
                    self.assume(self.left.cut_max(self))
                    self.rebalance()
                else:
                    self.assume(self.left)
                    self.left = self.left.left
                    self.rebalance()
            elif parent is None:
                if self.left:
                    self.assume(self.left)
                    self.right = self.left.right
                    self.left = self.left.left
                    self.rebalance()
                elif self.right:
                    self.assume(self.right)
                    self.left = self.right.left
                    self.right = self.right.right
                    self.rebalance()
                else:
                    del self
            elif self is parent.left:
                parent.left = self.left if self.left else self.right
                parent.rebalance()
            else:
                parent.right = self.left if self.left else self.right
                parent.rebalance()



if __name__ == "__main__":
    from random import randint

    tests = []
    for _ in range(100):
        tree = AVL()
        data = [randint(1,99) for _ in range(100)]
        for x in data:
            tree.insert(x,x)
        for _ in range(20):
            tree.remove(data.pop())
        data.sort()
        tests.append(all(n == x for n,x in zip(tree,data)))
    print(all(tests))
