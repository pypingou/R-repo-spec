%global packname  mar1s
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.0.1
Release:          1%{?dist}
Summary:          Multiplicative AR(1) with Seasonal Processes

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.0-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-cmrutils R-fda 

BuildRequires:    R-devel tex(latex) R-cmrutils R-fda 

%description
Multiplicative AR(1) with Seasonal is a stochastic process model built on
top of AR(1). The package provides the following procedures for MAR(1)S
processes: fit, compose, decompose, advanced simulate and predict.

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
%doc %{rlibdir}/mar1s/DESCRIPTION
%doc %{rlibdir}/mar1s/COPYING
%doc %{rlibdir}/mar1s/html
%{rlibdir}/mar1s/NAMESPACE
%{rlibdir}/mar1s/Meta
%{rlibdir}/mar1s/INDEX
%{rlibdir}/mar1s/R
%{rlibdir}/mar1s/help
%{rlibdir}/mar1s/data

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0.1-1
- initial package for Fedora