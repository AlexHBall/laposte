FROM python:3.7-slim

# layer caching for faster builds
COPY requirements.txt /
RUN pip install -r /requirements.txt

#COPY app.py /app.py
ADD . /flask_app
WORKDIR /flask_app

ENV FLASK_ENV=development

CMD flask run --host=0.0.0.0