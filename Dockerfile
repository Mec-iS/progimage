FROM tiangolo/uvicorn-gunicorn:python3.7

RUN pip install setuptools --upgrade && \
    pip install pip --upgrade && \
    pip install -r requirements.txt

COPY ./src /app

CMD uvicorn app:app