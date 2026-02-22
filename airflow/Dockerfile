# Custom image for airflow

FROM apache/airflow:2.8.4-python3.9

USER root

RUN apt-get update -y && \
    apt-get install -y wget apt-transport-https gnupg && \
    wget -qO - https://packages.adoptium.net/artifactory/api/gpg/key/public | gpg --dearmor -o /etc/apt/trusted.gpg.d/adoptium.gpg && \
    echo "deb https://packages.adoptium.net/artifactory/deb $(. /etc/os-release && echo $VERSION_CODENAME) main" \
        > /etc/apt/sources.list.d/adoptium.list && \
    apt-get update -y && \
    apt-get install -y temurin-8-jdk

ENV JAVA_HOME=/usr/lib/jvm/temurin-8-arm64
ENV PATH="${JAVA_HOME}/bin:${PATH}"

USER airflow

# Install Spark + Spark NLP
RUN pip install spark-nlp==6.3.2 pyspark==3.3.1