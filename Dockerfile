FROM ubuntu

WORKDIR /app

ADD requirements.txt /app

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y python python-pip 

RUN pip install -r requirements.txt
RUN pip install gunicorn

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y libmysqlclient-dev
RUN pip install mysql-python

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y libpq-dev
RUN pip install psycopg2

ADD . /app

EXPOSE 9090

ENV LOG_TO_STDOUT 1
ENV SERVER_SOFTWARE Development/
ENV WAIT_DB 5

CMD sh -c "python main.py waitdb $WAIT_DB && python main.py createdb && gunicorn -w 4 --log-file - --log-level debug --access-logfile - -b 0.0.0.0:9090 main:app"
