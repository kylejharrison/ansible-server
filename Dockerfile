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

# Install SSH keys

RUN mkdir /root/.ssh
ADD sources/id_rsa* /root/.ssh/

# install setup script

ADD sources/setup-ansible.sh /root/
RUN chmod 755 /root/setup-ansible.sh