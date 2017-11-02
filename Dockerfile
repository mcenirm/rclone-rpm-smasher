FROM centos:7
RUN yum -y install \
    make \
    rpmdevtools
RUN useradd maker
USER maker
VOLUME "/home/maker/rpmbuild"
WORKDIR "/home/maker/rpmbuild"
CMD "make"
