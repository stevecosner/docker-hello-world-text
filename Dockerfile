FROM ubuntu
MAINTAINER steve

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install python -y
RUN apt-get install python-pip -y
RUN pip install requests
COPY text.py /
