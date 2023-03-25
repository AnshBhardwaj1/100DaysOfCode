class Emp :
    companyname='Apple'
    def __init__(self,ID,name) -> None:
        self.ID=ID
        self.name=name
    def info(self):
        print (f"Name of {self.ID} is {self.name} and compnay is {self.companyname}")

emp1=Emp(112,'Ansh')
emp1.info()
emp1.companyname="google"
emp1.info()
emp2=Emp(113,'rohan')
emp2.info()