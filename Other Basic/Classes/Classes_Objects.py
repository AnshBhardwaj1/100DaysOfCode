class persom_info:
    name='You have bot entered this info yet'
    age='You have bot entered this info yet'
    job='You have bot entered this info yet'
    def inofo(self):
        print (f" {self.name} is {self.age} and is a {self.job}")

first=persom_info()
first.name=("ansh")
first.age=(18)
first.job=("software engineer")
print (first.inofo())