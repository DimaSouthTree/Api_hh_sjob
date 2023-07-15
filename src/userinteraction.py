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
        '''
        метод запрашивает у пользователя название файла, куда будем добавлять вакансии.
        :return: название файла
        '''
        title_file = input('Введите наименования файла для сохранения вакансий в файл: ')
        return title_file

    def top_n_salary(self):
        '''
        Метод для ввода числа вакансий для формирования списка с самыми большими зарплатами.
        :return: число вакансий int
        '''
        number_top_salary = int(input("Введите число для вывода количества вакансий топ N по заработной плате: "))
        return number_top_salary

    def filter_salary(self):
        '''
        запрашивает у пользователя сумму заработной платы для фильтрации вакансий из файла
        :return:
        '''
        filter_salary = int(input("Введите сумму для отбора вакансий заработной платы  "))
        return filter_salary

    def filter_city(self):
        '''
        запрашивает у пользователя наименование города для фильтрации вакансий из файла
        :return:
        '''
        filter_city = int(input("Введите сумму для отбора вакансий заработной платы  "))
        return filter_city

    # def job_delete_user(self):
    #     answer_user_delete = input('Вы хотите удалить вакансию из файла? ')
    #     return answer_user_delete