FROM ubuntu:18.04

RUN apt-get update && apt-get -y install sudo && apt-get install -y python3 python3-pip
RUN python3 -m pip install --upgrade pip
RUN pip3 install rasa

ADD ./models /app/models/
ADD ./actions /app/actions/
ADD ./scripts /app/scripts/
ADD ./ /app/config/

# # Don't run as root
# USER 1001

#RUN useradd -m docker && echo "docker:docker" | chpasswd && adduser docker sudo

#"USER docker
ENTRYPOINT []
CMD /app/scripts/start_service.sh