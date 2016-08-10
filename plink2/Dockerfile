FROM ubuntu:16.04

MAINTAINER David Guzman d.guzman [at] ucl.ac.uk

LABEL version="1.0" \
      description="plink 1.90 beta container" \
      department="UCL BioResource" \
      organisation="University College London"

ENV PLINK_VERSION 1.90
ENV PLINK_ZIP plink_linux_x86_64.zip
ENV PLINK_DIR /opt/plink2

RUN set -ex \
    && apt-get update && apt-get install -y unzip curl \
    && curl -fSL "https://www.cog-genomics.org/static/bin/plink160808/plink_linux_x86_64.zip" -o $PLINK_ZIP \
    && mkdir $PLINK_DIR \
    && unzip $PLINK_ZIP -d $PLINK_DIR \
    && rm $PLINK_ZIP

RUN cd /usr/local/bin \
    && ln -s $PLINK_DIR/plink plink
    
ENTRYPOINT ["plink"]