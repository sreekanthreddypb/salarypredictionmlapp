FROM ubuntu:20.04
RUN apt-get update
RUN apt-get install python3 python3-pip -y

RUN pip install flask pandas numpy sklearn pickle5 scikit-learn

COPY . .
#RUN python3 model.py
EXPOSE $PORT
#CMD [ "python3", "server.py"  ]
ENTRYPOINT FLASK_APP=server.py flask run --host 0.0.0.0