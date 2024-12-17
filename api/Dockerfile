# imagem de referencia para o container backend: baseada na iimagem de python 3.10
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

#cria um diretorio chamado 'api' dentro no container criado
WORKDIR /api

COPY ./requirements.txt /api/requirements.txt

# instala todas as dependencias dentro da imagem
RUN pip install --no-cache-dir -r /api/requirements.txt

#copia o diretorio atual para o diretorio api dentro do container
COPY ./ /api