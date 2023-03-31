Name:		texlive-amsmath-it
Version:	22930
Release:	2
Summary:	Italian translations of some old AMSmath documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/translations/amsmath/it
License:	NOINFO
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amsmath-it.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amsmath-it.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
