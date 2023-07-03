class Vacancy():
    """
    Класс для работы с вакансиями. Сравнение по зарплате.
    """

    def __init__(self, my_vacancies_dict):
        self.name = my_vacancies_dict['name_vacancy']
        self.url = my_vacancies_dict['url']
        self.city = my_vacancies_dict['city']
        self.salary_currency = my_vacancies_dict['salary_currency']
        self.salary_from_and_to = f"{my_vacancies_dict['salary_from']} -> {my_vacancies_dict['salary_to']}"
        self.requirements = my_vacancies_dict['requirement']