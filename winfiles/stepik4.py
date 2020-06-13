class MoneyBox:
    def __init__(self, capacity = 0):
        self.capacity = capacity
    def can_add(self, v = 0): 
        if v <= (self.capacity):
            return True
        else:
            return False
    def add(self, v = 0):
        if self.can_add(v):
            self.capacity-=v