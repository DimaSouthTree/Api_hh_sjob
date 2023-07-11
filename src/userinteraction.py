class UserInteraction:
    platforms = ["HeadHunter", "SuperJob"]

    def __init__(self):
        pass

    def platform_selection(self):
        '''
        Метод для выбора платформы для поиска вакансий.
        :return: наименование платформы введеное пользователем str
        '''
        platform = input(
            f"Привет мы можем собрать данные с сайтов вакансий {UserInteraction.platforms}. Введите с какой платформы получить данные о вакансиях: ")
        return platform

    def search_query(self):
        '''
        Метод для ввода наименование вакансии.
        :return: наименование вакансии введеное пользователем str
        '''
        key_word = input("Введите поисковый запрос(название вакансии): ")
        return key_word

    def file_name(self):
        title = input('Введите наименования файла для сохранения вакансий в файл: ')
        return title

    def top_n_salary(self):
        '''
        Метод для ввода числа вакансий для формирования списка с самыми большими зарплатами.
        :return: число вакансий int
        '''
        top_salary = int(input("Введите число для вывода количества вакансий топ N по заработной плате: "))
        return top_salary

    def filter_salary(self):
        '''
        запрашивает у пользователя сумму заработной платы для фильтрации вакансий из файла
        :return:
        '''
        filter_user_salary = int(input("Введите сумму для отбора вакансий заработной платы  "))
        return filter_user_salary
    def filter_city(self):
        '''
        запрашивает у пользователя наименование города для фильтрации вакансий из файла
        :return:
        '''
        filter_user_city = int(input("Введите сумму для отбора вакансий заработной платы  "))
        return filter_user_city