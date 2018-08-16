FROM python:3.6-alpine

RUN adduser -D fmt

WORKDIR /home/fmt

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install pymysql

COPY app app
COPY migrations migrations
COPY fmt.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP fmt.py

RUN chown -R fmt:fmt ./
USER fmt

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]