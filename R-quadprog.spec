%global packname  quadprog
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.5.4
Release:          1%{?dist}
Summary:          Functions to solve Quadratic Programming Problems.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.5-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package contains routines and documentation for solving quadratic
programming problems.

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
%doc %{rlibdir}/quadprog/html
%doc %{rlibdir}/quadprog/DESCRIPTION
%{rlibdir}/quadprog/INDEX
%{rlibdir}/quadprog/Meta
%{rlibdir}/quadprog/NAMESPACE
%{rlibdir}/quadprog/libs
%{rlibdir}/quadprog/R
%{rlibdir}/quadprog/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.5.4-1
- initial package for Fedora