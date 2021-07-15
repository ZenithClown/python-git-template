# ==========================================
#   Copyright (c) 2020 Debmalya Pramanik   #
# ==========================================

# -------------------------------------------------------------------
#   Mnemonic:   Dockerfile
#   Abstract:   Hello-World Docker Template
#
#   Date:       15 July 2021
#   Author:     Debmalya Pramanik
# -------------------------------------------------------------------

FROM python:3.8

ENV INSTALL_PATH /usr/src/helloworld
RUN mkdir -p $INSTALL_PATH

# install net-tools and nano-editor
RUN apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    nano \
    net-tools \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# set working directory
WORKDIR $INSTALL_PATH

# setup flask environment
# install all requirements
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# copy all files and folder to docker
COPY . .

# install the package with setup tools
RUN pip install <pkg-name>

# run the application in docker environment
# setup code for the same
