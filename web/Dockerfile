# Use the Python3.7.2 image
FROM python:3.7.2-stretch


# Create and switch to a user called app
RUN useradd -ms /bin/bash app
WORKDIR /home/app

# Copy across dependencies and install them
COPY ./app /home/app
RUN pip install flask uwsgi
RUN chown -R app:app /home/app
USER app
# run the command to start uWSGI
CMD ["uwsgi", "app.ini"]
