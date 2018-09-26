#download base Jenkins image
FROM jenkinsci/blueocean

#set user
USER root

#run update and install prerequisites
RUN apk update && apk add alpine-sdk python-dev ruby python python3 py-pip yarn openjdk8

#python install stuff
RUN pip install -U pip tox codecov

#tell docker which port to connect on
EXPOSE 8000

USER jenkins
