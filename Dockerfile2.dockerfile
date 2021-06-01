FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -y python3 python3-pip sudo
RUN apt-get install -y vim
RUN apt-get install -y git
RUN mkdir -p ~/genfiles
COPY pseudomonasAeruginosa/genfiles /genfiles