%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           pungi
Version:        0.3.2
Release:        1%{?dist}
Summary:        Distribution compose tool

Group:          Development/Tools
License:        GPL
URL:            http://hosted.fedoraproject.org/projects/pungi
Source0:        http://linux.duke.edu/projects/%{name}/release/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       anaconda-runtime, yum => 3.0.3
BuildRequires:  python-devel

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
%doc Authors Changelog COPYING GPL README ToDo
%config(noreplace) %{_sysconfdir}/pungi
# For noarch packages: sitelib
%{python_sitelib}/pypungi
%{_bindir}/pungi


%changelog
* Mon May 21 2007 Jesse Keating <jkeating@redhat.coM> - 0.3.2-1
- Don't quote ISO label, not running mkisofs in shell
- Apply sparc patches (spot)
- Fix cached downloads comparing correctly
- Shorten 'development' to 'devel' in default config, more space for mkisofs
- Handle config file missing better (jgranado)

* Fri Apr 06 2007 Jesse Keating <jkeating@redhat.com> - 0.3.1-1
- Fix comments in default config file

* Mon Apr 02 2007 Jesse Keating <jkeating@redhat.com> - 0.3.0-1
- Remove incompatible fc6 config files
- Update default config file with comments / new options
- Update comps file
- Enable source iso building again.
- Don't try a rescue if the script doesn't exist (prarit)
- Pass flavor off to buildinstall if it is set (wwoods)
- Fix a logic flaw in the depsolving loop
- Use yum's built in exclude handling
- Use yum's built in conditional handling for things from comps
- Do excludes before group handling.
- Get all potential matches for deps, let install time figure
  the best one to use.
- Work around false positive 'unmatched' packages (globs are fun)
- Change how depsolving is done
  - Get all potential matches for a dep, instead of our 'best'
    our 'best' may not be the same as install time best.
  - Remove anaconda code, use direct yum functions to get deps
  - Use a True/False flag to depsolve instead of iterating over
    a dict.
  - Log what packages are being added for which reasons.
- Do things faster/smarter if we've only asked for one disc
- log the rpm2cpio stuff for release notes
- correctly capture errors from subprocess

* Fri Mar 09 2007 Jesse Keating <jkeating@redhat.com> - 0.2.8-1
- Call createrepo ourselves for the tree, not buildinstall's job
- Convert from commands to subprocess for things we call out
- Add kickstart %packages syntax support to package manifest
- Make the list we hand off to yum to search for as unique as we can

* Wed Feb 28 2007 Jesse Keating <jkeating@redhat.com> - 0.2.7-1
- Fix gathering of srpms (thanks skvidal)
- Update comps from F7 Test2

* Thu Feb 22 2007 Jesse Keating <jkeating@redhat.com> - 0.2.6-1
- Don't use TMPDIR with buildinstall, it is broken

* Wed Feb 21 2007 Jesse Keating <jkeating@redhat.com> - 0.2.5-1
- Make use of anaconda's TMPDIR support
- Put yum tempdirs in the workdir
- Add a version option to cli arguments
- Make cdsize a config option

* Thu Feb 15 2007 Jesse Keating <jkeating@redhat.com> - 0.2.4-1
- Add support for globbing in manifest
- Add new Make targets (Essien Ita Essien)
- Add runtime flags for doing specific stages of the compose (Essien Ita Essien)
- Add ability to define destdir on the cli to override conf file
- Clean up optionparse stuff, print usage if arg list is too small
- Fix part of the patch from Essien
- Add Contributors to the Authors file
- Adjust the Makefile so that srpm doesn't cause a tag
- Merged changes from Will Woods
  - Write out some tree description files
  - Don't traceback on existing files in download area (not sure this will stay)
- Style fixed some stuff from Will
- Add logging patch from jbowes
- Various logging tweaks
- Use -d flag in createrepo for sqlite blobs
- Add pydoc stuff to various functions
- Support comments in the package manifest

* Tue Feb 06 2007 Jesse Keating <jkeating@redhat.com> - 0.2.3-1
- Be able to opt-out of a bugurl since buildinstall supports this
- Make isodir an object of pungi (wwoods)
- yum bestPackagesFromList takes an arch argument. Fixes ppc64 bug
- Don't use 'returnSimple' anymore, deprecated in yum api

* Mon Jan 29 2007 Jesse Keating <jkeating@redhat.com> - 0.2.2-1
- Update the comps file again from F7
- Fix the ppc boot flags
- Clean up SRPM-disc junk
- add bugurl config option for anaconda betanag

* Thu Jan 25 2007 Jesse Keating <jkeating@redhat.com> - 0.2.1-1
- Add a "flavor" option (such as Desktop)
- Move packageorder file into workdir
- Update the comps file from F7

* Wed Jan 24 2007 Jesse Keating <jkeating@redhat.com> - 0.2.0-1
- Now use a manifest to determine what to pull in, not comps itself
- Add a minimal-manifest for test composes
- Add current F7 comps file for test composes
- Use some anaconda code to depsolve, gets better (and more common) results
- Bump the iso size to what was used in FC6
- Move splittree workdirs into work/ at the end of the run
- Remove our splittree for rawhide
- Remove old main() sections from pungi.py and gather.py
- Require yum 3.0.3 or newer
- Add rescueCD support

* Wed Dec 13 2006 Jesse Keating <jkeating@redhat.com> - 0.1.2-1
- Fix a bug in DVD repodata
- Add correct ppc boot args
- Set ppc arch correctly

* Mon Dec 11 2006 Jesse Keating <jkeating@redhat.com> - 0.1.1-2
- Need BR python-devel in rawhide

* Mon Dec 11 2006 Jesse Keating <jkeating@redhat.com> - 0.1.1-1
- Update to 0.1.1
- Add ability to get srpms
- Add ability to get relnote files
- Use a config file system
- Clean up some docs
- Add config files for composing FC6 respins

* Wed Nov  8 2006 Jesse Keating <jkeating@redhat.com> - 0.1.0-1
- Initial spec
