Name:		texlive-insbox
Version:	34299
Release:	1
Summary:	A TeX macro for inserting pictures/boxes into paragraphs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/insbox
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/insbox.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/insbox.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive insbox package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/insbox
%doc %{_texmfdistdir}/doc/generic/insbox

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
