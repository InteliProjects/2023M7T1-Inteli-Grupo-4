FROM python:3.11-slim-buster

RUN mkdir backend

WORKDIR /backend 

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . . 

CMD ["gunicorn", "-b" ,"0.0.0.0:8000", "app:app"]