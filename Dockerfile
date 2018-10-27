FROM python

EXPOSE 8000

RUN mkdir /app
WORKDIR /app

ADD Pipfile Pipfile.lock ./

RUN pip3 install pipenv \
 && pipenv install --system --deploy

ADD . .

CMD ./manage.py migrate \
 && ./manage.py runserver 0.0.0.0:8000
