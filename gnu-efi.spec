#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
# autospec version: v10
# autospec commit: 6fa3d52
#
%define keepstatic 1
Name     : gnu-efi
Version  : 3.0.18
Release  : 74
URL      : https://sourceforge.net/projects/gnu-efi/files/gnu-efi-3.0.18.tar.bz2
Source0  : https://sourceforge.net/projects/gnu-efi/files/gnu-efi-3.0.18.tar.bz2
Summary  : EFI development toolkit
Group    : Development/Tools
License  : BSD-2-Clause
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Add-memset-and-memcpy.patch
Patch2: 0002-Remove-werror-flag.patch
Patch3: 0003-Update-PREFIX-and-LIBDIR-for-Clear.patch
Patch4: 0004-Add-memset-and-memcpy-weak-attr.patch
Patch5: 0005-Makefile-add-pkgconfig-generation-code.patch

%description
The files in the "lib" and "inc" subdirectories are using the EFI Application
Toolkit distributed by Intel at http://developer.intel.com/technology/efi

%package dev
Summary: dev components for the gnu-efi package.
Group: Development
Provides: gnu-efi-devel = %{version}-%{release}
Requires: gnu-efi = %{version}-%{release}

%description dev
dev components for the gnu-efi package.


%package staticdev
Summary: staticdev components for the gnu-efi package.
Group: Default
Requires: gnu-efi-dev = %{version}-%{release}

%description staticdev
staticdev components for the gnu-efi package.


%prep
%setup -q -n gnu-efi-3.0.18
cd %{_builddir}/gnu-efi-3.0.18
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1

%build
## build_prepend content
CLEAR_INTERMEDIATE_CFLAGS="`sed -E 's/-Wl,--build-id=sha1//' <<<$CLEAR_INTERMEDIATE_CFLAGS`"
CLEAR_INTERMEDIATE_LDFLAGS="`sed -E 's/-Wl,--build-id=sha1//' <<<$CLEAR_INTERMEDIATE_LDFLAGS`"
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1715717807
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
make


%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1715717807
rm -rf %{buildroot}
## install_prepend content
CLEAR_INTERMEDIATE_CFLAGS="`sed -E 's/-Wl,--build-id=sha1//' <<<$CLEAR_INTERMEDIATE_CFLAGS`"
CLEAR_INTERMEDIATE_LDFLAGS="`sed -E 's/-Wl,--build-id=sha1//' <<<$CLEAR_INTERMEDIATE_LDFLAGS`"
## install_prepend end
export GOAMD64=v2
GOAMD64=v2
%make_install
## install_append content
#cp -a %{buildroot}/usr/lib %{buildroot}/usr/lib64
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib64/crt0-efi-x86_64.o
/usr/lib64/elf_x86_64_efi.lds
/usr/lib64/gnuefi/apps/AllocPages.efi
/usr/lib64/gnuefi/apps/FreePages.efi
/usr/lib64/gnuefi/apps/bltgrid.efi
/usr/lib64/gnuefi/apps/ctors_dtors_priority_test.efi
/usr/lib64/gnuefi/apps/ctors_test.efi
/usr/lib64/gnuefi/apps/debughook.efi
/usr/lib64/gnuefi/apps/debughook.efi.debug
/usr/lib64/gnuefi/apps/drv0.efi
/usr/lib64/gnuefi/apps/drv0_use.efi
/usr/lib64/gnuefi/apps/exit.efi
/usr/lib64/gnuefi/apps/lfbgrid.efi
/usr/lib64/gnuefi/apps/modelist.efi
/usr/lib64/gnuefi/apps/printenv.efi
/usr/lib64/gnuefi/apps/route80h.efi
/usr/lib64/gnuefi/apps/setdbg.efi
/usr/lib64/gnuefi/apps/setjmp.efi
/usr/lib64/gnuefi/apps/t.efi
/usr/lib64/gnuefi/apps/t2.efi
/usr/lib64/gnuefi/apps/t3.efi
/usr/lib64/gnuefi/apps/t4.efi
/usr/lib64/gnuefi/apps/t5.efi
/usr/lib64/gnuefi/apps/t6.efi
/usr/lib64/gnuefi/apps/t7.efi
/usr/lib64/gnuefi/apps/t8.efi
/usr/lib64/gnuefi/apps/tcc.efi
/usr/lib64/gnuefi/apps/unsetdbg.efi

%files dev
%defattr(-,root,root,-)
/usr/include/efi/efi.h
/usr/include/efi/efi_nii.h
/usr/include/efi/efi_pxe.h
/usr/include/efi/efiapi.h
/usr/include/efi/eficompiler.h
/usr/include/efi/eficon.h
/usr/include/efi/eficonex.h
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
/usr/include/efi/efishell.h
/usr/include/efi/efishellintf.h
/usr/include/efi/efistdarg.h
/usr/include/efi/efitcp.h
/usr/include/efi/efiudp.h
/usr/include/efi/efiui.h
/usr/include/efi/lib.h
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
/usr/lib64/pkgconfig/gnu-efi.pc

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libefi.a
/usr/lib64/libgnuefi.a
