Kinto RPM
=========
This project contains tooling to create [Kinto](http://kinto.readthedocs.io) RPMs targeting CentOS and using the
PostgreSQL [backend](http://kinto.readthedocs.io/en/stable/configuration/settings.html#backends).

Development Environment Setup
=============================
Vagrant is used for developing and testing the RPMs, and the build VM can be set up on macOS using Homebrew by executing
the following script. Please read it before executing it in order to understand the changes it will make to your system.

    bin/setup.sh
    
After running the above, a separate test VM can be provisioned with the following command.

    vagrant up test
    
Running a Build
===============
From the host machine:

    bin/buildrpm.sh
    
On the guest build VM:

    /opt/kinto_rpm/bin/build/buildrpm.sh
    
How to Update to a New Version of Kinto
=======================================
1. Replace the source tarball
2. Update `kinto.spec`'s `Version` tag to reflect the source version number
3. Update the Python packages if applicable (see _A Note..._ below)
3. Ensure the version of zope.sqlalchemy in the build's `pip install` command matches that in Kinto's `requirements.txt`
   and that `sqlalchemy-postgresql-json`'s version is appropriate.
   
A Note About Choosing the Python Version
========================================
The Python version is chosen by referring to Kinto's `setup.py` for the tagged version being packaged. For example,
Kinto 5.3.0's [`setup.py`](https://github.com/Kinto/kinto/blob/5.3.0/setup.py#L103) indicates that Python 3.5.0 is the
most current supported version.

References
==========
* [RPM documentation](http://rpm.org/documentation.html)
* [Maximum RPM](http://rpm.org/max-rpm-snapshot/)
* [Python: Creating Built Distributions](https://docs.python.org/3/distutils/builtdist.html)
* [Fedora Packaging Guidelines for Python](https://fedoraproject.org/wiki/Packaging:Python)
