"""
36:00
https://www.youtube.com/watch?v=SEvR78OhGtw

Ветвления

Последний коммит имеет указатель HEAD.
При каждом новом коммите указатель перемещается.
его можно увидеть, если открыть команду git log
Мы увидим где стоит коммит, но и еще на какой ветке
"""
"""
Новую ветку можно создать коммандой
git branch new-api
Переключаются на новую ветку командой
git checkout new-api

Неписанное правило:
На ветке мастер находятся только готовые закнченные разработки.
Все остальные разработки ведутся в отдельных ветках.
Исправления также рекомендуется делать в отдельных ветках.
"""

"""
Есть механизм слияния веток - это
git merge
"""
"""
Чтобы посмотреть какие есть ветки - есть команда 
git branch -a

lsl33@SergeiPC MINGW64 /d/work on GitHube (master)
$ git branch new-api

lsl33@SergeiPC MINGW64 /d/work on GitHube (master)
$ git branch bugfix

lsl33@SergeiPC MINGW64 /d/work on GitHube (master)
$ git branch -a
  bugfix
* master
  new-api

* показывает на кокаой ветке мы сейчас находимся
git status

lsl33@SergeiPC MINGW64 /d/work on GitHube (master)
$ git status
On branch master
nothing to commit, working tree clean

выполним 
git checkout merge bugfix

Теперь ветка bugfix больше не нужна ее можно удалить
git branch -d bugfix

Если вы хотите удалить ветку не слив ее с какой-то другой,
это можно сделать командой git branch -D bugfix

тЕперь попытаемся объединить с new-api
git merge new-api
"""