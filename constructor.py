class Employee:
    company="Google"

    def __init__(self,name,salary,subunit):
        self.name=name
        self.salary=salary
        self.subunit=subunit
        print("Profile Created!!")

    def getDetails(self):
        print(f"Name is {self.name}")
        print(f"Salary is {self.salary}")
        print(f"Subunit is {self.subunit}")

anmol=Employee("Anmol",100000,"YouTube")
anmol.getDetails()            
