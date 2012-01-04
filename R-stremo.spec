%global packname  stremo
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2
Release:          1%{?dist}
Summary:          Functions to help the process of learning structural equation modelling

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-lavaan R-numDeriv R-MASS 

BuildRequires:    R-devel tex(latex) R-lavaan R-numDeriv R-MASS 

%description
Functions to assist the process of learning structural equation modeling

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
%doc %{rlibdir}/stremo/DESCRIPTION
%doc %{rlibdir}/stremo/html
%{rlibdir}/stremo/NEWS.Rd
%{rlibdir}/stremo/data
%{rlibdir}/stremo/NAMESPACE
%{rlibdir}/stremo/Meta
%{rlibdir}/stremo/help
%{rlibdir}/stremo/INDEX
%{rlibdir}/stremo/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2-1
- initial package for Fedora