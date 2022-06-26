from bs4 import BeautifulSoup


fin = open('test_stepik_course/xml/map2.osm', 'r', encoding='utf8')
xml = fin.read()
fin.close()

count = 0

soup = BeautifulSoup(xml, 'lxml')
all_nodes = soup.find_all('node')
s = BeautifulSoup(str(all_nodes), 'lxml').find_all('tag', k='amenity', v='fuel')
for refuel in s:
    count += 1
print(count)
