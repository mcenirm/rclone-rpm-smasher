all: rpm

# Most recent as of 2017-11-02
VERSION := 1.38
NAME := rclone
FILE := $(NAME)-v$(VERSION)-linux-amd64.zip
ARCH := x86_64
RELEASE := 1
DISTRO := el7.centos
SPEC := SPECS/$(NAME).spec
RPM := RPMS/$(ARCH)/$(NAME)-$(VERSION)-$(RELEASE).$(DISTRO).$(ARCH).rpm
SOURCES := SOURCES/$(FILE) SOURCES/Makefile


.PHONY : rpm sources

rpm : $(RPM)

sources : $(SOURCES)


SOURCES/$(FILE) :
	spectool -g -R $(SPEC)


$(RPM) : $(SPEC) $(SOURCES)
	rpmbuild -ba $(SPEC)
