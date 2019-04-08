FROM tensorflow/tensorflow:latest
RUN pip install kafka-python
RUN pip install flask
ADD /util/* /util/
ADD python_app.py /
ENTRYPOINT ["python","/python_app.py"]
CMD []

