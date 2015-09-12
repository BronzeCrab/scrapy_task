# scrapy_task
Я выполнил не все задание, только часть. Конфигурационные файлы загрузить нельзя. Можно только напарсить тайтлы и посмотреть результаты. Использовал: `Python 2.7`, `Scrapy`, `Flask`, `SQLalchemy`, `sqlite`. `Celery` не использовал вообще. 
## Как запустить парсер (на примере голой ubuntu 14.04):
1.  `sudo apt-get install git`
2.  `wget https://bootstrap.pypa.io/get-pip.py`
3.  `python get-pip.py`
4.  `sudo pip install Flask`
5.  `sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 627220E7`
6.  `echo 'deb http://archive.scrapy.org/ubuntu scrapy main' | sudo tee /etc/apt/sources.list.d/scrapy.list`
7.  `sudo apt-get update && sudo apt-get install scrapy`
8.  `pip install SQLAlchemy`
2.  `git clone https://github.com/BronzeCrab/scrapy_task.git`
3.  `cd scrapy_task`
4.  `python`
5.  `from fl_app import init_db`
6.  `init_db()`
7.  `python database_setup.py`
8.  `python fl_app.py`
9.  `curl -X POST localhost:5000`
10.  `curl localhost:5000/titles`
