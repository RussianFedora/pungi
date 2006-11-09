%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           pungi
Version:        0.1.0
Release:        1%{?dist}
Summary:        Distribution compose tool

Group:          Development/Tools
License:        GPL
URL:            http://linux.duke.edu/projects/%{name}
Source0:        http://linux.duke.edu/projects/%{name}/release/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       anaconda-runtime

BuildArch:      noarch

%description
A tool to create anaconda based installation trees/isos of a set of rpms.


%prep
%setup -q


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

 
%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Authors Changelog COPYING GPL PLAN.gather PLAN.pungi README ToDo
%config(noreplace) %{_sysconfdir}/pungi
# For noarch packages: sitelib
%{python_sitelib}/pypungi
%{_bindir}/pungi


%changelog
* Wed Nov  8 2006 Jesse Keating <jkeating@redhat.com> - 0.1.0-1
- Initial spec
