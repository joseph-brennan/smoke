FROM ubuntu:18.04

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN apt-get update
RUN apt-get install -y --no-install-recommends \
  curl \
  git \
  python3 \
  python3-pip \
  python3-distutils \
  python3-pkg-resources \
  python \
  python-pip \
  python-pkg-resources
RUN rm -rf /var/lib/apt/lists/*

COPY ./scripts/smoke-env /usr/local/bin/smoke-env
RUN chmod +x /usr/local/bin/smoke-env

COPY ./scripts/bootstrap.sh /tmp/bootstrap
RUN bash /tmp/bootstrap
