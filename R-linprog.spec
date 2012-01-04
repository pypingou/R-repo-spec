%global packname  linprog
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.9.0
Release:          1%{?dist}
Summary:          Linear Programming / Optimization

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-lpSolve 

BuildRequires:    R-devel tex(latex) R-lpSolve 

%description
This package can be used to solve Linear Programming / Linear Optimization
problems by using the simplex algorithm.

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
%doc %{rlibdir}/linprog/html
%doc %{rlibdir}/linprog/DESCRIPTION
%{rlibdir}/linprog/Meta
%{rlibdir}/linprog/NAMESPACE
%{rlibdir}/linprog/INDEX
%{rlibdir}/linprog/R
%{rlibdir}/linprog/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.0-1
- initial package for Fedora