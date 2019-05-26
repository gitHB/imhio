FROM python:3.5

ENV BROWSER chrome
ENV BASE_URL http://localhost:58001/
ENV DOCKER_SERVER_ADDR http://selenium_chrome:4444/wd/hub
ENV ALLURE_VERSION 2.7.0

WORKDIR /app

ADD requirements /tmp/requirements
RUN pip install -r /tmp/requirements

RUN apt-get update && apt-get install -y software-properties-common tar

RUN mkdir -p /opt/

#install oracle jdk10
RUN cd /tmp \
    && curl -L -k "https://download.java.net/java/GA/jdk10/10.0.1/fb4372174a714e6b8c52526dc134031e/10/openjdk-10.0.1_linux-x64_bin.tar.gz" > jre.tar.gz \
    && tar xzf /tmp/jre.tar.gz -C /opt/ \
    && ls -la /opt/

ENV JAVA_HOME /opt/jdk-10.0.1

ADD https://github.com/allure-framework/allure2/releases/download/${ALLURE_VERSION}/allure-${ALLURE_VERSION}.tgz /tmp/allure.tar.gz
RUN tar xzf /tmp/allure.tar.gz -C /opt/

ENV PATH=$PATH:/opt/allure-${ALLURE_VERSION}/bin

ADD . /app

CMD pytest --alluredir allure-results --browser $BROWSER --base_url $BASE_URL --docker_adr $DOCKER_SERVER_ADDR bdd/main_scenarios.py
