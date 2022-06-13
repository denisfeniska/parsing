import pandas as pd
import re


products = pd.read_excel("test_stepik_course/spreadsheets/trekking1.xlsx")
print(*products.sort_values(
	by=['ККал на 100', 'Unnamed: 0'],
	ascending=[False, True]
	)['Unnamed: 0'].to_list(), sep='\n')
