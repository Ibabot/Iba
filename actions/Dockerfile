FROM ubuntu:18.04

RUN apt-get update && apt-get install -y python3 python3-pip
RUN python3 -m pip install --upgrade pip
RUN pip3 install rasa

ADD * /app/actions/

RUN chmod +x /app/actions/*

ENTRYPOINT []
CMD ./app/actions/start_actions.sh
