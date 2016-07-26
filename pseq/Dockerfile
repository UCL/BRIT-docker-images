FROM python:3.5

MAINTAINER David Guzman d.guzman [at] ucl.ac.uk

ENV PLINKSEQ_VERSION 0.10
ENV PLINKSEQ_ZIP plinkseq-x86_64-0.10.zip
ENV PLINKSEQ_DIR /opt/plinkseq-0.10

RUN set -ex \
    && apt-get update && apt-get install -y unzip \
    && curl -fSL "http://psychgen.u.hpc.mssm.edu/plinkseq_downloads/plinkseq-x86_64-0.10.zip" -o $PLINKSEQ_ZIP \
    && unzip $PLINKSEQ_ZIP -d /opt \
    && rm $PLINKSEQ_ZIP

RUN cd /usr/local/bin \
    && ln -s $PLINKSEQ_DIR/pseq pseq \
    && ln -s $PLINKSEQ_DIR/smp smp \
    && ln -s $PLINKSEQ_DIR/mm mm \
    && ln -s $PLINKSEQ_DIR/behead behead \
    && ln -s $PLINKSEQ_DIR/gcol gcol \
    && ln -s $PLINKSEQ_DIR/browser browser \
    && ln -s $PLINKSEQ_DIR/mongoose mongoose \
    && ln -s $PLINKSEQ_DIR/pbrowse pbrowse
    
CMD ["pseq"]