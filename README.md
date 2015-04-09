upaste
======

A simple, plain file storage Python-powered pastebin.

Requirements
------------
* *nix operating system 
* xattr-enabled filesystem, with user xattrs enabled (Linux: `user_xattr` mount option)
* Python 3
* uwsgi

Setup
-----
```bash
# Install requirements.
pip3 install -e requirements.txt
# Modify config.
editor upaste/config.py
editor uwsgi.xml
# Restore xattrs not tracked by git.
setfattr -n user.upaste.language -v python3 upaste/upaste.py

# Now point a uwsgi instance to uwsgi.xml and you're done.
```

License
-------
WTFPL. See LICENSE file.
