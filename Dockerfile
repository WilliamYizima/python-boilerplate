FROM python:3.9.1
MAINTAINER WilliamYizima

RUN mkdir /app
RUN mkdir /app/src

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN apt-get update

WORKDIR /app

COPY ./src /app/src
COPY ./requirements.txt /app/requirements.txt
COPY ./run.py /app/run.py


RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host=files.pythonhosted.org --no-cache-dir -r /app/requirements.txt
CMD ["python3", "-u", "run.py"]
