FROM apache/airflow:2.8.4-python3.8

USER root

# Install OpenJDK 17, required tools, and C++ compiler for Python extensions
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        openjdk-17-jdk \
        ant \
        curl \
        ca-certificates \
        g++ \
        gcc \
        python3-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set JAVA_HOME properly for arm64 (mac users)
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH="${JAVA_HOME}/bin:${PATH}"

# Download JARs to a local directory
RUN mkdir -p /opt/spark/jars && \
    curl -fsSL -o /opt/spark/jars/iceberg-spark-runtime-3.3_2.12-1.4.3.jar \
        https://repo1.maven.org/maven2/org/apache/iceberg/iceberg-spark-runtime-3.3_2.12/1.4.3/iceberg-spark-runtime-3.3_2.12-1.4.3.jar && \
    curl -fsSL -o /opt/spark/jars/iceberg-aws-bundle-1.4.3.jar \
        https://repo1.maven.org/maven2/org/apache/iceberg/iceberg-aws-bundle/1.4.3/iceberg-aws-bundle-1.4.3.jar && \
    curl -fsSL -o /opt/spark/jars/hadoop-aws-3.3.4.jar \
        https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar && \
    curl -fsSL -o /opt/spark/jars/aws-java-sdk-bundle-1.12.262.jar \
        https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.262/aws-java-sdk-bundle-1.12.262.jar && \
    curl -fsSL -o /opt/spark/jars/postgresql-42.6.0.jar \
        https://repo1.maven.org/maven2/org/postgresql/postgresql/42.6.0/postgresql-42.6.0.jar && \
    curl -fsSL -o /opt/spark/jars/spark-nlp-assembly-6.3.2.jar \
        https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/jars/spark-nlp-assembly-6.3.2.jar && \
    curl -fsSL -o /opt/spark/jars/spark-nlp-gpu-assembly-6.3.2.jar \
        https://s3.amazonaws.com/auxdata.johnsnowlabs.com/public/jars/spark-nlp-gpu-assembly-6.3.2.jar

# Switch back to airflow user
USER airflow

COPY requirements.txt /

# Install Python dependencies
RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" -r /requirements.txt