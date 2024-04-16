#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : gnu-efi
Version  : 3.0.15
Release  : 64
URL      : https://sourceforge.net/projects/gnu-efi/files/gnu-efi-3.0.15.tar.bz2
Source0  : https://sourceforge.net/projects/gnu-efi/files/gnu-efi-3.0.15.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Patch1: memset.patch
Patch2: nowerror.patch
Patch3: nolocal.patch
Patch4: 0001-add-missing-rule-to-makefile.patch
Patch5: weak.patch
Patch6: 0002-Makefile-add-pkgconfig-generation-code.patch

%description
The files in the "lib" and "inc" subdirectories are using the EFI Application
Toolkit distributed by Intel at http://developer.intel.com/technology/efi

%prep
%setup -q -n gnu-efi-3.0.15
cd %{_builddir}/gnu-efi-3.0.15
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1672175232
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
make


%install
export SOURCE_DATE_EPOCH=1672175232
rm -rf %{buildroot}
%make_install
## install_append content
#cp -a %{buildroot}/usr/lib %{buildroot}/usr/lib64
## install_append end

%files
%defattr(-,root,root,-)
