%global packname  futile.matrix
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Futile matrix utilities

Group:            Applications/Engineering 
License:          LGPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-futile.logger R-futile.any 

BuildRequires:    R-devel tex(latex) R-futile.logger R-futile.any 

%description
A collection of matrix manipulation functions

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
%doc %{rlibdir}/futile.matrix/DESCRIPTION
%doc %{rlibdir}/futile.matrix/html
%{rlibdir}/futile.matrix/R
%{rlibdir}/futile.matrix/Meta
%{rlibdir}/futile.matrix/INDEX
%{rlibdir}/futile.matrix/NAMESPACE
%{rlibdir}/futile.matrix/help

%changelog
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora