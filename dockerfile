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

COPY Pipfile ${WORKDIR}
COPY Pipfile.lock ${WORKDIR}
COPY ./horse/data_downloader/horse/ ${WORKDIR}

RUN pip install pipenv --no-cache-dir && \
    pipenv install --system --deploy && \
    pip3 uninstall -y pipenv virtualenv-clone virtualenv
WORKDIR /horse/bin
CMD /bin/sh autoHorseScrape.sh
