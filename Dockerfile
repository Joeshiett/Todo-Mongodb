FROM python:3.8.10
ADD . /todo
WORKDIR /todo
RUN pip install -r requirements.txt