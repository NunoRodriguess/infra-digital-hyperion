FROM apache/airflow:2.8.4-python3.8

USER root

# Install OpenJDK 17 and required tools
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        openjdk-17-jdk \
        ant \
        curl \
        ca-certificates && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set JAVA_HOME properly for arm64 (mac users)
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-arm64
ENV PATH="${JAVA_HOME}/bin:${PATH}"

# Switch back to airflow user
USER airflow

COPY requirements.txt /

# Install Python dependencies
RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" -r /requirements.txt