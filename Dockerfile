FROM python:3-bullseye

RUN apt update
RUN apt install mariadb-client -y
RUN pip install --no-cache-dir --upgrade web.py mysqlclient
COPY ./server.py /server.py
COPY ./genre.py /genre.py
COPY ./DB.py /DB.py
CMD [ "python", "/server.py" ]
