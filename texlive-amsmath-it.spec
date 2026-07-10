%global tl_name amsmath-it
%global tl_revision 22930

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Italian translations of some old amsmath documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/translations/amsmath/it
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/amsmath-it.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/amsmath-it.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The documents are: diffs-m.txt of December 1999, and amsmath.faq of
March 2000.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/doc/latex/amsmath-it
%doc %{_datadir}/texmf-dist/doc/latex/amsmath-it/README
%doc %{_datadir}/texmf-dist/doc/latex/amsmath-it/amsmath.faq
%doc %{_datadir}/texmf-dist/doc/latex/amsmath-it/diffs-m_it.txt
