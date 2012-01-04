%global packname  VecStatGraphs3D
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Vector analysis using graphical and analytical methods in 3D.

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-rgl R-misc3d R-tcltk R-MASS 


BuildRequires:    R-devel tex(latex) R-rgl R-misc3d R-tcltk R-MASS



%description
This package performs a 3D statistical analysis, both numerical and
graphic, of a set of vectors. Since a vector has three components (a
module and two angles) vector analysis is performed in two stages: modules
are analyzed by means of linear statistics and orientations are analyzed
by spherical statistics. Tests and spherical statistic parameters are
accompanied by a full range of graphing: vector maps, density maps,
distribution modules and angles. The tests, spherical statistic parameters
and graphs allow us detecting another distribution properties (I.e.
anisotropy) and outliers.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2-1
- initial package for Fedora