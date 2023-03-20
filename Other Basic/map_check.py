l=[i for i in range(10)]
newl=str(map(lambda x : x*x*x,l))
print (newl)
print(list(filter(lambda x : x>2,l)))