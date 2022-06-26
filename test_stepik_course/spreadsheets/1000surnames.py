import pandas as pd
import zipfile


def unzip(zip_path, directory_path):
    fantasy_zip = zipfile.ZipFile(zip_path)
    fantasy_zip.extractall(directory_path)
    
    fantasy_zip.close()


unzip(zip_path='test_stepik_course/spreadsheets/rogaikopyta.zip', directory_path='test_stepik_course/spreadsheets/rogaikopyta')

L = {}
for i in range(1, 1001):
    data = pd.read_excel(
        f"test_stepik_course/spreadsheets/rogaikopyta/{i}.xlsx")
    data.set_index('Расчетный лист', inplace=True)
    # print(data)

    surname = data['Unnamed: 1'][0]
    salary = int(data['Unnamed: 3'][0])

    L[surname] = salary

sorted_dict = dict(sorted(L.items(), key=lambda x: x[0]))
for i in sorted_dict:
    print(str(i) + ' ' + str(sorted_dict[i]))
