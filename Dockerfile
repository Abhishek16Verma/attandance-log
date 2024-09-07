FROM python:3-alpine3.15
WORKDIR /app
COPY .  /app
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade pip setuptools wheel
RUN pip3 install -r app/requirements.txt
EXPOSE 4000
CMD python3 ./app/app.py