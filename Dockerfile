# Latest Ubuntu LTS
FROM ubuntu:14.04
MAINTAINER Kyle Harrison <kylejharrison@gmail.com>

#Install ansible

RUN apt-get update && \
    apt-get install --no-install-recommends -y software-properties-common && \
    apt-add-repository ppa:ansible/ansible && \
    apt-get update && \
    apt-get install -y ansible

RUN echo '[local]\nlocalhost\n' > /etc/ansible/hosts

# Install git

RUN apt-get install -y git
RUN git config --global user.email "kylejharrison@gmail.com"
RUN git config --global user.name "Kyle Harrison"

# Install SSH keys

RUN mkdir /root/.ssh
ADD sources/ssh/* /root/.ssh/
RUN chmod 400 /root/.ssh/id_rsa

# install setup scripts

ADD sources/scripts/* /root/
RUN chmod 755 /root/*.sh


# Create playbook directory
RUN mkdir /etc/ansible/playbooks