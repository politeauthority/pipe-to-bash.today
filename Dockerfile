FROM debian:jessie

MAINTAINER Booj Data "alix@politeauthority.com"

EXPOSE 80

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        apt-utils \
        python \
        python-dev \
        python-pip \
        && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD ./ /pipe-to-git/
RUN pip install -r /pipe-to-git/requirements.txt
RUN cd /pipe-to-git/


CMD python /pipe-to-git/run.py