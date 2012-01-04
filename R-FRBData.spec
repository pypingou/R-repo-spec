%global packname  FRBData
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.3
Release:          1%{?dist}
Summary:          Download interest rate data from FRB's website

Group:            Applications/Engineering 
License:          BSD
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-xts 


BuildRequires:    R-devel tex(latex) R-xts



%description
This package provides functions which can get financial and economical
data from FRB's website.(http://www.federalreserve.gov)

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
%doc %{rlibdir}/FRBData/DESCRIPTION
%doc %{rlibdir}/FRBData/html
%{rlibdir}/FRBData/INDEX
%{rlibdir}/FRBData/help
%{rlibdir}/FRBData/Meta
RPM build errors:
%{rlibdir}/FRBData/R
%{rlibdir}/FRBData/NAMESPACE

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3-1
- initial package for Fedora