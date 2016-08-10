FROM ubuntu:16.04

MAINTAINER David Guzman d.guzman [at] ucl.ac.uk

LABEL version="1.0" \
      description="plink 1.07 container" \
      department="UCL BioResource" \
      organisation="University College London"

ENV PLINK_VERSION 1.07
ENV PLINK_ZIP plink-1.07-x86_64.zip
ENV PLINK_DIR /opt/plink-1.07-x86_64

RUN set -ex \
    && apt-get update && apt-get install -y unzip curl \
    && curl -fSL "http://pngu.mgh.harvard.edu/~purcell/plink/dist/plink-1.07-x86_64.zip" -o $PLINK_ZIP \
    && unzip $PLINK_ZIP -d /opt \
    && rm $PLINK_ZIP

RUN cd /usr/local/bin \
    && ln -s $PLINK_DIR/plink plink
    
ENTRYPOINT ["plink","--noweb"]