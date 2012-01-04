%global packname  HPbayes
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1
Release:          1%{?dist}
Summary:          Heligman Pollard mortality model parameter estimation using Bayesian Melding with Incremental Mixture Importance Sampling

Group:            Applications/Engineering 
License:          Unlimited
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-MASS R-mvtnorm R-corpcor R-numDeriv R-stats R-boot 

BuildRequires:    R-devel tex(latex) R-MASS R-mvtnorm R-corpcor R-numDeriv R-stats R-boot 

%description
This package provides all the functions necessary to estimate the 8
parameters of the Heligman Pollard mortality model using a Bayesian
Melding procedure with IMIS as well as to convert those parameters into
age-specifc probabilities of death and a corresponding life table

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1-1
- initial package for Fedora