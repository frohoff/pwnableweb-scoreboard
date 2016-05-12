FROM ubuntu

WORKDIR /app

ADD requirements.txt /app

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y python python-pip 

RUN pip install -r requirements.txt

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y libmysqlclient-dev
RUN pip install mysql-python

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y libpq-dev
RUN pip install psycopg2

ADD . /app

EXPOSE 9999

ENV SCOREBOARD_CREATE_DB 1 

CMD python main.py