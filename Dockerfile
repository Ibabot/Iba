FROM ubuntu:18.04

RUN apt-get update && apt-get install -y python3 python3-pip
RUN python3 -m pip install --upgrade pip
RUN pip3 install rasa


ADD ./models /app/models/
ADD ./actions /app/actions/
ADD ./scripts /app/scripts/
ADD ./config /app/config/

# Don't run as root
USER 1001

RUN sudo chmod u+x /app/scripts/*

ENTRYPOINT []
CMD /app/scripts/start_service.sh