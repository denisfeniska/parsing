import re
from collections import Counter


with open("test_stepik_course/2.html", encoding='utf8') as file:
    src = file.read()

s = str(src)


regex = '<code>(.*?)</code>'
l = sorted(re.findall(regex, s)) #это список всех совпадений

print(Counter(l))

