# revision 17694
# category Package
# catalog-ctan /macros/generic/insbox
# catalog-date 2007-01-07 15:47:33 +0100
# catalog-license pd
# catalog-version 2.2
Name:		texlive-insbox
Version:	2.2
Release:	6
Summary:	A TeX macro for inserting pictures/boxes into paragraphs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/generic/insbox
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/insbox.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/insbox.doc.tar.xz
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
%{_texmfdistdir}/tex/generic/insbox/insbox.tex
%doc %{_texmfdistdir}/doc/generic/insbox/demo.tex
%doc %{_texmfdistdir}/doc/generic/insbox/pic1.eps
%doc %{_texmfdistdir}/doc/generic/insbox/pic2.eps

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.2-2
+ Revision: 752796
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.2-1
+ Revision: 718722
- texlive-insbox
- texlive-insbox
- texlive-insbox
- texlive-insbox

