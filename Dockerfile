# set base image (host OS)
FROM python:3-alpine

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY src/ .

# copy crontabs for root user
COPY cronjobs /etc/crontabs/root

# start crond
CMD ["crond", "-f"]
