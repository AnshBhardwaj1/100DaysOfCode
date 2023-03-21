class person:
    def __init__(self,n):
        self.value=n
    
    def info(self):
        print (f'Value of your number is {self.value}')

    @property
    def cube (self):
        return (self.value**2)
    
    @cube.setter
    def naya_num_par_aadha (self,newnum):
        self.value=newnum/2
aa=person(5)
aa.info()
print (aa.cube)
aa.info()
aa.naya_num_par_aadha=78
aa.info()      
