%global packname  GeneralizedHyperbolic
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2.0
Release:          1%{?dist}
Summary:          The generalized hyperbolic distribution

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-DistributionUtils 

BuildRequires:    R-devel tex(latex) R-DistributionUtils 

%description
This package provides functions for the hyperbolic and related
distributions. Density, distribution and quantile functions and random
number generation are provided for the hyperbolic distribution, the
generalized hyperbolic distribution, the generalized inverse Gaussian
distribution and the skew-Laplace distribution. Additional functionality
is provided for the hyperbolic distribution, including fitting of the
hyperbolic to data.

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
%doc %{rlibdir}/GeneralizedHyperbolic/NEWS
%doc %{rlibdir}/GeneralizedHyperbolic/DESCRIPTION
%doc %{rlibdir}/GeneralizedHyperbolic/html
%{rlibdir}/GeneralizedHyperbolic/R
%{rlibdir}/GeneralizedHyperbolic/NAMESPACE
%{rlibdir}/GeneralizedHyperbolic/Meta
%{rlibdir}/GeneralizedHyperbolic/help
%{rlibdir}/GeneralizedHyperbolic/data
%{rlibdir}/GeneralizedHyperbolic/INDEX
%{rlibdir}/GeneralizedHyperbolic/unitTests

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.0-1
- initial package for Fedora