FROM ubuntu:18.04

# Mode non interractif
ENV DEBIAN_FRONTEND=noninteractive 

# Installation des packets utiles
RUN  apt-get update \
	&& apt-get install libasound2 git-core git-gui git-doc python3 python3-pip software-properties-common apt-transport-https wget tar sudo -y

# Ajout du repository de VSCode et installation de VSCode
RUN wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | apt-key add - \
	&& add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" \
	&& apt update \
	&& apt install code -y

# Installation de pygame 
RUN pip3 install pygame

# Installation de GitKraken
RUN wget https://release.gitkraken.com/linux/gitkraken-amd64.tar.gz
RUN tar -xvzf gitkraken-amd64.tar.gz
RUN rm gitkraken-amd64.tar.gz

RUN export uid=1000 gid=1000 && \
    mkdir -p /home/developer && \
    echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
    echo "developer:x:${uid}:" >> /etc/group && \
    echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \
    chmod 0440 /etc/sudoers.d/developer && \
    chown ${uid}:${gid} -R /home/developer

USER developer

# Définition du dossier courrant 
WORKDIR /aquarium
