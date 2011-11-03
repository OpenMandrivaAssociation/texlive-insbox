# revision 17694
# category Package
# catalog-ctan /macros/generic/insbox
# catalog-date 2007-01-07 15:47:33 +0100
# catalog-license pd
# catalog-version 2.2
Name:		texlive-insbox
Version:	2.2
Release:	1
Summary:	A TeX macro for inserting pictures/boxes into paragraphs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/insbox
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/insbox.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/insbox.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
TeXLive insbox package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/insbox/insbox.tex
%doc %{_texmfdistdir}/doc/generic/insbox/demo.tex
%doc %{_texmfdistdir}/doc/generic/insbox/pic1.eps
%doc %{_texmfdistdir}/doc/generic/insbox/pic2.eps
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
