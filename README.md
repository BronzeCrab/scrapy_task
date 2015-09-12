# scrapy_task
Я выполнил не все задание, только часть. Конфигурационные файлы загрузить нельзя. Можно только напарсить тайтлы и посмотреть результаты. Использовал: `Python 2.7`, `Scrapy`, `Flask`, `SQLalchemy`, `sqlite`. `Celery` не использовал вообще. 
## Как запустить парсер (на примере голой ubuntu 14.04):
ставим гит

1.  `sudo apt-get install git`

и пип

2.  `wget https://bootstrap.pypa.io/get-pip.py`
3.  `python get-pip.py`

фласк

4.  `sudo pip install Flask`

установка scrapy через apt-get

5.  `sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 627220E7`
6.  `echo 'deb http://archive.scrapy.org/ubuntu scrapy main' | sudo tee /etc/apt/sources.list.d/scrapy.list`
7.  `sudo apt-get update && sudo apt-get install scrapy`

Sqlalchemy

8.  `pip install SQLAlchemy`

Копируем этот репозиторий

2.  `git clone https://github.com/BronzeCrab/scrapy_task.git`

Запускаем скрипт, создающий бд в sqlite

3.  `cd scrapy_task`
4.  `python`
5.  `from fl_app import init_db`
6.  `init_db()`

Запускаем скрипт, создающий необходимый класс slqalchemy -`Title`

7.  `python database_setup.py`

Запускаем сервер

8.  `python fl_app.py`

Смотрим результаты

9.  `curl -X POST localhost:5000`
10.  `curl localhost:5000/titles`
