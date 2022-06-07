from bs4 import BeautifulSoup


with open("test_stepik_course/html and bs4/4.html", encoding='utf8') as file:
    src = file.read()


soup = BeautifulSoup(src, 'lxml')
numbers = soup.find_all("td")
suma = 0
for number in numbers:
    suma += int(number.text)

print(suma)