Name:		texlive-amsmath-it
Version:	20110329
Release:	1
Summary:	Italian translations of some old AMSmath documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/translations/amsmath/it
License:	NOINFO
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amsmath-it.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amsmath-it.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The documents are: diffs-m.txt of December 1999, and
amsmath.faq of March 2000.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/amsmath-it/README
%doc %{_texmfdistdir}/doc/latex/amsmath-it/amsmath.faq
%doc %{_texmfdistdir}/doc/latex/amsmath-it/diffs-m_it.txt

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
