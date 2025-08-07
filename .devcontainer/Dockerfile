FROM mcr.microsoft.com/devcontainers/python:1-3.11-bookworm
# FROM mcr.microsoft.com/devcontainers/base:jammy 
ENV PYTHONUNBUFFERED 1
RUN pip install poetry==1.8.3


RUN pip install Cython
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
 && apt-get -y install --no-install-recommends iputils-ping postgresql-client libsctp-dev libgsm1-dev libsrtp2-dev

WORKDIR /workspace