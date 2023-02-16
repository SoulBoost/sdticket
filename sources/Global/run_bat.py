from subprocess import Popen, CREATE_NEW_CONSOLE, PIPE
import pathlib


# запускает .bat файл, возвращает код ошибки
def run_bat(file):
    p = Popen(file, text=True, creationflags=CREATE_NEW_CONSOLE, encoding="cp866")
    stdout, stderr = p.communicate()
    return p.returncode


# запускает .bat файл, возвращает все
def run_bat_out(file):
    p = Popen(file, text=True, creationflags=CREATE_NEW_CONSOLE,
              stdout=PIPE, stderr=PIPE, encoding="cp866")
    stdout, stderr = p.communicate()
    return [stdout, stderr, p.returncode]


# проверяет существует ли указанный путь
def path_existance(file):
    path = pathlib.Path(file)
    return path.exists()


# если нет подключения
# [None, None, 2]
# ['', 'Не удалось найти сетевое подключение.\n\nДля вызова дополнительной справки наберите NET HELPMSG 2250.\n\nСистемная ошибка 53.\n\nНе найден сетевой путь.\n\n', 2]

# если открыт B и ответ N
# [None, None, 2]
# ['В подключения к B: имеются открытые файлы и/или незавершенные операции поиска в каталогах.\n\nПродолжить отключение и закрыть? (Y-да/N-нет) [N]: \n', 'Не был получен допустимый отклик.\nСистемная ошибка 85.\n\nИмя локального устройства уже используется.\n\n', 2]

# если открыт B и ответ Y
# [None, None, 0]
# ['B: успешно удален.\n\n', '', 0]

# если нет диска и он норм поключился
# [None, None, 0]
# ['B: успешно удален.\n\n', '', 0]

# если все ок
# [None, None, 0]
# ['B: успешно удален.\n\n', '', 0]

if __name__ == '__main__':
    path_B_bat = r"..\Resources\B_Drive.bat"
    path_B = r"B:\\"
    PATH_TEMP_CLEAN = r"..\Resources\Temp_Clean.cmd"
    PATH_CACHE_CLEANING = r"..\Resources\Cache_Cleaning.bat"
    print(run_bat_out(path_B_bat))
    print(path_existance(path_B))
