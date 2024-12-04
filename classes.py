class Employee:
    name = 'prashant malviya'
    language = 'Python'
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print('Good Morning')

mohan = Employee()
prashant = Employee()

mohan.name = 'mohan solanki'

prashant.name = 'prashant solanki'

# print(prashant.name,prashant.language)

# print(mohan.name,mohan.salary,mohan.language)

mohan.getInfo()
prashant.greet()

