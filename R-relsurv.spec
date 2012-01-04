%global packname  relsurv
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.6.4
Release:          1%{?dist}
Summary:          Relative survival

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-survival R-splines R-date 

BuildRequires:    R-devel tex(latex) R-survival R-splines R-date 

%description
Various functions for relative survival analysis.

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
%doc %{rlibdir}/relsurv/DESCRIPTION
%doc %{rlibdir}/relsurv/html
%{rlibdir}/relsurv/Meta
%{rlibdir}/relsurv/INDEX
%{rlibdir}/relsurv/R
%{rlibdir}/relsurv/help
%{rlibdir}/relsurv/data

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6.4-1
- initial package for Fedora