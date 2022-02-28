# Step 1 select default OS image
FROM alpine


# Step 2 Setting up environment
RUN apk add --no-cache python3-dev && pip3 install --upgrade pip

# Step 3 Configure a software
WORKDIR /app

# Installing dependencies.
COPY /requirements.txt /app

RUN pip3 install -r requirements.txt

COPY ["main.py", "/app"]

EXPOSE 5000

ENTRYPOINT [ "python3" ]

CMD ["main.py"]