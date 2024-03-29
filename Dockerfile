FROM python:3.8-alpine

WORKDIR /home/portfolio

COPY requirements.txt portfolio-backend/portfolio_backend/requirements.txt
RUN python3 -m venv python
RUN python/bin/python3 -m pip install --upgrade pip
RUN apk add zlib-dev jpeg-dev gcc musl-dev python3-dev build-base linux-headers pcre-dev
RUN python/bin/pip install wheel
RUN python/bin/pip install uwsgi
RUN python/bin/pip install -r portfolio-backend/portfolio_backend/requirements.txt
RUN python/bin/pip install 'SQLAlchemy<1.4.0'

COPY portfolio_backend portfolio-backend/portfolio_backend
COPY templates portfolio-backend/templates

RUN mkdir /home/portfolio/conf
RUN mkdir /home/portfolio/data
RUN touch /home/portfolio/conf/secrets.txt
RUN echo "SECRET_KEY=ASDASDASDSADASD" >> /home/portfolio/conf/secrets.txt

ENV FLASK_APP /home/portfolio/portfolio-backend/portfolio_backend/application/wsgi.py
ENV FLASK_ENV production

COPY deploy/uwsgi.ini /home/portfolio/conf/uwsgi.ini

CMD ["python/bin/uwsgi", "/home/portfolio/conf/uwsgi.ini"]
