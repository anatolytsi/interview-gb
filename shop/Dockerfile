FROM python:3.6.15

RUN pip install gunicorn
RUN pip install --upgrade pip

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY ./ ./
