%global packname  RWebMA
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.0.2
Release:          1%{?dist}
Summary:          RWebMA

Group:            Applications/Engineering 
License:          BSD
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-XML 

BuildRequires:    R-devel tex(latex) R-XML 

%description
This package is an interface for R of WebMA of Yahoo! Japan.

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
%doc %{rlibdir}/RWebMA/html
%doc %{rlibdir}/RWebMA/DESCRIPTION
%{rlibdir}/RWebMA/Meta
%{rlibdir}/RWebMA/INDEX
%{rlibdir}/RWebMA/help
%{rlibdir}/RWebMA/NAMESPACE
%{rlibdir}/RWebMA/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.2-1
- initial package for Fedora