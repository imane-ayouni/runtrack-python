import re
from bs4 import BeautifulSoup as bs

import matplotlib.pyplot as plt

with open('data.txt','r') as data_text:
    new_data = data_text.read()
    upper_case = re.findall("[A-Z]", new_data)
    print(len(upper_case))
    lower_case = re.findall('[a-z]', new_data)
    print(len(lower_case))

x = ["Uppercase", "Lowercase"]
y = [len(upper_case),len(lower_case)]
plt.plot(x,y)
plt.xlabel("Upper/lower case")
plt.ylabel("number of letters")
plt.title("Occurence of Upper/lower case letters")
plt.show()
