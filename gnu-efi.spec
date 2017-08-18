#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : gnu-efi
Version  : 3.0.6
Release  : 37
URL      : https://sourceforge.net/projects/gnu-efi/files/gnu-efi-3.0.6.tar.bz2
Source0  : https://sourceforge.net/projects/gnu-efi/files/gnu-efi-3.0.6.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Patch1: memset.patch
Patch2: nowerror.patch
Patch3: nolocal.patch
Patch4: 0001-add-missing-rule-to-makefile.patch

%description
The files in the "lib" and "inc" subdirectories are using the EFI Application
Toolkit distributed by Intel at http://developer.intel.com/technology/efi

%package dev
Summary: dev components for the gnu-efi package.
Group: Development
Provides: gnu-efi-devel

%description dev
dev components for the gnu-efi package.


%prep
%setup -q -n gnu-efi-3.0.6
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1503011465
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1503011465
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/crt0-efi-x86_64.o
/usr/lib64/elf_x86_64_efi.lds

%files dev
%defattr(-,root,root,-)
/usr/include/efi/efi.h
/usr/include/efi/efi_nii.h
/usr/include/efi/efi_pxe.h
/usr/include/efi/efiapi.h
/usr/include/efi/eficompiler.h
/usr/include/efi/eficon.h
/usr/include/efi/efidebug.h
/usr/include/efi/efidef.h
/usr/include/efi/efidevp.h
/usr/include/efi/efierr.h
/usr/include/efi/efifs.h
/usr/include/efi/efigpt.h
/usr/include/efi/efiip.h
/usr/include/efi/efilib.h
/usr/include/efi/efilink.h
/usr/include/efi/efinet.h
/usr/include/efi/efipart.h
/usr/include/efi/efipciio.h
/usr/include/efi/efipoint.h
/usr/include/efi/efiprot.h
/usr/include/efi/efipxebc.h
/usr/include/efi/efirtlib.h
/usr/include/efi/efiser.h
/usr/include/efi/efisetjmp.h
/usr/include/efi/efishellintf.h
/usr/include/efi/efishellparm.h
/usr/include/efi/efistdarg.h
/usr/include/efi/efitcp.h
/usr/include/efi/efiudp.h
/usr/include/efi/efiui.h
/usr/include/efi/libsmbios.h
/usr/include/efi/pci22.h
/usr/include/efi/protocol/adapterdebug.h
/usr/include/efi/protocol/eficonsplit.h
/usr/include/efi/protocol/efidbg.h
/usr/include/efi/protocol/efivar.h
/usr/include/efi/protocol/intload.h
/usr/include/efi/protocol/legacyboot.h
/usr/include/efi/protocol/piflash64.h
/usr/include/efi/protocol/vgaclass.h
/usr/include/efi/romload.h
/usr/include/efi/x86_64/efibind.h
/usr/include/efi/x86_64/efilibplat.h
/usr/include/efi/x86_64/efisetjmp_arch.h
/usr/include/efi/x86_64/pe.h
/usr/lib64/*.a
