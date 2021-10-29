FROM python:3.8-buster

RUN apt update && apt install -y wget gnupg software-properties-common

COPY . /
ENV PYTHONPATH=.
RUN pip install -r requirements.txt -U

# initialize db
ENV FLASK_APP=src
RUN flask init-db

EXPOSE 5000

CMD ["gunicorn", "--bind=0.0.0.0:5000", "--timeout", "600", "src:create_app()"]
