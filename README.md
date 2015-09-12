# scrapy_task
Я выполнил не все задание, только часть. Конфигурационные файлы загрузить нельзя. Можно только напарсить тайтлы и посмотреть результаты. Использовал: `Python 2.7`, `Scrapy`, `Flask`, `SQLalchemy`, `sqlite`. `Celery` не использовал вообще. 
## Как запустить парсер (на примере голой ubuntu 14.04):
ставим гит

-  `sudo apt-get install git`

и пип

-  `wget https://bootstrap.pypa.io/get-pip.py`
-  `python get-pip.py`

фласк

-  `sudo pip install Flask`

установка scrapy через apt-get

-  `sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 627220E7`
-  `echo 'deb http://archive.scrapy.org/ubuntu scrapy main' | sudo tee /etc/apt/sources.list.d/scrapy.list`
-  `sudo apt-get update && sudo apt-get install scrapy`

Sqlalchemy

-  `pip install SQLAlchemy`

Копируем этот репозиторий

-  `git clone https://github.com/BronzeCrab/scrapy_task.git`

Запускаем функцию, создающую sqlite бд под названием `test.db`. Скрипт использует файл `schema.sql`. В котором определена таблица `titles`.

-  `cd scrapy_task`
-  `python`
-  `from fl_app import init_db`
-  `init_db()`

Запускаем скрипт, создающий необходимый класс slqalchemy -`Title`

-  `python database_setup.py`

Запускаем сервер

-  `python fl_app.py`

Смотрим результаты

-  `curl -X POST localhost:5000`
-  `curl localhost:5000/titles`
