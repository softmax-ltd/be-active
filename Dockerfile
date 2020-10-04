ARG BASE_CONTAINER=python:3.7-alpine
FROM $BASE_CONTAINER

RUN apk add --no-cache bash git

WORKDIR app/

RUN git clone https://github.com/pe-st/garmin-connect-export.git \
    && git clone https://github.com/dtcooper/python-fitparse \
    && cd python-fitparse \
    && python setup.py install \
    && pip install pytz

RUN mkdir raw-data

COPY * ./

CMD ["bash", "download-raw-data.sh"]