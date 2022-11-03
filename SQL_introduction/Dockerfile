FROM ubuntu:20.04
RUN apt-get -y update
# update and install dependencies
RUN  apt-get update \
    && apt-get install -y \
        make \
        git \
    && apt install -y build-essential
RUN apt-get install -y sqlite3 libsqlite3-dev