# revision 22930
# category Package
# catalog-ctan /info/translations/amsmath/it
# catalog-date 2011-03-29 16:35:51 +0200
# catalog-license noinfo
# catalog-version undef
Name:		texlive-amsmath-it
Version:	20110329
Release:	6
Summary:	Italian translations of some old AMSmath documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/translations/amsmath/it
License:	NOINFO
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amsmath-it.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amsmath-it.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20110329-2
+ Revision: 749226
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110329-1
+ Revision: 717826
- texlive-amsmath-it
- texlive-amsmath-it
- texlive-amsmath-it
- texlive-amsmath-it

