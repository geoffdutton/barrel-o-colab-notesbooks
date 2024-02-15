# Use the official Python 3.10 image as the base image
FROM mcr.microsoft.com/devcontainers/python:3.10 as base

# Set user as vscode
USER vscode

RUN pip install --upgrade pip setuptools
RUN pipx install poetry==1.7.1

FROM base as devenv

# Set the working directory in the container
RUN git clone --depth=1 https://github.com/geoffdutton/bash-it.git ~/.bash_it
RUN bash ~/.bash_it/install.sh --silent
RUN sed -i "s/BASH_IT_THEME='bobby'/BASH_IT_THEME='bobby-python'/g" ~/.bashrc