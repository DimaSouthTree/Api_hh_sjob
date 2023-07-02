from abc import ABC, abstractmethod
from pprint import pprint
import requests
import json


class Api_get_servise(ABC):
    pass


class Api_get_servise_hh(Api_get_servise):
    pass


class Api_get_servise_sjob(Api_get_servise):
    pass


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
