FROM tikhonovapolly/phigaro:latest
RUN /bin/bash -c '/root/miniconda3/bin/pip install phigaro --upgrade'
RUN apt-get update 
RUN apt-get install -y python3 python3-pip sudo
RUN apt-get install -y vim
RUN apt-get install -y git
RUN mkdir -p ~/fastafiles
COPY pseudomonasAeruginosa/fastafiles /fastafiles