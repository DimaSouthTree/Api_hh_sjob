import os
import json
from abc import ABC, abstractmethod


class Save_to_file(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_info_vacancy_name(self, text):
        pass

    @abstractmethod
    def get_info_vacancy_salary(self, text):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass


class JsonSaveFail(Save_to_file):

    def __init__(self, title):
        self.name_file = title

    def add_vacancy(self, vacancy: dict):
        '''
        метод добавления вакансий в файл json
        :param vacancy: экземпляр класса Vacancy в dict
        :return:создает файл с вакансией и добавляет следующие вакансии в созданный файл
        '''
        data: list = []

        if not os.path.exists(f'{self.name_file}.json'):
            data.append(vacancy)
            with open(f'{self.name_file}.json', 'w') as file:
                json.dump(data, file, indent=3, ensure_ascii=False)
        else:
            with open(f'{self.name_file}.json', 'r') as file_app:
                data_file = json.load(file_app)
                data_file.append(vacancy)

            with open(f'{self.name_file}.json', 'w') as file_app:
                json.dump(data_file, file_app, indent=3, ensure_ascii=False)

    def save_vacancies_top(self, name_file: str, vacancies: list):
        with open(f'{name_file}.json', 'w') as file:
            json.dump(vacancies, file, indent=3, ensure_ascii=False)

    def get_info_vacancy_city(self, city: str):
        '''
        метод для получение инфомации о ваакансих из файла с отбором по городу
        :param city: наименование города введенное пользователем str
        :return: масиив вакансий
        '''
        info_vacancy_city = []
        with open(f'{self.name_file}.json', 'r') as file:
            data_file = json.load(file)
            for idx, txt in enumerate(data_file):
                if city == txt['city']:
                    info_vacancy_city.append(data_file[idx])

        return info_vacancy_city

    def get_info_vacancy_salary(self, number: int):
        '''
        метод для получение инфомации о ваакансих из файла с отбором по заработной плате
        :param number: сумм заработной платы которая интересует пользователя int
        :return: масиив вакансий
        '''
        info_vacancy_salary = []
        with open(f'{self.name_file}.json', 'r') as file:
            data_file = json.load(file)
            print(data_file)
            for idx, txt in enumerate(data_file):
                print(idx, txt)
                if number == txt['salary']:
                    info_vacancy_salary.append(data_file[idx])

        return info_vacancy_salary

    def delete_vacancy(self, id_vacancy: str):
        '''
        метод для удаление из файла вакансии по id
        :param id_vacancy: id вакансии str
        :return: перезаписыввает файл
        '''
        with open(f'{self.name_file}.json', 'r') as file_dell:
            data_file = json.load(file_dell)
            for idx, txt in enumerate(data_file):
                # print(idx, txt)
                if txt['id_vacancy'] == id_vacancy:
                    print('Запись будет удалена')
                    data_file.pop(idx)
                    break

        with open(f'{self.name_file}.json', 'w') as file_dell:
            json.dump(data_file, file_dell, indent=3, ensure_ascii=False)
