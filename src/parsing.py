from abc import ABC, abstractmethod
from pprint import pprint
import requests
import json


class Api_get_servise(ABC):

    def __init__(self):
        pass

    def get_service(self):
        pass


class Api_get_servise_hh(Api_get_servise):
    """
        Класс для подключения по АПИ к hh.ru. Реализованы два метода один возвращает данные о вакансиях в формате Json. Второй метод возвращает массив вакансий с необходимыми полями.
        """
    url = "https://api.hh.ru/vacancies?only_with_salary=true"

    def __init__(self, text):
        self.name_text = text

    def get_service(self):
        """
        Отправляет Get запрос к сайту hh.ru с поиском вакансии по наименованю.
        :return: данные о вакансиях в формате Json.
        """
        hh_info = requests.get(Api_get_servise_hh.url, params={'text': f'NAME:{self.name_text}',
                                                               'per_page': 100})
        return hh_info.json()['items']

    def my_vacancies_data(self):
        """
        проходит в цикле по каждой вакансии и записывает в словарь необходимые данные о вакансии.
        :return: массив вакансий с нужными атрибутами
        """
        my_vacancies = []
        for data in self.get_service():
            if data['salary']['from'] == None:
                salary_from = 0
            else:
                salary_from = int(data['salary']['from'])

            if data['salary']['to'] == None:
                salary_to = 0
            else:
                salary_to = int(data['salary']['to'])
            my_dict_vacancies = {'id_vacancy': data['id'], 'vacancy': data['name'], 'url': data['alternate_url'],
                                 'city': data['area']['name'],
                                 'salary_currency': data['salary']['currency'], 'salary_from': salary_from,
                                 'salary_to': salary_to, 'requirement': data['snippet']['requirement']}
            my_vacancies.append(my_dict_vacancies)

        return my_vacancies


class Api_get_servise_sjob(Api_get_servise):
    """
    Класс для подключения по АПИ к super.job. Реализованы два метода один возвращает данные о вакансиях в формате Json. Второй метод возвращает массив вакансий с необходимыми полями.
    """
    API_KEY = {
        "X-Api-App-Id": "v3.r.137645209.b47468e74b48a5fb3a8923a38104bf7bf9405bc5.c332503b8cc95ce4034c399dae34c4042e4a09bc"}
    url = "https://api.superjob.ru/2.0/vacancies"

    def __init__(self, text):
        self.name_text = text

    def get_service_job(self):
        """
                Отправляет Get запрос к сайту super.job с поиском вакансии по ключевому слову.
                :return: данные о вакансиях в формате Json.
                """
        job_info = requests.get(Api_get_servise_sjob.url, headers=Api_get_servise_sjob.API_KEY,
                                params={'keyword': self.name_text})

        return job_info.json()['objects']

    def my_vacancies_data(self):
        """
               проходит в цикле по каждой вакансии и записывает в словарь необходимые данные о вакансии.
               :return: массив вакансий с нужными атрибутами
               """
        my_vacancies = []
        for data in self.get_service_job():
            my_dict_vacancies = {'id_vacancy': data['id'], 'vacancy': data['profession'], 'url': data['link'],
                                 'city': data['town']['title'],
                                 'salary_currency': data['currency'], 'salary_from': int(data['payment_from']),
                                 'salary_to': int(data['payment_to']), 'requirement': data['candidat']}
            my_vacancies.append(my_dict_vacancies)

        return my_vacancies


class ExaminationUserWordHH(Api_get_servise_hh):
    pass


class ExaminationUserWordSJob(Api_get_servise_sjob):
    pass
