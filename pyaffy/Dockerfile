FROM python:3.5

MAINTAINER David Guzman d.guzman [at] ucl.ac.uk

ENV PYAFFY_DIR /opt/pyaffy

RUN mkdir $PYAFFY_DIR

COPY fixfam.py $PYAFFY_DIR
COPY unphasable.py $PYAFFY_DIR

RUN set -ex \
    && pip install numpy \
    && pip install pandas \
    && cd /usr/local/bin \
    && chmod +x $PYAFFY_DIR/fixfam.py \
    && chmod +x $PYAFFY_DIR/unphasable.py \
    && ln -s $PYAFFY_DIR/fixfam.py fixfam \
    && ln -s $PYAFFY_DIR/unphasable.py unphasable

CMD ["python"]