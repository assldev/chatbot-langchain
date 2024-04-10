FROM python:3.9-slim

COPY app/requirements.txt /app_libs/requirements.txt
WORKDIR /app_libs
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY app/ /app
WORKDIR /app

CMD ["python", "chat.py"]