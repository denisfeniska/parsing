import numpy as np
import pandas as pd


directory = pd.read_excel(
    "test_stepik_course/spreadsheets/trekking2.xlsx", sheet_name='Справочник')
directory.set_index('Unnamed: 0', inplace=True)
layout = pd.read_excel(
    "test_stepik_course/spreadsheets/trekking2.xlsx", sheet_name='Раскладка')
layout.set_index('Продукт', inplace=True)
# print(directory)
# print(layout)
calories = 0
protein = 0
fats = 0
carbohydrates = 0


def calc_calories():
    global calories
    layout_cal = layout.to_dict('dict')
    layout_cal = layout_cal['Вес в граммах']
    directory_cal = directory.to_dict('dict')
    directory_cal = directory_cal['ККал на 100']
    for i in layout_cal:
        amount = layout_cal[i]
        hundred_amount = directory_cal[i]
        calories += hundred_amount / 100 * amount


def calc_protein():
    global protein
    layout_protein = layout.to_dict('dict')
    layout_protein = layout_protein['Вес в граммах']
    directory_protein = directory.to_dict('dict')
    directory_protein = directory_protein['Б на 100']
    for i in layout_protein:
        amount = layout_protein[i]
        hundred_amount = directory_protein[i]
        protein += hundred_amount / 100 * amount


def calc_fats():
    global fats
    layout_fats = layout.to_dict('dict')
    layout_fats = layout_fats['Вес в граммах']
    directory_fats = directory.to_dict('dict')
    directory_fats = directory_fats['Ж на 100']
    for i in layout_fats:
        amount = layout_fats[i]
        hundred_amount = directory_fats[i]
        fats += hundred_amount / 100 * amount


def calc_carbohydrates():
    global carbohydrates
    layout_carbohydrates = layout.to_dict('dict')
    layout_carbohydrates = layout_carbohydrates['Вес в граммах']
    directory_carbohydrates = directory.to_dict('dict')
    directory_carbohydrates = directory_carbohydrates['У на 100']
    for i in layout_carbohydrates:
        amount = layout_carbohydrates[i]
        hundred_amount = directory_carbohydrates[i]
        if np.isnan(hundred_amount):
            hundred_amount = 0
        carbohydrates += hundred_amount / 100 * amount


calc_calories()
calc_protein()
calc_fats()
calc_carbohydrates()
print(int(calories), int(protein), int(fats), int(carbohydrates))
