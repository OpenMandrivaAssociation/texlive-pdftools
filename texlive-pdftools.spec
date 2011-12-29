# revision 23089
# category TLCore
# catalog-ctan /support/xpdfopen
# catalog-date 2011-05-31 15:00:33 +0200
# catalog-license pd
# catalog-version 0.82
Name:		texlive-pdftools
Version:	0.82
Release:	1
Summary:	PDF-related utilities, including PostScript-to-PDF conversion
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/xpdfopen
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdftools.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pdftools.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-oberdiek
Requires:	texlive-pdftools.bin
Requires:	texlive-pst-pdf

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
%{_texmfdir}/scripts/tetex/e2pall.pl
%doc %{_mandir}/man1/e2pall.1*
%doc %{_texmfdir}/doc/man/man1/e2pall.man1.pdf
%doc %{_mandir}/man1/pdfclose.1*
%doc %{_texmfdir}/doc/man/man1/pdfclose.man1.pdf
%doc %{_mandir}/man1/pdfopen.1*
%doc %{_texmfdir}/doc/man/man1/pdfopen.man1.pdf
%doc %{_mandir}/man1/pdftosrc.1*
%doc %{_texmfdir}/doc/man/man1/pdftosrc.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdir}/scripts/tetex/e2pall.pl e2pall
    ln -sf %{_texmfdistdir}/scripts/oberdiek/pdfatfi.pl pdfatfi
    ln -sf %{_texmfdistdir}/scripts/pst-pdf/ps4pdf ps4pdf
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
