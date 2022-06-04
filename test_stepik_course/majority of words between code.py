import re
from collections import Counter


with open("test_stepik_course/2.html", encoding='utf8') as file:
    src = file.read()

s = str(src)


codes_array = re.findall(r"(?<=<code>).{0,}(?=</code>)", s)
code_array = ' '.join(codes_array)

print(Counter(code_array))

