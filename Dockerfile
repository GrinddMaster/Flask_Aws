FROM python:3.12.3

WORKDIR /CybProj

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . . 

WORKDIR /CybProj/CyberApp

RUN flask db init
RUN flask db migrate
RUN flask db upgrade

WORKDIR /CybProj

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]
