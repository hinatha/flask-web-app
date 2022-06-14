# Specify base image
FROM python:3.9

# Update apt-get version and install SQLite3
RUN apt-get update && apt-get install -y sqlite3 && apt-get install -y libsqlite3-dev && apt-get install -y libgl1-mesa-dev

# Specify working directory on container
WORKDIR /usr/src/

# Copy directory and file to container
COPY ./apps /usr/src/apps
COPY ./local.sqlite /usr/src/local.sqlite
COPY ./requirements.txt /usr/src/requirements.txt
COPY ./model.pt /usr/src/model.pt

# Upgrade pip version
RUN pip install --upgrade pip

# Install required libraries to environment of container
RUN pip install -r requirements.txt

# Process of showing "building"
RUN echo "Building..."

# Setting required each environment variables
ENV FLASK_APP "apps.app:create_app('local')"
ENV IMAGE URL "/storage/images/"

# Listen to specific network port when executing the container
EXPOSE 5000

# Process of executing when "docker run" execute
CMD ["flask", "run", "-h", "0.0.0.0"]
