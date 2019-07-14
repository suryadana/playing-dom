FROM python:3.7

# Install node for asset building
RUN apt-get update -qq && apt-get install -y build-essential \
    libpq-dev

# Create and switch to a user called app
RUN useradd -ms /bin/bash app
WORKDIR /home/app

# Copy across dependencies and install them
COPY ./app /home/app
COPY ./start.sh /home
RUN pip install flask
RUN chown -R app:app /home/app
USER app
