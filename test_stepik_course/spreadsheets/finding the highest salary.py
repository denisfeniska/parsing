from __future__ import print_function
import pandas as pd


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
    pass


find_the_biggest_median_slary(salaries)
# find_the_biggest_salary(salaries)
