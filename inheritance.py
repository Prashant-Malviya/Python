class Employee:

    company = 'ITC'

    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary} ")
    

class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"out of all the languages here is your language: {self.language}")

class Programmer(Employee,Coder):
    company = "Infotech"

    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language") 

 
p = Programmer()

p.printLanguage()
p.showLanguage()