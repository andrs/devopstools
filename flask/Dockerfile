FROM python:3.12

RUN apt-get update && \
    apt-get install -y postgresql-client

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app app
COPY application.py .

EXPOSE 5000

CMD [ "python", "application.py"]
