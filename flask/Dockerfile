FROM python:slim-buster

WORKDIR /flask

COPY . .

RUN pip install -r requirements.txt

CMD [ "python", "app.py" ]
