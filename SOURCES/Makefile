PREFIX := $(DESTDIR)/usr
BINDIR := $(PREFIX)/bin
MANDIR := $(PREFIX)/share/man

install :
	install -d $(BINDIR) $(MANDIR)/man1
	install -p -m 0755 -o root -g root -t $(BINDIR) rclone
	install -p -m 0644 -o root -g root -t $(MANDIR)/man1 rclone.1
