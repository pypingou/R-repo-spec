%global packname  VarianceGamma
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.3.0
Release:          1%{?dist}
Summary:          The Variance Gamma Distribution

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-DistributionUtils R-GeneralizedHyperbolic 

BuildRequires:    R-devel tex(latex) R-DistributionUtils R-GeneralizedHyperbolic 

%description
This package provides functions for the variance gamma distributions.
Density, distribution and quantile functions. Functions for random number
generation and fitting of the variance gamma to data. Also, functions for
computing moments of the variance gamma distribution of any order about
any location. In addition, there are functions for checking the validity
of parameters and to interchange different sets of parameterizatons for
the variance gamma distribution.

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
* Fri Nov 25 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.0-1
- initial package for Fedora