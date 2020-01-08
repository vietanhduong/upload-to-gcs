FROM vietanhs0817/python:3.6

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV PYTHONPATH /app

COPY main.py /usr/local/bin/converter

RUN chmod +x /usr/local/bin/converter

ENTRYPOINT ['converter']
