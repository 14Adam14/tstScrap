import requests
from bs4 import BeautifulSoup
import pandas as pd
import random
from time import sleep



page_number = 1

shag = 0

url = 'https://www.apetogentleman.com/category/grooming/page/' + str(page_number) + '/'

q = requests.get(url)
result = q.content

# with open("data.html") as file:
#      src = file.read()

soup = BeautifulSoup(result, "lxml")

test_categories = soup.find_all('article')

duta = []

while page_number != 15:

    for ony in test_categories:
        duta.append(ony.text.strip())

    page_number += 1
    shag += 1

    print('делаем шаг ' + str(shag))
    sleep(random.randrange(2, 4))



   # print(ony.text)

# with open('data.txt', 'w') as f:
#     f.write(soup.prettify())

# print(duta[9])

dictionary = {
    'title':duta
}

df = pd.DataFrame(dictionary)

to_csv = df.to_csv('/Users/adam/Desktop/tstScrap/data-cvl.csv')

print('ее все завершено')

