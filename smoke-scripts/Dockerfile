FROM ubuntu:18.04

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN apt-get update
RUN apt-get install -y --no-install-recommends gnupg curl ca-certificates

RUN curl -sSL "https://dl-ssl.google.com/linux/linux_signing_key.pub" | apt-key add -
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" | tee -a /etc/apt/sources.list

RUN apt-get update
RUN apt-get install -y --no-install-recommends \
  git \
  python3 \
  python3-pip \
  python3-distutils \
  python3-pkg-resources \
  python \
  python-pip \
  python-pkg-resources \
  openjdk-8-jdk \
  google-chrome-stable

RUN rm -rf /var/lib/apt/lists/*

COPY ./scripts/smoke-env /bin/smoke-env
RUN chmod +x /bin/smoke-env

COPY ./scripts/bootstrap.sh /tmp/bootstrap
RUN bash /tmp/bootstrap
