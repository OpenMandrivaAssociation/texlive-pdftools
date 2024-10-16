# revision 34192
# category TLCore
# catalog-ctan /support/xpdfopen
# catalog-date 2014-05-17 07:55:44 +0200
# catalog-license pd
# catalog-version 0.84
Name:		texlive-pdftools
Version:	0.84
Release:	6
Summary:	PDF-related utilities, including PostScript-to-PDF conversion
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/xpdfopen
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdftools.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdftools.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-pdftools.bin

%description
The command-line programs pdfopen and pdfclose allow you to
control the X Window System version of Adobe's Acrobat Reader
from the command line or from within a (shell) script. The
programs work with Acrobat Reader 5, 7, 8 and 9 for Linux, xpdf
and evince. This version derives from one written by Fabrice
Popineau for Microsoft operating systems.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/e2pall
%{_bindir}/pdfatfi
%{_bindir}/ps4pdf
%{_texmfdistdir}/scripts/texlive/e2pall.pl
%doc %{_mandir}/man1/e2pall.1*
%doc %{_texmfdistdir}/doc/man/man1/e2pall.man1.pdf
%doc %{_mandir}/man1/pdfclose.1*
%doc %{_texmfdistdir}/doc/man/man1/pdfclose.man1.pdf
%doc %{_mandir}/man1/pdfopen.1*
%doc %{_texmfdistdir}/doc/man/man1/pdfopen.man1.pdf
%doc %{_mandir}/man1/pdftosrc.1*
%doc %{_texmfdistdir}/doc/man/man1/pdftosrc.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/texlive/e2pall.pl e2pall
    ln -sf %{_texmfdistdir}/scripts/oberdiek/pdfatfi.pl pdfatfi
    ln -sf %{_texmfdistdir}/scripts/pst-pdf/ps4pdf ps4pdf
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
