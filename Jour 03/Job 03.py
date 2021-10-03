import re
from bs4 import BeautifulSoup as bs

with open("data.txt", 'r') as data_text:
    new_data = data_text.read()
    words = re.split("\s", new_data)
    characters_count = input("Choose a number ")
    words_list = []
for word in words:
    if len(word) == characters_count:
        words_list.append(word)

print(words_list)