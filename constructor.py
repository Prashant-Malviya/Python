class Employee:
    language = 'python'
    salary = 1200000
    
         #dunder methods which is automatically called
    def __init__(self,name,salary,language):

        self.name = name
        self.salary = salary
        self.language = language
        print('I am creating an object')

    def getInfo(self):
        print(f"Hi I am {self.name}. And I am earning {self.salary} annually")


krishna = Employee('krishna',2000000,'javascript')

krishna.getInfo()
