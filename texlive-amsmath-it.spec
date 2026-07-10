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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The documents are: diffs-m.txt of December 1999, and amsmath.faq of
March 2000.

