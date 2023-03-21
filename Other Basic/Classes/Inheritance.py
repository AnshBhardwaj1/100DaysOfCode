class employee :
    def __init__(self,name_,id_):
        self.name=name_
        self.id=id_
    
    def info (self):
        print (f'ID no {self.id} is {self.name}')
    
class engineer (employee):
    def __init__(self, name_, id_,lang_):
        employee().__init__(self.name, self.id,lang_)

e1=employee('ansh',234)
e1.info()
e2=engineer('rohan',267,'python')
#e2.lang='python'
e2.info()