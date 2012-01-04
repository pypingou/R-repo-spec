%global packname  B2Z
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.4
Release:          1%{?dist}
Summary:          Bayesian Two-Zone Model

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-numDeriv R-coda R-mvtnorm 

BuildRequires:    R-devel tex(latex) R-numDeriv R-coda R-mvtnorm 

%description
This package fits the Bayesian two-Zone Models.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{rlibdir}/B2Z/DESCRIPTION
%doc %{rlibdir}/B2Z/CITATION
%doc %{rlibdir}/B2Z/html
%{rlibdir}/B2Z/data
%{rlibdir}/B2Z/NAMESPACE
%{rlibdir}/B2Z/INDEX
%{rlibdir}/B2Z/Meta
%{rlibdir}/B2Z/help
%{rlibdir}/B2Z/R

%changelog
* Sun Nov 20 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4-1
- initial package for Fedora