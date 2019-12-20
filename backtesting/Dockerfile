# Python support can be specified down to the minor or micro version
# (e.g. 3.6 or 3.6.3).
# OS Support also exists for jessie & stretch (slim and full).
# See https://hub.docker.com/r/library/python/ for all supported Python
# tags from Docker Hub.
# FROM python:alpine

# If you prefer miniconda:
FROM continuumio/miniconda3

LABEL Name=backtesting Version=0.0.1
EXPOSE 3000

WORKDIR /app

ADD ./environment.yml /app/

RUN conda env create -f environment.yml

ADD ./*.py /app/

ARG QUANDL_API_KEY
ENV ZIPLINE_ROOT /.zipline
RUN /bin/bash -c "\
    mkdir /.zipline && \
    source activate backtest && \
    zipline ingest -b quantopian-quandl && \
    python3 setup.py"

ADD ./src /app/src

CMD /bin/bash -c "source activate backtest && python3 -m src"
