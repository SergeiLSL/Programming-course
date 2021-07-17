"""
git ignor

32:00
Можно создать специальный файл внутри репрозитория и
создать специальные паттерны (шаблоны).
Если имя-файл попадет под этот шаблон, то git будет просто
игнорировать этот файл.
Создадим каталог:
mkdir log
cd log/
и внутри создадим файлик, который так и будет называться log.txt
touch log.txt
Чтобы перейти на каталог выше достаточно написать cd ..
git status

lsl33@SergeiPC MINGW64 /d/work on GitHube (master)
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        log/

nothing added to commit but untracked files present (use "git add" to track)
"""

"""
Добавляем файлик внутри нашего репозитория,
который так и называется vim .gitignore
В нем пропишем:

### Python template
# Byte-compiled / optimized / DLL files
__pycache__/
*py[cod]
docker-compose.yaml
log/
resources/products.json

Первые две строки это комментарий
Далее git не будет обращять вимание на целую папку __pycache__/
Все файлы с расширением .pyc, .pyo, .pyd будут игнорироваться git
Конкретно файл docker-compose.yaml будет игнорироваться git
папка log/
файл resources/products.json внутри каталога resources/

git status

lsl33@SergeiPC MINGW64 /d/work on GitHube (master)
$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .gitignore

nothing added to commit but untracked files present (use "git add" to track)

папка log пропала, но появился файл .gitignore

git add .gitignore

lsl33@SergeiPC MINGW64 /d/work on GitHube (master)
$ git add .gitignore
warning: LF will be replaced by CRLF in .gitignore.
The file will have its original line endings in your working directory

git commit -m "Add gitignore"

lsl33@SergeiPC MINGW64 /d/work on GitHube (master)
$ git commit -m "Add gitignore"
[master 7bcc1aa] Add gitignore
 1 file changed, 7 insertions(+)
 create mode 100644 .gitignore

git status

$ git status
On branch master
nothing to commit, working tree clean
"""

"""
Давайте создадим файл 
touch docker-compose.yaml
ls -la

lsl33@SergeiPC MINGW64 /d/work on GitHube (master)
$ touch docker-compose.yaml

lsl33@SergeiPC MINGW64 /d/work on GitHube (master)
$ ls -la
total 22
drwxr-xr-x 1 lsl33 197609   0 июл 17 16:08 ./
drwxr-xr-x 1 lsl33 197609   0 июл 16 16:07 ../
drwxr-xr-x 1 lsl33 197609   0 июл 17 16:06 .git/
-rw-r--r-- 1 lsl33 197609 131 июл 17 16:00 .gitignore
-rw-r--r-- 1 lsl33 197609  44 июл 17 15:15 application.py
-rw-r--r-- 1 lsl33 197609   0 июл 17 16:08 docker-compose.yaml
drwxr-xr-x 1 lsl33 197609   0 июл 17 15:42 log/

lsl33@SergeiPC MINGW64 /d/work on GitHube (master)

как видим файл есть
git status

lsl33@SergeiPC MINGW64 /d/work on GitHube (master)
$ git status
On branch master
nothing to commit, working tree clean

а у нас никаких ихменений нет, git проигнорировал этот файл
"""

"""
Подведем итоги

1. Настроить пользователя и его email
git config --global user.name "Sergei Student" 
git config --global user.email lsl1959@mail.ru 

2. Создаем репозиторий в каталоге 
git init

3. Состояние файлов
"""