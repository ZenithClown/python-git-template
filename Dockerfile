# ==========================================
#   Copyright (c) 2021 Debmalya Pramanik   #
# ==========================================

# -------------------------------------------------------------------
#   Mnemonic:   Dockerfile
#   Abstract:   Python Package Template Dockerfile
#
#   Date:       15 July 2021
#   Author:     Debmalya Pramanik
# -------------------------------------------------------------------

FROM python:3.10-slim

ENV INSTALL_PATH /usr/src/app
RUN mkdir -p $INSTALL_PATH

# set working directory
WORKDIR $INSTALL_PATH

# install all requirements
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# copy all files and folder to docker
COPY . .

# install the package from source
RUN pip install --no-cache-dir .

# run the application in docker environment
# setup code for the same
