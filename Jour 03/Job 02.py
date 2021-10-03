import re
from bs4 import BeautifulSoup as bs
with open("data.txt", 'r') as data_text:
    new_data = data_text.read()
    n_data= re.sub(r"[^a-zA-Z]","",new_data)
    words = re.split("\s", new_data)

print("Number of words is: " + str(len(words)))