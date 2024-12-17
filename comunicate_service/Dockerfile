FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

WORKDIR /comunicate_service

COPY ./requirements.txt /comunicate_service/requirements.txt

RUN pip install --no-cache-dir -r /comunicate_service/requirements.txt

COPY ./ /comunicate_service