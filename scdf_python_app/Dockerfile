FROM springcloud/openjdk:latest

RUN apt-get update && apt-get install --no-install-recommends -y \
    python-pip && rm -rf /var/lib/apt/lists/*

RUN pip install kafka-python
RUN pip install flask

ADD /util/* /util/
ADD python_app.py /
ENTRYPOINT ["python","/python_app.py"]
CMD []