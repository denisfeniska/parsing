import pandas as pd


directory = pd.read_excel(
    "test_stepik_course/spreadsheets/trekking2.xlsx", sheet_name='Справочник')
directory.set_index('Unnamed: 0', inplace=True)
layout = pd.read_excel(
    "test_stepik_course/spreadsheets/trekking2.xlsx", sheet_name='Раскладка')
layout.set_index('Продукт', inplace=True)
# print(directory)
# print(layout)


def calc_calories():
    print(layout)
    print(layout.keys())


calc_calories()
