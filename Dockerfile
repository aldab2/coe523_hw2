FROM ubuntu:18.04

# Store the test apps in /app 
WORKDIR /app
RUN apt update && apt upgrade -y
RUN apt install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa -y
RUN apt install python3.10 -y
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 2
RUN apt-get install curl -y
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10
RUN python3.10 -m pip install --upgrade pip
RUN pip install rticonnextdds_connector --root-user-action=ignore
# Copy the apps and QoS file
COPY . /app
# Add the apps to the PATH
ENV PATH $PATH:/app