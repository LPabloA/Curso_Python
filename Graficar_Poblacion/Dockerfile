FROM python:3.10

WORKDIR /graficos
COPY requirements.txt /graficos/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /graficos/requirements.txt

COPY . /graficos

CMD  bash -c "while true; do sleep 1; done"