Name:          kinto
Version:       6.0.3
Release:       %{?release_number}%{!?release_number:1}%{?dist}
Summary:       Kinto
License:       ASL 2.0
URL:           http://kinto.readthedocs.io/
               # See https://fedoraproject.org/wiki/Packaging:SourceURL?rd=Packaging/SourceURL#Troublesome_URLs
Source0:       https://github.com/Kinto/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:       kinto.service
BuildRequires: postgresql-devel python36u-devel python36u-pip
Requires:      python36u
AutoReqProv:   no


# RPM's install post processing macro, __os_install_post, includes the brp-python-hardlink script
# (https://github.com/rpm-software-management/rpm/blob/master/scripts/brp-python-hardlink) which fails apparently trying
# to create links to non-existent files. As we don't need the functionality provided by this macro, we disable it (See
# http://livecipher.blogspot.com/2012/06/disable-binary-stripping-in-rpmbuild.html).
%global __os_install_post %{nil}

%define debug_package %{nil}
%define kinto_venv /opt/kinto


%description
Kinto


%prep
%setup -q

# Because venv uses the target directory argument in the #! line of the scripts it installs in its bin directory, and
# because it explicitly fails when the target directory argument is a symlink (see https://github.com/python/cpython/blob/144fff8b900f9d452402a8e47ff79e88e4916d28/Lib/venv/__init__.py#L96),
# the virtual environment must be created outside of the build environment in /opt/kinto. Therefore, as a prerequisite
# to using this spec the root user must create /opt/kinto and set the build user as the owner.
%{__python36} -m venv --clear %{kinto_venv}
%{kinto_venv}/bin/pip install --upgrade pip setuptools wheel


%build
# Because we are installing Kinto as a package (and pinning package dependencies to specific versions is not a best
# practice), but treating it as an application (where a repeatable installation is the goal), we use the Kinto project's
# requirements.txt as constraints for pip install (see https://packaging.python.org/requirements/#install-requires-vs-requirements-files).
%{kinto_venv}/bin/pip install \
  --constraint=%{_builddir}/%{name}-%{version}/requirements.txt \
  %{_builddir}/%{name}-%{version} \
  raven \
  sqlalchemy-postgresql-json==0.5.0 \
  zope.sqlalchemy

%{kinto_venv}/bin/kinto init --backend=postgresql


%install
install -d %{buildroot}%{_unitdir}
install -d %{buildroot}/etc/opt/kinto
install -d %{buildroot}/opt/kinto
cp -r %{kinto_venv}/* %{buildroot}/opt/kinto
install %{SOURCE1} %{buildroot}%{_unitdir}
install %{_builddir}/kinto-%{version}/config/kinto.ini %{buildroot}/etc/opt/kinto


%files
%{_unitdir}
/etc/opt/kinto/kinto.ini
/opt/kinto


%post
/usr/bin/systemctl daemon-reload


%changelog
