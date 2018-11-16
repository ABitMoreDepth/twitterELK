FROM python:3.6-alpine3.6

STOPSIGNAL SIGINT

RUN pip install pipenv

WORKDIR /usr/share/app/

COPY ./setup.py /usr/share/app/setup.py
COPY ./MANIFEST.in /usr/share/app/MANIFEST.in
COPY ./README.rst /usr/share/app/README.rst
COPY ./Pipfile /usr/share/app/Pipfile
COPY ./Pipfile.lock /usr/share/app/Pipfile.lock
COPY ./ingress /usr/share/app/ingress/

RUN set -ex && pipenv install --deploy --system

CMD ingress
