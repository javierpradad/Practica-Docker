FROM python:3.14.0a1-alpine3.20

WORKDIR /app

COPY . .

RUN pip install -r requirments.txt

CMD [ "python", "model.py" ]