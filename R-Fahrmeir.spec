%global packname  Fahrmeir
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.4
Release:          1%{?dist}
Summary:          Data from the book "Multivariate Statistical Modelling Based on Generalized Linear Models", first edition, by Ludwig Fahrmeir and Gerhard Tutz

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats 

BuildRequires:    R-devel tex(latex) R-stats 

%description
Data and functions for the book "Multivariate Statistical Modelling Based
on Generalized Linear Models", version 1, by Ludwig Fahrmeir and Gerhard

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
%doc %{rlibdir}/Fahrmeir/DESCRIPTION
%doc %{rlibdir}/Fahrmeir/html
%{rlibdir}/Fahrmeir/INDEX
%{rlibdir}/Fahrmeir/NAMESPACE
%{rlibdir}/Fahrmeir/help
%{rlibdir}/Fahrmeir/data
%{rlibdir}/Fahrmeir/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4-1
- initial package for Fedora