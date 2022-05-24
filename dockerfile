FROM python:3

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ca-certificates \
    git \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/*\
    python3\
    python-pip

ENV WORKDIR /horse/

WORKDIR ${WORKDIR}

COPY ./requirements.txt ${WORKDIR}
COPY ./horseDataScraper/ ${WORKDIR}
COPY ./bin/ ${WORKDIR}

RUN pip install -r requirements.txt
WORKDIR /horse/bin
CMD /bin/sh autoScrape.sh
