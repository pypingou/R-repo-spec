%global packname  prLogistic
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Estimation of Prevalence Ratios using Logistic Models

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-boot R-methods R-stats R-stats4 R-lme4 R-Hmisc 


BuildRequires:    R-devel tex(latex) R-boot R-methods R-stats R-stats4 R-lme4 R-Hmisc



%description
Estimation of prevalence ratios using logistic models and confidence
intervals with delta and bootstrap methods.

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
%doc %{rlibdir}/prLogistic/DESCRIPTION
%doc %{rlibdir}/prLogistic/html
%{rlibdir}/prLogistic/R
%{rlibdir}/prLogistic/INDEX
%{rlibdir}/prLogistic/data
%{rlibdir}/prLogistic/NAMESPACE
%{rlibdir}/prLogistic/Meta
%{rlibdir}/prLogistic/help

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora