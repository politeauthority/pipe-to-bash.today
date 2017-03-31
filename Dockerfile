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

ADD ./ /pipe-to-bash/
RUN pip install -r /pipe-to-bash/resources/pip-requirements.txt
RUN cd /pipe-to-bash/


CMD python /pipe-to-bash/run.py