# FROM python:3.6-slim
FROM rasa/rasa-sdk:1.4.0

ADD . /app/actions

# CMD rasa run actions -p $PORT

# SHELL ["/bin/bash", "-c"]

# RUN apt-get update -qq && \
#   apt-get install -y --no-install-recommends \
#   build-essential && \
#   apt-get clean && \
#   rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
#   mkdir /app

# WORKDIR /app

# Copy as early as possible so we can cache ...
# COPY requirements.txt .

# RUN pip install -r requirements.txt --no-cache-dir

# COPY . .

# RUN pip install -e . --no-cache-dir

# VOLUME ["/app/actions"]

# EXPOSE 5055

# ENTRYPOINT ["./entrypoint.sh"]
# ENTRYPOINT []

# CMD ["start", "--actions", "actions.actions"]
# CMD ["rasa", "run", "actions", "-p", "$PORT"]
# CMD $(echo “rasa run actions -p $PORT” | sed ‘s/=//’)