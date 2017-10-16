FROM python:3.6

MAINTAINER jlin <jlinsche@gmail.com>

RUN pip3 install falcon
RUN pip3 install numpy
RUN pip3 install scipy
RUN pip3 install uwsgi
RUN pip3 install --upgrade gensim


ADD volume /code
WORKDIR /code


