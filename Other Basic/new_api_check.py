import bs4
import requests
source=requests.get("https://instagram-username.firebaseapp.com/check?username=AWESOME.USERNAME")
link=source.text
link=bs4.BeautifulSoup(link,'html.parser')
li=[]
print(link)
lis=link.find_all("div")
#for i in range(0,len(lis)):
 # li.append(lis[i].getText())
#for z in range(1,40):
#  print str(z)+(lis[z].getText())
#day_that_year=li[37]
#print day_that_year