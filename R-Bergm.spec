%global packname  Bergm
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.4
Release:          1%{?dist}
Summary:          Bayesian inference for exponential random graph models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-network R-ergm R-coda R-KernSmooth 

BuildRequires:    R-devel tex(latex) R-network R-ergm R-coda R-KernSmooth 

%description
Functions implementing Bayesian estimation for exponential random graph
models via exchange algorithm

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
%doc %{rlibdir}/Bergm/DESCRIPTION
%doc %{rlibdir}/Bergm/html
%{rlibdir}/Bergm/INDEX
%{rlibdir}/Bergm/Meta
%{rlibdir}/Bergm/R
%{rlibdir}/Bergm/help

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4-1
- initial package for Fedora