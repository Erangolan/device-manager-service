FROM alpine

RUN apk add --no-cache python3-dev && pip3 install --upgrade pip

WORKDIR /app

COPY /requirements.txt /app

RUN pip3 install -r requirements.txt

COPY ["main.py", "/app"]

EXPOSE 5000

ENTRYPOINT [ "python3" ]

CMD ["main.py"]