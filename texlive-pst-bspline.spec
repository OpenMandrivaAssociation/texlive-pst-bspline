# revision 25582
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-bspline
# catalog-date 2012-03-07 20:35:45 +0100
# catalog-license lppl1.3
# catalog-version 1.61
Name:		texlive-pst-bspline
Version:	1.62
Release:	1
Summary:	Draw cubic Bspline curves and interpolations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-bspline
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-bspline.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-bspline.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package draws uniform, cubic B-spline curves, open and
closed, based on a sequence of B-spline control points. There
is also code which permits drawing the open or closed cubic
Bspline curve interpolating a sequence of points. Graphical
output is created using PStricks.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pst-bspline/pst-bspline.pro
%{_texmfdistdir}/tex/generic/pst-bspline/pst-bspline.tex
%{_texmfdistdir}/tex/latex/pst-bspline/pst-bspline.sty
%doc %{_texmfdistdir}/doc/generic/pst-bspline/README
%doc %{_texmfdistdir}/doc/generic/pst-bspline/pst-bspline-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-bspline/pst-bspline-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Mar 27 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.61-1
+ Revision: 787733
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.44-2
+ Revision: 755224
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.44-1
+ Revision: 719337
- texlive-pst-bspline
- texlive-pst-bspline
- texlive-pst-bspline
- texlive-pst-bspline

