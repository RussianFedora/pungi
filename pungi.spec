Name:           pungi
Version:        4.0.3
Release:        1%{?dist}
Summary:        Distribution compose tool

Group:          Development/Tools
License:        GPLv2
URL:            https://pagure.io/pungi
Source0:        https://fedorahosted.org/pungi/attachment/wiki/%{version}/%{name}-%{version}.tar.bz2
# fix https://bugzilla.redhat.com/show_bug.cgi?id=1264570
Patch0:		pungi-lorax.patch
Requires:       createrepo >= 0.4.11
Requires:       yum => 3.4.3-28
Requires:       lorax >= 22.1
Requires:       repoview
Requires:       python-lockfile
Requires:       kobo
Requires:       kobo-rpmlib
Requires:       python-productmd
Requires:       python-kickstart
Requires:       libselinux-python
Requires:       createrepo_c
Requires:       python-lxml
Requires:       koji
Requires:       jigdo
Requires:       cvs
Requires:       yum-utils
Requires:       isomd5sum
Requires:       genisoimage
Requires:       gettext
#Requires:       syslinux
Requires:       git

BuildRequires:  python-devel, python-setuptools

BuildArch:      noarch

%description
A tool to create anaconda based installation trees/isos of a set of rpms.

%prep
%setup -q
%patch0 -p0

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
%{__install} -d $RPM_BUILD_ROOT/var/cache/pungi

