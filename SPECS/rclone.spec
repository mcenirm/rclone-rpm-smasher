Name: rclone
Epoch: 1
Version: 1.38
Release: 1%{?dist}
Summary: rclone - rsync for cloud storage
License: MIT
URL: https://rclone.org/
ExclusiveArch: x86_64
ExclusiveOS: Linux
Source0: https://downloads.rclone.org/%{name}-v%{version}-linux-amd64.zip
Source1: Makefile

%description
Rclone is a command line program to sync files and
directories to and from: Amazon Drive, Amazon S3,
Backblaze B2, Box, Ceph, Dreamhost, Dropbox, FTP,
Google Cloud Storage, Google Drive, HTTP, Hubic,
Memset Memstore, Microsoft Azure Blob Storage,
Microsoft OneDrive, Minio, OVH, Openstack Swift,
Oracle Cloud Storage, QingStor, Rackspace Cloud Files, SFTP,
Wasabi, Yandex Disk, the local filesystem.

%prep
%autosetup -n %{name}-v%{version}-linux-amd64
cp %{SOURCE1} ./

%build

%install
%make_install

%files
%doc README.html README.txt
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Thu Nov  2 2017 Michael McEniry <michael.mceniry@uah.edu> 1.38-1
- Initial packaging as RPM
