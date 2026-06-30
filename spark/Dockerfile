FROM bitnamilegacy/spark:3.3.2-debian-11-r9

USER root

RUN apt-get update && apt-get install -y curl && \
    mkdir -p /opt/bitnami/spark/jars && \
    curl -fsSL -o /opt/bitnami/spark/jars/iceberg-spark-runtime-3.3_2.12-1.4.3.jar \
        https://repo1.maven.org/maven2/org/apache/iceberg/iceberg-spark-runtime-3.3_2.12/1.4.3/iceberg-spark-runtime-3.3_2.12-1.4.3.jar && \
    curl -fsSL -o /opt/bitnami/spark/jars/iceberg-aws-bundle-1.4.3.jar \
        https://repo1.maven.org/maven2/org/apache/iceberg/iceberg-aws-bundle/1.4.3/iceberg-aws-bundle-1.4.3.jar && \
    curl -fsSL -o /opt/bitnami/spark/jars/hadoop-aws-3.3.4.jar \
        https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar && \
    curl -fsSL -o /opt/bitnami/spark/jars/aws-java-sdk-bundle-1.12.262.jar \
        https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.262/aws-java-sdk-bundle-1.12.262.jar && \
    curl -fsSL -o /opt/bitnami/spark/jars/postgresql-42.6.0.jar \
        https://repo1.maven.org/maven2/org/postgresql/postgresql/42.6.0/postgresql-42.6.0.jar && \
    curl -fsSL -o /opt/bitnami/spark/jars/spark-nlp_2.12-6.3.2.jar \
        https://repo1.maven.org/maven2/com/johnsnowlabs/nlp/spark-nlp_2.12/6.3.2/spark-nlp_2.12-6.3.2.jar && \
    curl -fsSL -o /opt/bitnami/spark/jars/spark-nlp_2.12-6.4.1.jar \
        https://repo1.maven.org/maven2/com/johnsnowlabs/nlp/spark-nlp_2.12/6.4.1/spark-nlp_2.12-6.4.1.jar && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Python packages for Spark jobs
RUN pip install --no-cache-dir \
    langdetect==1.0.9 \
    reverse-geocode==1.6.6 \
    geopy==2.4.0
    
USER 1001