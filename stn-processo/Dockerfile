FROM python:3.6.8-jessie

RUN mkdir -p /src
WORKDIR /src

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /src

EXPOSE 5013
