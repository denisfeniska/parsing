import xmltodict
from bs4 import BeautifulSoup

fin = open('test_stepik_course/xml/map1 (1).osm', 'r', encoding='utf8')
xml = fin.read()
fin.close()

count_with_tag = 0
count_without_tag = 0

# parsedxml = xmltodict.parse(xml)
# print(parsedxml['osm'])


soup = BeautifulSoup(xml, 'lxml')
for node in soup.find_all('node'):
    if node.find('tag') != None:
        # print(node)
        count_with_tag += 1
    else:
        # print(node)
        count_without_tag += 1
print(count_with_tag, count_without_tag)
