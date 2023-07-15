class Vacancy:
    """
    Класс для работы с вакансиями. Сравнение по зарплате.
    """

    def __init__(self, my_vacancies_dict: dict):
        self.id = my_vacancies_dict['id_vacancy']
        self.name = my_vacancies_dict['vacancy']
        self.url = my_vacancies_dict['url']
        self.city = my_vacancies_dict['city']
        self.salary_currency = my_vacancies_dict['salary_currency']
        self.salary_from = my_vacancies_dict['salary_from']
        self.salary_to = my_vacancies_dict['salary_to']
        self.requirements = my_vacancies_dict['requirement']
        self.salary_from_and_to = f'{self.salary_from}-{self.salary_to}'
        self.salary = self.salary_from if self.salary_to == 0 else self.salary_to
        self.__salary_range = range(self.salary_from) if self.salary_to == 0 else range(self.salary_from,
                                                                                        self.salary_to)

    @property
    def salary_range(self):
        return self.__salary_range

    # написать метод все свойства конвертировались в дикшионари
    def vacancy_dict(self):
        '''
        Метод для преобразования атрибутов экземпляра класса в словарь
        :return: словарь атрибутов экземпляра класса
        '''
        my_vacancy_dict = {'id_vacancy': self.id, 'vacancy': self.name, 'url': self.url, 'city': self.city,
                           'salary_currency': self.salary_currency, 'salary_from': self.salary_from,
                           'salary_to': self.salary_to, 'salary_from_and_to': self.salary_from_and_to,
                           'salary': self.salary, 'requirement': self.requirements}
        return my_vacancy_dict

    def __gt__(self, other):
        if not isinstance(other, Vacancy):
            raise ArithmeticError("Правый операнд должен быть Vacancy")
        if isinstance(other, Vacancy):
            return self.salary > other.salary

    def __ge__(self, other):
        if not isinstance(other, Vacancy):
            raise ArithmeticError("Правый операнд должен быть Vacancy")
        if isinstance(other, Vacancy):
            return self.salary >= other.salary

    def __lt__(self, other):
        if not isinstance(other, Vacancy):
            raise ArithmeticError("Правый операнд должен быть Vacancy")
        if isinstance(other, Vacancy):
            return self.salary <= other.salary

    def __le__(self, other):
        if not isinstance(other, Vacancy):
            raise ArithmeticError("Правый операнд должен быть Vacancy")
        if isinstance(other, Vacancy):
            return self.salary < other.salary

    def __eq__(self, other):
        if not isinstance(other, Vacancy):
            raise ArithmeticError("Правый операнд должен быть Vacancy")
        if isinstance(other, Vacancy):
            return self.salary == other.salary
