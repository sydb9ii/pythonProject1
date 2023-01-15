# в данной програме митируется процесс аутенетнификации пользоватля. С записью и чтением в файл
def begin_screen():  # начальный экран приветствия
    flag = False
    login = ''
    password = ''
    print('Добро пожаловать в базу данных\n')
    login = input('Введите логин: ')
    flag = login_correct(login)
    password = input('Ввведите пароль: ')
    if flag:
        return login, password
    else:
        print('Некорректное имя позователя')


def file_exist():  # проверяем существует ли файл
    try:
        file_password = open('file.txt', 'r')
        return 1
    except FileNotFoundError:
        file_password = open('file.txt', 'w')
        return 0


def login_correct(login):  # проверят корректный ли введен логин пароль
    flag_login = False
    if login.isalpha():
        flag_login = True
    return flag_login


def user_exist(dict_login_password):  # проверяет существует ли пользователь в базе
    file_password = open('file.txt', 'r')
    while line!='':
        line = file_password.readline()
        if line == dict_login_password:
            return 1
        else:
            return 0


def main():
    dict_login_password = {}
    dict_login_password = begin_screen()
    file_flag = file_exist()
    user_exist_flag = user_exist(dict_login_password)
    if file_flag == 1:
        file_password = open('file.txt', 'r')
        line = file_password.readline()
        while line != '':
            pass


if __name__ == '__main__':
    main()