%files
%license COPYING GPL
%doc AUTHORS doc/*
%{python_sitelib}/%{name}
%{python_sitelib}/%{name}-%{version}-py?.?.egg-info
%{_bindir}/*
%{_datadir}/pungi
/var/cache/pungi

%changelog
* Sat Oct 24 2015 Arkady L. Shane <ashejn@russianfedora.pro> 4.0.3-1.R
- fix https://bugzilla.redhat.com/show_bug.cgi?id=1264570

* Tue Aug 08 2015 Dennis Gilmore <dennis@ausil.us> 4.0.3-1
- Merge #54 `fix log_info for image_build (fails if image_build is skipped)`
  (lkocman)
- image_build: self.log_info -> self.compose.log_info (lkocman)
- Revert "Added params needed for Atomic compose to LoraxWrapper" (dennis)
- Revert "fix up if/elif in _handle_optional_arg_type" (dennis)
- Add image-build support (lkocman)
- Add translate path support. Useful for passing pungi repos to image-build
  (lkocman)
- import duplicate import of errno from buildinstall (lkocman)
- handle openning missing images.json (image-less compose re-run) (lkocman)
- compose: Add compose_label_major_version(). (lkocman)
- pungi-koji: Don't print traceback if error occurred. (pbabinca)
- More detailed message for unsigned rpms. (tkopecek)
- New config option: product_type (default is 'ga'); Set to 'updates' for
  updates composes. (dmach)
- kojiwrapper: Add get_signed_wrapped_rpms_paths() and get_build_nvrs()
  methods. (tmlcoch)
- live_images: Copy built wrapped rpms from koji into compose. (tmlcoch)
- kojiwrapper: Add get_wrapped_rpm_path() function. (tmlcoch)
- live_images: Allow custom name prefix for live ISOs. (tmlcoch)
- Do not require enabled runroot option for live_images phase. (tmlcoch)
- Support for rpm wrapped live images. (tmlcoch)
- Remove redundant line in variants wrapper. (tmlcoch)
- Merge #36 `Add params needed for Atomic compose to LoraxWrapper` (admiller)
- live_images: replace hardcoded path substition with translate_path() call
  (lkocman)
- live_images fix reference from koji to koji_wrapper (lkocman)
- fix up if/elif in _handle_optional_arg_type (admiller)
- Added params needed for Atomic compose to LoraxWrapper (admiller)
- Merge #24 `Fix empty repodata when hash directories were enabled. ` (dmach)
- createrepo: Fix empty repodata when hash directories were enabled. (dmach)

* Fri Jul 24 2015 Dennis Gilmore <dennis@ausil.us> - 4.0.2-1
- Merge #23 `fix treeinfo checksums` (dmach)
- Fix treeinfo checksums. (dmach)
- add basic setup for making arm iso's (dennis)
- gather: Implement hashed directories. (dmach)
- createiso: Add createiso_skip options to skip createiso on any variant/arch.
  (dmach)
- Fix buildinstall for armhfp. (dmach)
- Fix and document productimg phase. (dmach)
- Add armhfp arch tests. (dmach)
- Document configuration options. (dmach)
- Add dependency of 'runroot' config option on 'koji_profile'. (dmach)
- Rename product_* to release_*. (dmach)
- Implement koji profiles. (dmach)
- Drop repoclosure-%arch tests. (dmach)
- Config option create_optional_isos now defaults to False. (dmach)
- Change createrepo config options defaults. (dmach)
- Rewrite documentation to Sphinx. (dmach)
- Fix test data, improve Makefile. (dmach)
- Update GPL to latest version from https://www.gnu.org/licenses/gpl-2.0.txt
  (dmach)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Dennis Gilmore <dennis@ausil.us> - 4.0.1-1
- wrap check for selinux enforcing in a try except (dennis)
- pull in gather.py patches from dmach for test compose (admiller)
- Add some basic testing, dummy rpm creation, and a testing README (admiller)
- pungi-koji: use logger instead of print when it's available (lkocman)
- fix incorrect reference to variable 'product_is_layered' (lkocman)
- pungi-koji: fix bad module path to verify_label() (lkocman)
- update the package Requires to ensure we have everything installed to run
  pungi-koji (dennis)
- update the package to be installed for productmd to python-productmd (dennis)

* Sun Jun 07 2015 Dennis Gilmore <dennis@ausil.us> - 4.0-0.9.20150607.gitef7c78c
- update docs now devel-4-pungi is merged to master, minor spelling fixes
  (pbrobinson)
- Fix remaining productmd issues. (dmach)
- Revert "refactor metadata.py to use productmd's compose.dump for composeinfo"
  (dmach)
- Fix LoraxTreeInfo class inheritance. (dmach)
- Fix pungi -> pungi_wrapper namespace issue. (dmach)
- fix arg order for checksums.add (admiller)
- update for productmd checksums.add to TreeInfo (admiller)
- fix product -> release namespace change for productmd (admiller)
- update arch manifest.add config order for productmd api call (admiller)
- update for new productmd named args to rpms (admiller)
- fix pungi vs pungi_wrapper namespacing in method_deps.py (admiller)
- add createrepo_c Requires to pungi.spec (admiller)
- add comps_filter (admiller)
- refactor metadata.py to use productmd's compose.dump for composeinfo instead
  of pungi compose_to_composeinfo (admiller)
- Update compose, phases{buildinstall,createiso,gather/__ini__} to use correct
  productmd API calls (admiller)
- Use libselinux-python instead of subprocess (lmacken)
- Add README for contributors (admiller)

* Wed May 20 2015 Dennis Gilmore <dennis@ausil.us> - 4.0-0.8.20150520.gitff77a92
- fix up bad += from early test of implementing different iso labels based on
  if there is a variant or not (dennis)

* Wed May 20 2015 Dennis Gilmore <dennis@ausil.us> - 4.0-0.7.20150520.gitdc1be3e
- make sure we treat the isfinal option as a boolean when fetching it (dennis)
- if there is a variant use it in the volume id and shorten it. this will make
  each producst install tree have different volume ids for their isos (dennis)
- fix up productmd import in the executable (dennis)
- fixup productmd imports for changes with open sourcing (dennis)
- tell the scm wrapper to do an absolute import otherwise we hit a circular dep
  issue and things go wonky (dennis)
- include the dtd files in /usr/share/pungi (dennis)
- add missing ) causing a syntax error (dennis)
- fix up the productmd imports to import the function from the common module
  (dennis)
- fix up typo in getting arch for the lorax log file (dennis)

* Sat Mar 14 2015 Dennis Gilmore <dennis@ausil.us> - 4.0-0.6.20150314.gitd337c34
- update the git snapshot to pick up some fixes

* Fri Mar 13 2015 Dennis Gilmore <dennis@ausil.us> - 4.0-0.5.git18d4d2e
- update Requires for rename of python-productmd

* Thu Mar 12 2015 Dennis Gilmore <dennis@ausil.us> - 4.0-0.4.git18d4d2e
- fix up the pungi logging by putting the arch in the log file name (dennis)
- change pypungi imports to pungi (dennis)
- spec file cleanups (dennis)

* Thu Mar 12 2015 Dennis Gilmore <dennis@ausil.us> - 4.0-0.3.gita3158ec
- rename binaries (dennis)
- Add the option to pass a custom path for the multilib config files (bcl)
- Call lorax as a process not a library (bcl)
- Close child fds when using subprocess (bcl)
- fixup setup.py and MANIFEST.in to make a useable tarball (dennis)
- switch to BSD style hashes for the iso checksums (dennis)
- refactor to get better data into .treeinfo (dennis)
- Initial code merge for Pungi 4.0. (dmach)
- Initial changes for Pungi 4.0. (dmach)
- Add --nomacboot option (csieh)

* Thu Mar 12 2015 Dennis Gilmore <dennis@ausil.us> - 4.0-0.2.git320724e
- update git snapshot to switch to executing lorax since it is using dnf

* Thu Mar 12 2015 Dennis Gilmore <dennis@ausil.us> - 4.0-0.1.git64b6c80
- update to the pungi 4.0 dev branch
