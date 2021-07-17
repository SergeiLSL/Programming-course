"""
ТЕПЕРЬ РАССМОТРИМ НЕКОТОРЫЕ КОММАНДЫ
"""
"""
1. git log - она ображает коммиты, которые есть в истории

$ git log
commit 486f2b068e6a234570450f32299bb439ae498a55 (HEAD -> master)
Author: Sergei Student <lsl1959@mail.ru>
Date:   Sat Jul 17 12:07:12 2021 +0600

    Init commit
"""

"""   
git show

2. git show - она в зависимости от переданного аргумента отобразит 
болле подробно, что вы запрашиваете. Например если запросить 
просмотр коммита она более подробно отобразит, что это был за коммит

$ git show 486f2b068e6a234570450f32299bb439ae498a55
commit 486f2b068e6a234570450f32299bb439ae498a55 (HEAD -> master)
Author: Sergei Student <lsl1959@mail.ru>
Date:   Sat Jul 17 12:07:12 2021 +0600

    Init commit

diff --git a/app.py b/app.py
new file mode 100644
index 0000000..e69de29

Видим, что у нас создан файл и он пустой

Откороем его редактором vim (выход из vim и сохранит изменения  - Esc, :, x). 
Еще один полезный параметр (сорхранение без выхода из vim - Esc, :, w)
Еще один полезный параметр (выхода из vim и не сорхранит 
измениния  - Esc, :, q)

vim
"""

"""
3. git log -p выведет коммит

$ git log -p
commit 486f2b068e6a234570450f32299bb439ae498a55 (HEAD -> master)
Author: Sergei Student <lsl1959@mail.ru>
Date:   Sat Jul 17 12:07:12 2021 +0600

    Init commit

diff --git a/app.py b/app.py
new file mode 100644
index 0000000..e69de29

Она как бы объеденила git log и git show
"""

"""
4. git restore -она откатывает файл на состояние последнео коммита.
Откроем редактор vim app.py и напишем например print("Hello world").
Чтобы начать, что- то редактировать нажимаем 'I'. Сохраняем.

Вызовем git status и обратим внимание, что файл перешел в состояние
modified (изменный)

$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   app.py

no changes added to commit (use "git add" and/or "git commit -a")

Рекомендуется выполнить комманду "git add" и затем "git commit -a"

То есть мы изменили файл, но если мы хотим его вернуть на 
состояние последнего коммита нажо выполнить git restore app.py
Откроем редактор и увидим, что состояние файла перешло на то, 
какое было до последнего коммита
"""

"""
5. git diff - она показывает какие измения были внесены 
с момента последнего коммита. Например:
Вернемся к своему файлу в редакторе vim app.py
Вводим команду print() и соххраняем.
Вводим команду git diff

$ git diff
warning: LF will be replaced by CRLF in app.py.
The file will have its original line endings in your working directory
diff --git a/app.py b/app.py
index e69de29..aec9291 100644
--- a/app.py
+++ b/app.py
@@ -0,0 +1 @@
+print()

Видим, что произошли изменения: "+" - добавились изменения, 
а "-" - удалились какие-то строки.

Выполним git status

$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   app.py

no changes added to commit (use "git add" and/or "git commit -a")

Выполним git add app.py и git status

$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   app.py

Выполним git diff --stage - эта команда выведет измения,
которые находятся в индексе.

Закомитим эти изменения
$ git commit -m "Refactoring"
[master a9c18ae] Refactoring
 1 file changed, 1 insertion(+)

Выполним git log и увидим, что у нас уже два коммита

$ git log
commit a9c18ae0b572ecfe9cfca2bfa9e0c68bb2cf1e98 (HEAD -> master)
Author: Sergei Student <lsl1959@mail.ru>
Date:   Sat Jul 17 13:13:45 2021 +0600

    Refactoring

commit 486f2b068e6a234570450f32299bb439ae498a55
Author: Sergei Student <lsl1959@mail.ru>
Date:   Sat Jul 17 12:07:12 2021 +0600

    Init commit
"""

"""    
6. Есть интересный параметр, который можно передать комманде git commit
Выполним git status

$ git status
On branch master
nothing to commit, working tree clean

Видим, что никаких изменений нет.
Давайте изменим наш файлик. vim app.py
Вносим изменения и сохраняем.

Выполним git status

$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   app.py

no changes added to commit (use "git add" and/or "git commit -a")

Выполним git commit -am "Refactoring" - "a" означает все  файлы, 
которые под версионным контролем и которые были изменены и добавить 
их в индекс. Ну а "m" добавим коммит messeg.

$ git commit -am "Refactoring"
warning: LF will be replaced by CRLF in app.py.
The file will have its original line endings in your working directory
[master 366822b] Refactoring
 1 file changed, 1 insertion(+), 1 deletion(-)

Теперь git log покажет 3 коммита
"""

