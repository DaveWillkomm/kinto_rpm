Name:          kinto
Version:       5.3.2
Release:       %{?release_number}%{!?release_number:1}%{?dist}
Summary:       Kinto
License:       ASL 2.0
URL:           http://kinto.readthedocs.io/
               # See https://fedoraproject.org/wiki/Packaging:SourceURL?rd=Packaging/SourceURL#Troublesome_URLs
Source0:       https://github.com/Kinto/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires: postgresql-devel python35u-devel python35u-pip


# RPM's install post processing macro, __os_install_post, includes the brp-python-hardlink script
# (https://github.com/rpm-software-management/rpm/blob/master/scripts/brp-python-hardlink) which fails apparently trying
# to create links to non-existent files. As we don't need the functionality provided by this macro, we disable it (See
# http://livecipher.blogspot.com/2012/06/disable-binary-stripping-in-rpmbuild.html).
%global __os_install_post %{nil}


# RPM's automatic dependency script, find-requires (https://github.com/rpm-software-management/rpm/blob/master/scripts/find-requires),
# wants to include /opt/kinto_rpm/BUILD/venv/bin/python3.5, which proves problematic. So we simply exclude it (see
# https://fedoraproject.org/wiki/Packaging:AutoProvidesAndRequiresFiltering#Filtering_provides_and_requires_after_scanning).
%global __requires_exclude ^%{_builddir}/venv/bin/python.*$


%define debug_package %{nil}


%description
Kinto


%prep
%setup -q
%{__python35u} -m venv --clear %{_builddir}/venv
%{_builddir}/venv/bin/pip install --upgrade pip setuptools wheel


%build
# Because we are installing Kinto as a package (and pinning package dependencies to specific versions is not a best
# practice), but treating it as an application (where a repeatable installation is the goal), we use the Kinto project's
# requirements.txt as constraints for pip install (see https://packaging.python.org/requirements/#install-requires-vs-requirements-files).
%{_builddir}/venv/bin/pip install \
  --constraint=%{_builddir}/%{name}-%{version}/requirements.txt \
  %{_builddir}/%{name}-%{version} \
  sqlalchemy-postgresql-json==0.4.7 \
  zope.sqlalchemy==0.7.7

%{_builddir}/venv/bin/kinto init --backend=postgresql


%install
install -d %{buildroot}/etc/opt/kinto
install -d %{buildroot}/opt/kinto
cp -R %{_builddir}/venv/* %{buildroot}/opt/kinto
install %{_builddir}/kinto-%{version}/config/kinto.ini %{buildroot}/etc/opt/kinto


%files
/opt/kinto
/etc/opt/kinto/kinto.ini


%changelog
