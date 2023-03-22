class employee :
    def __init__(self,name_,id_):
        self.name=name_
        self.id=id_
    
    def info (self):
        print (f'ID no {self.id} is {self.name}')
    
class engineer (employee):
    def showlang(self):
        return 'my lang is python'

e1=employee('ansh',234)
e1.info()
e2=engineer('rohan',267)
e2.showlang()
e2.info()