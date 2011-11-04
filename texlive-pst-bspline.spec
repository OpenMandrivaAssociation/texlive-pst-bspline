# revision 23632
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-bspline
# catalog-date 2011-08-20 10:41:50 +0200
# catalog-license other-free
# catalog-version 1.44
Name:		texlive-pst-bspline
Version:	1.44
Release:	1
Summary:	Draw cubic Bspline curves and interpolations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-bspline
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-bspline.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-bspline.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package draws uniform, cubic B-spline curves, open and
closed, based on a sequence of B-spline control points. There
is also code which permits drawing the open or closed cubic
Bspline curve interpolating a sequence of points. Graphical
output is created using PStricks.

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
%{_texmfdistdir}/dvips/pst-bspline/pst-bspline.pro
%{_texmfdistdir}/tex/generic/pst-bspline/pst-bspline.tex
%{_texmfdistdir}/tex/latex/pst-bspline/pst-bspline.sty
%doc %{_texmfdistdir}/doc/generic/pst-bspline/README
%doc %{_texmfdistdir}/doc/generic/pst-bspline/pst-bspline-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-bspline/pst-bspline-doc.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
