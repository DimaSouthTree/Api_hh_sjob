import sys
from pprint import pprint
from src.parsing import Api_get_servise_hh, Api_get_servise_sjob, ExaminationUserWordHH, ExaminationUserWordSJob
from src.vacancy import Vacancy
from src.save_to_file import JsonSaveFail
from src.userinteraction import UserInteraction

# инициализируем класс UserInteraction для взаимодействия с пользователем
user = UserInteraction()

# выбор платформы и проверка выбора
while True:
    platform = user.platform_selection()
    if platform in user.platforms:
        break
    elif platform == "stop":
        print('Вы ввели stop. Программа завершается.')
        sys.exit()
    else:
        print(
            f'Вы неправильно ввели название платформы или мы не знаем такую платформу. Введите ще раз {user.platforms} или введите stop для завершения программы ')

# ввод наименования вакансии для сбора данных из платформы и проверка корректности введеного наименования
while True:
    name_vacancy = user.search_query()
    examination_hh = ExaminationUserWordHH(name_vacancy)
    examination_sjob = ExaminationUserWordHH(name_vacancy)
    if examination_hh.my_vacancies_data() == []:
        print(
            f"По вакансии {name_vacancy} ничего не найдено в {user.platforms[0]} или наименование введено некорректно. Проверьте корректность введенного наименования вакансии или введите другое наименование")
    elif examination_sjob.my_vacancies_data() == []:
        print(
            f"По вакансии {name_vacancy} ничего не найдено в {user.platforms[1]} или наименование введено некорректно. Проверьте корректность введенного наименования вакансии или введите другое наименование")
    else:
        break

# ввод названия фала для сохранения вакансий в json файл
name_file = user.file_name()
# ввод чила вакансий для отбора топ N вакансий и записих их в файл
number_top_vacancies = user.top_n_salary()
# ввод суммы заработной платы для отбора вакансий из файла
salary_user = user.filter_salary()
# ввод yfbvtyjdfybz ujhjlf для отбора вакансий из файла
city_user = user.filter_city()

# инициализируем класс для работы с платформой выбранной пользователем
if platform == user.platforms[0]:
    print('Вы выбрали HeadHunter. Осущевствляем сбор данных.')
    user_vacancies = Api_get_servise_hh(name_vacancy)
elif platform == user.platforms[1]:
    print('Вы выбрали SuperJob. Осущевствляем сбор данных.')
    user_vacancies = Api_get_servise_sjob(name_vacancy)

# инициализация класса Vacancy массивом вакансий с необходимыми атрибутами
vacancies = [Vacancy(data) for data in user_vacancies.my_vacancies_data()]

# Сортировка вакансий по заработной плате и валюте для сохранения в файл топ N введенным пользователем
vacancies_sorted = sorted(vacancies)
vacancies_sorted_RUR = []
vacancies_sorted_BYR = []
vacancies_sorted_USD = []
vacancies_sorted_EUR = []
vacancies_sorted_KZT = []
vacancies_sorted_UZS = []
for vacancy in vacancies_sorted:
    data = vacancy.vacancy_dict()
    if data['salary_currency'] == 'RUR':
        vacancies_sorted_RUR.append(data)
    elif data['salary_currency'] == 'rub':
        vacancies_sorted_RUR.append(data)
    elif data['salary_currency'] == 'BYR':
        vacancies_sorted_BYR.append(data)
    elif data['salary_currency'] == 'USD':
        vacancies_sorted_USD.append(data)
    elif data['salary_currency'] == 'EUR':
        vacancies_sorted_EUR.append(data)
    elif data['salary_currency'] == 'KZT':
        vacancies_sorted_KZT.append(data)
    elif data['salary_currency'] == 'UZS':
        vacancies_sorted_UZS.append(data)

# Инициализация класса JsonSaveFail по имени файла для добавления всех вакансий в файл
json_saver = JsonSaveFail(name_file)
for vacancy in vacancies:
    data = vacancy.vacancy_dict()
    json_saver.add_vacancy(data)

# сохраниение топ N вакансий в файлы
json_saver.save_vacancies_top('top_vacancies_RUR', vacancies_sorted_RUR[-number_top_vacancies:])
json_saver.save_vacancies_top('top_vacancies_BYR', vacancies_sorted_BYR[-number_top_vacancies:])
json_saver.save_vacancies_top('top_vacancies_USD', vacancies_sorted_USD[-number_top_vacancies:])
json_saver.save_vacancies_top('top_vacancies_EUR', vacancies_sorted_EUR[-number_top_vacancies:])
json_saver.save_vacancies_top('top_vacancies_KZT', vacancies_sorted_KZT[-number_top_vacancies:])
json_saver.save_vacancies_top('top_vacancies_UZS', vacancies_sorted_UZS[-number_top_vacancies:])

# получение вакансий по фильтру заработной платы из файла и сохранение в отдельный файл
user_salary_filter = json_saver.get_info_vacancy_name(salary_user)
json_saver.save_vacancies_top('vacancies_user_salary', user_salary_filter)
# получение вакансий по фильтру наименования города из файла и сохранение в отдельный файл
user_city_filter = json_saver.get_info_vacancy_name(city_user)
json_saver.save_vacancies_top('vacancies_user_city', user_city_filter)

# удаление вакансии по id необходимо ввести id
json_saver.delete_vacancy('83041941')
