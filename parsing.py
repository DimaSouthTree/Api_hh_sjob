from abc import ABC, abstractmethod
from pprint import pprint
import requests
import json

import self


class Api_get_servise(ABC):
    # def __init__(self, text):
    #     self.name_text = text
    pass


class Api_get_servise_hh(Api_get_servise):
    url = "https://api.hh.ru/vacancies"

    def __init__(self, text):
        self.name_text = text

    def get_service(self):
        hh_info = requests.get(Api_get_servise_hh.url, params={'text': f'NAME:{self.name_text}',
                                                               'per_page': 100})

        return pprint(hh_info.json())


class Api_get_servise_sjob(Api_get_servise):
    API_KEY = {
        "X-Api-App-Id": "v3.r.137645209.b47468e74b48a5fb3a8923a38104bf7bf9405bc5.c332503b8cc95ce4034c399dae34c4042e4a09bc"}
    url = "https://api.superjob.ru/2.0/vacancies"

    def __init__(self, text):
        self.keyword = text

    def get_service_job(self):
        job_info = requests.get(Api_get_servise_sjob.url, headers=Api_get_servise_sjob.API_KEY,
                                params={'keyword': self.keyword})
        return pprint(job_info.json())


class Vacancy():
    def __init__(self, name_vacancy, url_vacancy, salary_vacancy, requirements_vacancy):
        self.name = name_vacancy
        self.url = url_vacancy
        self.salary = salary_vacancy
        self.requirements = requirements_vacancy

    pass


class Save_to_file(ABC):
    pass


class JsonSaveFail(Save_to_file):
    pass


# hh_info = Api_get_servise_hh('Python')
# hh_info.get_service()

job_info = Api_get_servise_sjob('Python')
job_info.get_service_job()
