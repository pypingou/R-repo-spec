%global packname  FAmle
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.3
Release:          1%{?dist}
Summary:          Maximum Likelihood and Bayesian Estimation of Univariate Probability Distributions

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-mvtnorm 

BuildRequires:    R-devel tex(latex) R-mvtnorm 

%description
This package contains a series of functions that might be useful in
carrying out maximum likelihood and Bayesian estimations of univariate
probability distributions

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
%doc %{rlibdir}/FAmle/html
%doc %{rlibdir}/FAmle/DESCRIPTION
%doc %{rlibdir}/FAmle/doc
%{rlibdir}/FAmle/INDEX
%{rlibdir}/FAmle/help
%{rlibdir}/FAmle/NAMESPACE
%{rlibdir}/FAmle/R
%{rlibdir}/FAmle/Meta
%{rlibdir}/FAmle/libs
%{rlibdir}/FAmle/data

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3-1
- initial package for Fedora