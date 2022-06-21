from bs4 import BeautifulSoup


soup = BeautifulSoup(open('test_stepik_course/xml/map2 (1).osm', encoding='utf8'), 'lxml')
print(len(soup.select('tag[k=amenity][v=fuel]')))
