%global tl_name pst-bspline
%global tl_revision 40685

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.62
Release:	%{tl_revision}.1
Summary:	Draw cubic Bspline curves and interpolations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-bspline
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-bspline.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-bspline.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package draws uniform, cubic B-spline curves, open and closed, based
on a sequence of B-spline control points. There is also code which
permits drawing the open or closed cubic Bspline curve interpolating a
sequence of points. Graphical output is created using PStricks.

