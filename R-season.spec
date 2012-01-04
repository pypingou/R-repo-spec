%global packname  season
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2.6
Release:          1%{?dist}
Summary:          Seasonal analysis of health data

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-6.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-lattice R-MASS R-mgcv R-survival R-coda 

BuildRequires:    R-devel tex(latex) R-lattice R-MASS R-mgcv R-survival R-coda 

%description
Routines for the seasonal analysis of health data, including regression
models, time-stratified case-crossover, plotting functions and residual
checks. Thanks to Yuming Guo for checking the case-crossover code.

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
%doc %{rlibdir}/season/CITATION
%doc %{rlibdir}/season/DESCRIPTION
%doc %{rlibdir}/season/html
%{rlibdir}/season/help
%{rlibdir}/season/R
%{rlibdir}/season/INDEX
%{rlibdir}/season/NAMESPACE
%{rlibdir}/season/data
%{rlibdir}/season/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.6-1
- initial package for Fedora