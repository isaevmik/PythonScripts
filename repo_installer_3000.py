import os
from shutil import rmtree

'''
Далее будут интуитивно понятные и описанные константы, которым необходимо передать значения под себе (фмя, 
фамилию, почту итд). Сделать это достаточно один раз. Затем скриптом можно будет пользоваться на постоянной основе.
'''

STUDENT_NAME = "Vasya Pupkin"  # Имя и Фамилия на латинице.
STUDENT_EMAIL = "vasya@post.ru"  # Электронная почта.

STUDENT_REPO_ADRESS = "git@gitlab.com:cpp-advanced-hse-2021/hse-Vasya-Pupkin-username.git"  # Нужно скопировать со страницы репозитория (My Repository в интерфейсе https://cpp-hse.org/). Синяя кнопка Clone -> Clone with SSH.

CURRENT_REPO_PATH = "/Users/username/cpp-advanced-hse"  # Директория, где сейчас находится репозиторий (Зайди в неё с терминала, введи pwd, скопируй и вставь сюда).
FUTURE_REPO_PATH = "/Users/username/"  # Директория, где репозиторий будет находится в будушем (То, куда склонируется репозиторий после git clone).

PARAM = 0  # 0 - удаление + создание, 1 - удаление, 2 - создание


'''
Тело скрипта
'''

if PARAM == 0 or PARAM == 1:
    # Удаляем репозиторий.
    rmtree(CURRENT_REPO_PATH)

if PARAM == 0 or PARAM == 2:
    # Клонируем репу в указанную в константах директорию.
    os.chdir(FUTURE_REPO_PATH)
    os.system("git clone https://gitlab.com/danlark/cpp-advanced-hse")

    # Устанавливаем Фамилию Имя и электронную почту для гита.
    os.system(f"git config --global user.name \"{STUDENT_NAME}\"")
    os.system(f"git config --global user.email {STUDENT_EMAIL}")

    # Добавляем remote репощитория.
    os.chdir(FUTURE_REPO_PATH + "cpp-advanced-hse")
    os.system(f"git remote add student {STUDENT_REPO_ADRESS}")

    # Сейчас создадим директории build и asan_build.
    os.system("mkdir build")
    os.system("mkdir asan_build")

    # Сгенерим cmake файлики для обычного билда и ASAN'a.
    os.chdir(FUTURE_REPO_PATH + "cpp-advanced-hse/build")
    os.system("cmake ..")
    os.chdir(FUTURE_REPO_PATH + "cpp-advanced-hse/asan_build")
    os.system("cmake -DCMAKE_BUILD_TYPE=ASAN ..")