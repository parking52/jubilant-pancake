FROM ubuntu:latest
MAINTAINER mfracas melchior.fracas@gmail.com

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /client
WORKDIR /client


RUN pip install -r requirements.txt
## ENTRYPOINT ["python"]
## CMD client.py

## RUN export FLASK_APP=client.py
##  flask run
CMD python client/client.py
