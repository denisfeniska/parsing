from __future__ import print_function
import pandas as pd
import numpy as np
import statistics


salaries = pd.read_excel("test_stepik_course/spreadsheets/salaries.xlsx")
salaries.set_index('Unnamed: 0', inplace=True)
print(salaries)


def find_the_biggest_salary(salaries):
    L = {}
    Programmer = salaries['Программист'].mean()
    cleaning = salaries['Менеджер по клинингу'].mean()
    designer = salaries['Дизайнер онлайн-курсов'].mean()
    hairdresser = salaries['Собачий парикмахер'].mean()
    neuralnetworks = salaries['Учитель для нейросетей'].mean()
    militia = salaries['Сотрудник конной милиции'].mean()
    actor = salaries['Актёр на роль человека-бутерброда'].mean()
    L['Программист'] = Programmer
    L['Менеджер по клинингу'] = cleaning
    L['Дизайнер онлайн-курсов'] = designer
    L['Собачий парикмахер'] = hairdresser
    L['Учитель для нейросетей'] = neuralnetworks
    L['Сотрудник конной милиции'] = militia
    L['Актёр на роль человека-бутерброда'] = actor
    final_dict = dict([max(L.items(), key=lambda k_v: k_v[1])])
    print(*final_dict.keys())


def find_the_biggest_median_slary(salaries):

    L = {}

    moscow = salaries.iloc[0]
    moscow_array = np.array(moscow.values.tolist())
    final_moscow = statistics.median(moscow_array)

    bator = salaries.iloc[1]
    bator_array = np.array(bator.values.tolist())
    final_bator = statistics.median(bator_array)

    Kuibyshev = salaries.iloc[2]
    Kuibyshev_array = np.array(Kuibyshev.values.tolist())
    final_Kuibyshev = statistics.median(Kuibyshev_array)

    Krekshino = salaries.iloc[3]
    Krekshino_array = np.array(Krekshino.values.tolist())
    final_Krekshino = statistics.median(Krekshino_array)

    village = salaries.iloc[4]
    village_array = np.array(village.values.tolist())
    final_village = statistics.median(village_array)

    lumpur = salaries.iloc[5]
    lumpur_array = np.array(lumpur.values.tolist())
    final_lumpur = statistics.median(lumpur_array)

    hafnarfjordur = salaries.iloc[6]
    hafnarfjordur_array = np.array(hafnarfjordur.values.tolist())
    final_hafnarfjordur = statistics.median(hafnarfjordur_array)

    kyul = salaries.iloc[7]
    kyul_array = np.array(kyul.values.tolist())
    final_kyul = statistics.median(kyul_array)

    L['Москва'] = final_moscow
    L['Улан-Батор'] = final_bator
    L['Посёлок гидроузла имени Куйбышева'] = final_Kuibyshev
    L['Крёкшино'] = final_Krekshino
    L['УСтаница Юго-Северная'] = final_village
    L['Куала-Лумпур'] = final_lumpur
    L['Хабнарфьордюр'] = final_hafnarfjordur
    L['Ытык-Кюёль'] = final_kyul

    final_dict = dict([max(L.items(), key=lambda k_v: k_v[1])])
    print(*final_dict.keys())


find_the_biggest_median_slary(salaries)
find_the_biggest_salary(salaries)
