%global packname  RMediation
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          An R Package for Mediation Analysis Confidence Intervals

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-base 

BuildRequires:    R-devel tex(latex) R-base 

%description
RMediation provides functions to compute confidence intervals, percentiles
and quantiles for the mediated effect and the product of two normal random

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
%doc %{rlibdir}/RMediation/DESCRIPTION
%doc %{rlibdir}/RMediation/CITATION
%doc %{rlibdir}/RMediation/html
%{rlibdir}/RMediation/Meta
%{rlibdir}/RMediation/help
%{rlibdir}/RMediation/libs
%{rlibdir}/RMediation/R
%{rlibdir}/RMediation/INDEX
%{rlibdir}/RMediation/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora