FROM python:3.9

COPY . /app

WORKDIR /app

EXPOSE 1337

CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0"]