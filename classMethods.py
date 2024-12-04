class Employee:
    a = 1
    def show():
        print(f"the value of a is {self.a}")

e = Employee()
e.a = 45

e.show()