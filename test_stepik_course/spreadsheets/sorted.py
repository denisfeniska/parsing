import pandas as pd
import re


products = pd.read_excel("test_stepik_course/spreadsheets/trekking1.xlsx")
products.set_index('Unnamed: 0', inplace=True)
sorted_products = products.sort_values(by='ККал на 100', ascending=False).index
# print(sorted_products)
for i in sorted_products:
    print(i)
