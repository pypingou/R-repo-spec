%global packname  VecStatGraphs2D
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.4
Release:          1%{?dist}
Summary:          Vector analysis using graphical and analytical methods in 2D

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS 

BuildRequires:    R-devel tex(latex) R-MASS 

%description
This package performs a 2D statistical analysis, both numerical and
graphic, of a set of vectors. Since a vector has two components (module
and azimuth) vector analysis is performed in three stages: modules are
analyzed by means of linear statistics, azimuths are analyzed by circular
statistics, and the joint analysis of modules and azimuths is done using
density maps that allow detecting another distribution properties (I.e.
anisotropy) and outliers. Tests and circular statistic parameters have
associated a full range of graphing: histograms, maps of distributions,
point maps, vector maps, density maps, distribution modules and azimuths.

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
%doc %{rlibdir}/VecStatGraphs2D/DESCRIPTION
%doc %{rlibdir}/VecStatGraphs2D/html
%{rlibdir}/VecStatGraphs2D/R
%{rlibdir}/VecStatGraphs2D/data
%{rlibdir}/VecStatGraphs2D/NAMESPACE
%{rlibdir}/VecStatGraphs2D/INDEX
%{rlibdir}/VecStatGraphs2D/help
%{rlibdir}/VecStatGraphs2D/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4-1
- initial package for Fedora