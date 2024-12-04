class Employee: 
    def __init__(self):
        print('contructor of employee')
    a = 1

class Programmer(Employee):
    def __init__(self):
        print('constructor of programmer')
    b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print('constructor of manager')
    c = 3


m = Manager()
print(m)