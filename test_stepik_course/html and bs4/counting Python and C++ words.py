# Посчитать на странице, каких слов больше(С++ или Python)

with open("test_stepik_course/html and bs4/1.html", encoding='utf8') as file:
    src = file.read()

text = str(src)

P_count = text.count("Python") #Кол-во слов Python
C_count = text.count("C++") #Кол-во слов C++

# print(C_count)

if P_count > C_count:
    print("Python")
elif P_count < C_count:
    print("C++")
else:
    print("The same number")
