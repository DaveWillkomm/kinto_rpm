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

    sudo /home/vagrant/kinto_rpm/bin/build/buildrpm.sh
        
Testing a Build
===============
Copy the package from the host to the test VM:

    vagrant scp RPMS/x86_64/kinto-4.1.1-1.el7.centos.x86_64.rpm test:/home/vagrant
    
SSH into the test VM:

    vagrant ssh test
    
Install the package on the test VM:

    sudo yum -y install kinto-4.1.1-1.el7.centos.x86_64.rpm
    
Quickie test:

    /opt/kinto/bin/kinto init --backend memory
    /opt/kinto/bin/kinto start
    curl http://localhost:8888/v1/
    
How to Update to a New Version of Kinto
=======================================
1. Replace the source tarball
2. Update `kinto.spec`'s `Version` tag to reflect the source version number
3. Update the Python packages if applicable (see _A Note..._ below)
3. Ensure that `sqlalchemy-postgresql-json`'s version in the build's `pip install` command is appropriate.
   
A Note About Choosing the Python Version
========================================
The Python version is chosen by referring to Kinto's `setup.py` for the tagged version being packaged. For example,
Kinto 5.3.0's [`setup.py`](https://github.com/Kinto/kinto/blob/5.3.0/setup.py#L103) indicates that Python 3.5.0 is the
most current supported version.

References
==========
* [RPM documentation](http://rpm.org/documentation.html)
* [Maximum RPM](http://rpm.org/max-rpm-snapshot/)
* [RPM source](https://github.com/rpm-software-management/rpm)
* [Python: Creating Built Distributions](https://docs.python.org/3/distutils/builtdist.html)
* [Fedora Packaging Guidelines for Python](https://fedoraproject.org/wiki/Packaging:Python)
* [Creating and Modifying systemd Unit Files](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/7/html/System_Administrators_Guide/sect-Managing_Services_with_systemd-Unit_Files.html)
