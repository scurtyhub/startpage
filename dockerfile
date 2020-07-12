FROM python:3.8.3-alpine

WORKDIR /project
ADD . /project
RUN pip install --upgrade pip
RUN pip install Flask requests

CMD ["python","app.py"]
