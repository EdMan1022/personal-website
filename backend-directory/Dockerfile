FROM python:3.5

WORKDIR /backend

ADD . /backend

RUN pip install -r requirements.txt

EXPOSE 80

ENV SQLALCHEMY_DATABASE_URI 'sqlite://'; /
    PYTHONPATH ../; /
    PORT 80

CMD ["python", "run.py"]
