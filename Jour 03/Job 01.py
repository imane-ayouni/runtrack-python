import re
text = input("Renseigner une chaine de caractères ")
my_file = open("output.txt","w+")
my_file = text
print(my_file)
from bs4 import BeautifulSoup as bs


with open("domains.xml", 'r') as dom :
    data = dom.readlines()
    data = "".join(data)


extensions= re.search("[.\w]",data)
print(extensions)