"""
7. git mv - с помщью этой команды можно либо 
переименовывать файлы, либо перемещать.
Например перименуем наш файл: git mv app.py application.py
Выплолним git status

$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        renamed:    app.py -> application.py

При этом git mv сразу выполняет git add
Закомитим git commit -m "Rename app.py"

$ git commit -m "Rename app.py"
[master 7859399] Rename app.py
 1 file changed, 0 insertions(+), 0 deletions(-)
 rename app.py => application.py (100%)
"""

"""
8. 26:05 git rm - сокращение от remove (удаление), в качестве аргумета 
можно передать например имя файла. git rm application.py

lsl33@SergeiPC MINGW64 /d/work on GitHube (master)
$ git rm application.py
rm 'application.py'

lsl33@SergeiPC MINGW64 /d/work on GitHube (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        deleted:    application.py

Давайте отменим измения
git restore --staged application.py

$ git status
On branch master
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        deleted:    application.py

no changes added to commit (use "git add" and/or "git commit -a")

Файл улетел из индекса

Выполним git restore application.py

git status
lsl33@SergeiPC MINGW64 /d/work on GitHube (master)
$ git restore application.py

lsl33@SergeiPC MINGW64 /d/work on GitHube (master)
$ git status
On branch master
nothing to commit, working tree clean
Теперь у нас нет никаких изменений , но и сам файл появился в каталоге

$ ls -la
total 21
drwxr-xr-x 1 lsl33 197609  0 июл 17 14:04 ./
drwxr-xr-x 1 lsl33 197609  0 июл 16 16:07 ../
drwxr-xr-x 1 lsl33 197609  0 июл 17 14:05 .git/
-rw-r--r-- 1 lsl33 197609 21 июл 17 14:04 application.py

Выполним команду  git rm --cached application.py
git status

$ git rm --cached application.py
rm 'application.py'

lsl33@SergeiPC MINGW64 /d/work on GitHube (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        deleted:    application.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        application.py

ls -la 
$ ls -la
total 21
drwxr-xr-x 1 lsl33 197609  0 июл 17 14:04 ./
drwxr-xr-x 1 lsl33 197609  0 июл 16 16:07 ../
drwxr-xr-x 1 lsl33 197609  0 июл 17 14:37 .git/
-rw-r--r-- 1 lsl33 197609 21 июл 17 14:04 application.py

Мы увидим файл никуда не делся
Вывполним git commit -m "Remove application.py"
git log
Наш файл есть и в каталоге и в коммитах, при этом если 
добавить git status увидим, что файл находится в категории Untracked files

$ git status
On branch master
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        application.py

nothing added to commit but untracked files present (use "git add" to track)
git add application.py
git status

$ git add application.py

lsl33@SergeiPC MINGW64 /d/work on GitHube (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   application.py

Что внутри этого файла?
vim application.py
git status

$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   application.py

После того как добавили в индекс давайте его поменяем.
vim application.py
git status

$ vim application.py

lsl33@SergeiPC MINGW64 /d/work on GitHube (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   application.py

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   application.py

Мы видим, что один и тот же файл application.py есть в изменениях 
для коммитов и он же изменен
git add application.py
git status

lsl33@SergeiPC MINGW64 /d/work on GitHube (master)
$ git add application.py

lsl33@SergeiPC MINGW64 /d/work on GitHube (master)
$ git status
On branch master
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   application.py

git commit -m "Refactoring"

lsl33@SergeiPC MINGW64 /d/work on GitHube (master)
$ git commit -m "Refactoring"
[master 02c7121] Refactoring
 1 file changed, 2 insertions(+)
 create mode 100644 application.py

git log

lsl33@SergeiPC MINGW64 /d/work on GitHube (master)
$ git show 02c712106f8e729fcc1d31ed9cbee0235f7c62a3
commit 02c712106f8e729fcc1d31ed9cbee0235f7c62a3 (HEAD -> master)
Author: Sergei Student <lsl1959@mail.ru>
Date:   Sat Jul 17 15:22:03 2021 +0600

    Refactoring

diff --git a/application.py b/application.py
new file mode 100644
index 0000000..0fbfb18
--- /dev/null
+++ b/application.py
@@ -0,0 +1,2 @@
+print("Some strig")
+print("Other string")
"""