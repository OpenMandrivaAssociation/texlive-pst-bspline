Name:		texlive-pst-bspline
Version:	40685
Release:	1
Summary:	Draw cubic Bspline curves and interpolations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-bspline
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-bspline.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-bspline.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/dvips/pst-bspline
%{_texmfdistdir}/tex/generic/pst-bspline
%{_texmfdistdir}/tex/latex/pst-bspline
%doc %{_texmfdistdir}/doc/generic/pst-bspline

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}
