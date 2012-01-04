%global packname  BayesX
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.5
Release:          1%{?dist}
Summary:          R Utilities Accompanying the Software Package BayesX

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-akima R-shapefiles 
Requires:         R-sp R-colorspace R-coda R-splines 

BuildRequires:    R-devel tex(latex) R-akima R-shapefiles
BuildRequires:    R-sp R-colorspace R-coda R-splines 


%description
This package provides functionality for exploring and visualising
estimation results obtained with the software package BayesX for
structured additive regression. It also provides functions that allow to
read, write and manipulate map objects that are required in spatial
analyses performed with BayesX, a free software for estimating structured
additive regression models (http://www.stat.uni-muenchen.de/~bayesx).

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
%doc %{rlibdir}/BayesX/DESCRIPTION
%doc %{rlibdir}/BayesX/html
%{rlibdir}/BayesX/R
%{rlibdir}/BayesX/examples
%{rlibdir}/BayesX/NAMESPACE
%{rlibdir}/BayesX/INDEX
%{rlibdir}/BayesX/ChangeLog
%{rlibdir}/BayesX/help
%{rlibdir}/BayesX/Meta

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.5-1
- initial package for Fedora