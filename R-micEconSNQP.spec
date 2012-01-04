%global packname  micEconSNQP
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.6.2
Release:          1%{?dist}
Summary:          Symmetric Normalized Quadratic Profit Function

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.6-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-systemfit R-miscTools R-micEcon R-MASS 

BuildRequires:    R-devel tex(latex) R-systemfit R-miscTools R-micEcon R-MASS 

%description
Production analysis with the Symmetric Normalized Quadratic (SNQ) profit

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
%doc %{rlibdir}/micEconSNQP/html
%doc %{rlibdir}/micEconSNQP/DESCRIPTION
%{rlibdir}/micEconSNQP/Meta
%{rlibdir}/micEconSNQP/INDEX
%{rlibdir}/micEconSNQP/R
%{rlibdir}/micEconSNQP/NAMESPACE
%{rlibdir}/micEconSNQP/help

%changelog
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6.2-1
- initial package for Fedora