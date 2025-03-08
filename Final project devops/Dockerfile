FROM python:3.9

WORKDIR /app
COPY app /app
COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "main.py"]
