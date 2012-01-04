%global packname  RHmm
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.5.0
Release:          1%{?dist}
Summary:          Hidden Markov Models simulations and estimations

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-MASS R-nlme 

BuildRequires:    R-devel tex(latex) R-MASS R-nlme 

%description
Discrete, univariate or multivariate gaussian, mixture of univariate or
multivariate gaussian HMM functions for simulation and estimation.

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
%doc %{rlibdir}/RHmm/DESCRIPTION
%doc %{rlibdir}/RHmm/html
%{rlibdir}/RHmm/data
%{rlibdir}/RHmm/R
%{rlibdir}/RHmm/NAMESPACE
%{rlibdir}/RHmm/INDEX
%{rlibdir}/RHmm/help
%{rlibdir}/RHmm/libs
%{rlibdir}/RHmm/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.5.0-1
- initial package for Fedora