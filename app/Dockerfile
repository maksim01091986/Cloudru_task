FROM ubuntu:latest
 
RUN apt update -qy
RUN apt install -qy python3-pip
RUN apt install python3-dev

WORKDIR /app
COPY ./ ./

RUN pip3 install -r requirements.txt

CMD [ "python3", "main.py" ]

EXPOSE 8000
