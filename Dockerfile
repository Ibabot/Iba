FROM rasa/rasa:1.5.1

ADD ./models /app/models/
ADD ./actions /app/actions/

CMD ["run"]
