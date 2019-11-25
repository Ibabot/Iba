FROM rasa/rasa-sdk:latest

WORKDIR /app COPY ./ ./

CMD $(echo “rasa run -p $PORT -m models --credentials credentials.yml --enable-api --log-file out.log --endpoints endpoints.yml” | sed ‘s/=//’)

EXPOSE 5005