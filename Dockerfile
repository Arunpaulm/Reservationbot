FROM python:3.9.1
ENV PYTHONUNBUFFERED 1
 
RUN mkdir /roomReservationBot
WORKDIR /roomReservationBot

COPY requirements.txt /roomReservationBot/


RUN pip install -r requirements.txt

COPY . /roomReservationBot/