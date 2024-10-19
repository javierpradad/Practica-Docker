FROM python:3.9-alpine3.20

WORKDIR /app

COPY . .

RUN pip install -r requirments.txt

EXPOSE 5000

CMD [ "python", "model.py" ]