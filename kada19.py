class MoneyBox:
    def __init__(self, capacity = 0): # конструктор с аргументом – вместимость копилки
        self.capacity = capacity
        self.value = 0
    def can_add(self, v = 0): 
        return self.value <= (self.capacity-v) # True, если можно добавить v монет, False иначе
    def add(self, v):                           # положить v монет в копилку
        if self.can_add(v=0):
            self.value+=v
class MoneyBox1:
    def __init__(self, capacity = 0): # конструктор с аргументом – вместимость копилки
        self.capacity = capacity
    def can_add(self, v = 0): 
        return (self.capacity >=  v) # True, если можно добавить v монет, False иначе
    def add(self, v):                           # положить v монет в копилку
        if self.can_add(v=0):
            self.capacity-=v
x = MoneyBox(15)
y = MoneyBox1(15)
x.add(5)
y.add(5)
x.add(9)
y.add(9)
x.add(3)
y.add(3)
1+1