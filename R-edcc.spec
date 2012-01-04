%global packname  edcc
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.0
Release:          1%{?dist}
Summary:          Economic Design of Control Charts

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-spc 

BuildRequires:    R-devel tex(latex) R-spc 

%description
This package provide a unified approach for Economic Design of Control
Charts. The main purpose of this package is to find out the optimal
parameters to minimize the cost per unit time.

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
%doc %{rlibdir}/edcc/html
%doc %{rlibdir}/edcc/DESCRIPTION
%{rlibdir}/edcc/INDEX
%{rlibdir}/edcc/R
%{rlibdir}/edcc/NAMESPACE
%{rlibdir}/edcc/help
%{rlibdir}/edcc/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.0-1
- initial package for Fedora