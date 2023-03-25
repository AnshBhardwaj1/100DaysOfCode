class Employee:
    company="Apple"

    def __init__(self,nam,ID) -> None:
        self.name=nam
        self.ID=ID
    def __str__(self) -> str:
        return (f"{self.name}({self.ID}) is in {self.company}")
    
    @classmethod
    def changecomp(cls,newname):
        cls.company=newname
    @classmethod
    def input_is_str(cls,string,spli):
        split_string=string.split(spli)
        return cls(split_string[0],split_string[1])
    @classmethod
    def input_is_list(cls,ls):
        return cls(ls[0],ls[1])
emp1=Employee('ansh',11)
print(emp1)
emp1.changecomp('google')
print(emp1)
inpu="Ansh 2004"
e3=Employee.input_is_str(inpu," ")
print (e3)
inp_ls=['ansh',445]
e4=Employee.input_is_list(inp_ls)
print (e4)